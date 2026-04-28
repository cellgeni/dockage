/*
 * JPEG2000 (compression tag 34712) codec for GDAL internal libtiff.
 * Uses OpenJPEG 2.x to decode JP2/J2K bitstreams stored in TIFF tiles.
 */
#include "tiffiop.h"
#include <openjpeg.h>
#include <string.h>

typedef struct {
    uint8_t *buf;
    size_t   size;
    size_t   alloc;
    size_t   offset;
} JP2KState;

#define LState(tif) ((JP2KState *)(tif)->tif_data)

typedef struct { const uint8_t *data; size_t len; size_t pos; } MS;

static OPJ_SIZE_T ms_read(void *b, OPJ_SIZE_T n, void *ud) {
    MS *m = (MS *)ud;
    size_t r = m->len - m->pos;
    if ((size_t)n > r) n = r;
    if (!n) return (OPJ_SIZE_T)-1;
    memcpy(b, m->data + m->pos, n); m->pos += n; return n;
}
static OPJ_BOOL ms_seek(OPJ_OFF_T o, void *ud) {
    MS *m = (MS *)ud;
    if (o < 0 || (size_t)o > m->len) return OPJ_FALSE;
    m->pos = (size_t)o; return OPJ_TRUE;
}
static OPJ_OFF_T ms_skip(OPJ_OFF_T n, void *ud) {
    MS *m = (MS *)ud;
    size_t r = m->len - m->pos;
    if ((size_t)n > r) n = r;
    m->pos += (size_t)n; return n;
}

static int JP2KFixupTags(TIFF *t) { (void)t; return 1; }
static int JP2KSetupDecode(TIFF *t) { (void)t; return 1; }

static int JP2KPreDecode(TIFF *tif, uint16_t s) {
    static const char mod[] = "JP2KPreDecode";
    JP2KState *sp = LState(tif);
    const uint8_t *comp = (const uint8_t *)tif->tif_rawcp;
    size_t csz = (size_t)tif->tif_rawcc;
    (void)s;
    if (!comp || !csz) { TIFFErrorExtR(tif,mod,"no compressed data"); return 0; }

    OPJ_CODEC_FORMAT fmt = OPJ_CODEC_J2K;
    if (csz >= 12 && comp[0]==0 && comp[1]==0 && comp[2]==0 && comp[3]==12 &&
        comp[4]=='j' && comp[5]=='P' && comp[6]==' ' && comp[7]==' ')
        fmt = OPJ_CODEC_JP2;

    opj_codec_t *codec = opj_create_decompress(fmt);
    if (!codec) { TIFFErrorExtR(tif,mod,"opj_create_decompress failed"); return 0; }
    opj_set_error_handler(codec,NULL,NULL);
    opj_set_warning_handler(codec,NULL,NULL);
    opj_set_info_handler(codec,NULL,NULL);
    opj_dparameters_t p; opj_set_default_decoder_parameters(&p);
    opj_setup_decoder(codec,&p);

    MS ms = {comp, csz, 0};
    opj_stream_t *st = opj_stream_create(csz, OPJ_TRUE);
    if (!st) { opj_destroy_codec(codec); return 0; }
    opj_stream_set_user_data(st,&ms,NULL);
    opj_stream_set_user_data_length(st,csz);
    opj_stream_set_read_function(st,ms_read);
    opj_stream_set_seek_function(st,ms_seek);
    opj_stream_set_skip_function(st,ms_skip);

    opj_image_t *img = NULL;
    if (!opj_read_header(st,codec,&img) || !opj_decode(codec,st,img)) {
        TIFFErrorExtR(tif,mod,"OpenJPEG decode failed");
        opj_stream_destroy(st); opj_destroy_codec(codec);
        if (img) opj_image_destroy(img); return 0;
    }
    opj_stream_destroy(st); opj_destroy_codec(codec);
    if (!img || !img->numcomps) { if(img)opj_image_destroy(img); return 0; }

    uint32_t w=img->comps[0].w, h=img->comps[0].h;
    int nc=img->numcomps, prec=img->comps[0].prec;
    int bps=(prec<=8)?1:2;
    size_t need=(size_t)w*h*nc*bps;

    if (sp->alloc < need) {
        _TIFFfreeExt(tif,sp->buf);
        sp->buf=(uint8_t*)_TIFFmallocExt(tif,(tmsize_t)need);
        if (!sp->buf){opj_image_destroy(img);sp->alloc=0;return 0;}
        sp->alloc=need;
    }
    sp->size=need; sp->offset=0;

    uint8_t *out=sp->buf;
    for (uint32_t y=0;y<h;y++) for (uint32_t x=0;x<w;x++) for (int c=0;c<nc;c++) {
        int32_t v=img->comps[c].data[y*w+x];
        if (bps==1) { *out++=(uint8_t)(v<0?0:v>255?255:v); }
        else { uint16_t u=(uint16_t)(v<0?0:v>65535?65535:v); memcpy(out,&u,2); out+=2; }
    }
    opj_image_destroy(img);
    return 1;
}

static int JP2KDecode(TIFF *tif, uint8_t *buf, tmsize_t occ, uint16_t s) {
    JP2KState *sp=LState(tif);
    (void)s;
    if (!sp->buf){TIFFErrorExtR(tif,"JP2KDecode","no decoded data");return 0;}
    if (sp->offset+(size_t)occ>sp->size) occ=(tmsize_t)(sp->size-sp->offset);
    memcpy(buf,sp->buf+sp->offset,(size_t)occ); sp->offset+=(size_t)occ;
    return 1;
}

static void JP2KCleanup(TIFF *tif) {
    JP2KState *sp=LState(tif);
    if (sp) _TIFFfreeExt(tif,sp->buf);
    _TIFFfreeExt(tif,tif->tif_data); tif->tif_data=NULL;
    _TIFFSetDefaultCompressionState(tif);
}

int TIFFInitJP2000(TIFF *tif, int scheme) {
    (void)scheme;
    tif->tif_data=(uint8_t*)_TIFFcallocExt(tif,1,(tmsize_t)sizeof(JP2KState));
    if (!tif->tif_data){TIFFErrorExtR(tif,"TIFFInitJP2000","out of memory");return 0;}
    tif->tif_fixuptags=JP2KFixupTags;
    tif->tif_setupdecode=JP2KSetupDecode;
    tif->tif_predecode=JP2KPreDecode;
    tif->tif_decoderow=JP2KDecode;
    tif->tif_decodestrip=JP2KDecode;
    tif->tif_decodetile=JP2KDecode;
    tif->tif_cleanup=JP2KCleanup;
    return 1;
}

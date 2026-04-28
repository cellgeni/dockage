#!/usr/bin/env python3
"""Patch GDAL 3.10.2 source to add JPEG2000-in-TIFF read support."""

# 1. libtiff/CMakeLists.txt — compile tif_jp2000.c and link OpenJPEG
cmake_libtiff = '/tmp/gdal-3.10.2/frmts/gtiff/libtiff/CMakeLists.txt'
with open(cmake_libtiff, 'a') as f:
    f.write("""
if (GDAL_USE_OPENJPEG)
  target_sources(libtiff PRIVATE tif_jp2000.c)
  gdal_target_link_libraries(libtiff PRIVATE ${OpenJPEG_TARGET})
endif ()
""")
print("libtiff/CMakeLists.txt patched")

# 2. frmts/gtiff/CMakeLists.txt — expose OpenJPEG include dirs to GTiff target
cmake_gtiff = '/tmp/gdal-3.10.2/frmts/gtiff/CMakeLists.txt'
with open(cmake_gtiff, 'a') as f:
    f.write("""
if (GDAL_USE_OPENJPEG AND OpenJPEG_TARGET)
  target_include_directories(gdal_GTIFF PRIVATE
    $<TARGET_PROPERTY:${OpenJPEG_TARGET},INTERFACE_INCLUDE_DIRECTORIES>)
endif ()
""")
print("frmts/gtiff/CMakeLists.txt patched")

# 3. geotiff.cpp — include header, declare variable, register/deregister (unconditional)
geotiff = '/tmp/gdal-3.10.2/frmts/gtiff/geotiff.cpp'
src = open(geotiff).read()

# 3a. Include tif_jp2000.h after tif_jxl.h
old = '#include "tif_jxl.h"'
new = '#include "tif_jxl.h"\n#include "tif_jp2000.h"'
assert old in src, "Cannot find tif_jxl.h include"
src = src.replace(old, new, 1)

# 3b. Declare pJP2000Codec AFTER the #ifdef HAVE_JXL block (not inside it)
old = 'static TIFFCodec *pJXLCodecDNG17 = nullptr;\n#endif'
new = 'static TIFFCodec *pJXLCodecDNG17 = nullptr;\n#endif\nstatic TIFFCodec *pJP2000Codec = nullptr;'
assert old in src, "Cannot find pJXLCodecDNG17 / #endif block"
src = src.replace(old, new, 1)

# 3c. Register JP2000 codec just after the JXL #endif
old = '#endif\n\n    _ParentExtender = TIFFSetTagExtender(GTiffTagExtender);'
new = ('#endif\n'
       '    if (pJP2000Codec == nullptr)\n'
       '        pJP2000Codec = TIFFRegisterCODEC(COMPRESSION_JP2000, "JP2000", TIFFInitJP2000);\n\n'
       '    _ParentExtender = TIFFSetTagExtender(GTiffTagExtender);')
assert old in src, "Cannot find _ParentExtender insertion point"
src = src.replace(old, new, 1)

# 3d. Deregister JP2000 codec in cleanup
old = '    pJXLCodecDNG17 = nullptr;\n#endif\n}'
new = ('    pJXLCodecDNG17 = nullptr;\n#endif\n'
       '    if (pJP2000Codec)\n'
       '        TIFFUnRegisterCODEC(pJP2000Codec);\n'
       '    pJP2000Codec = nullptr;\n}')
assert old in src, "Cannot find pJXLCodecDNG17 cleanup"
src = src.replace(old, new, 1)

open(geotiff, 'w').write(src)
print("geotiff.cpp patched")
print("All patches applied successfully")

#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 Wellcome Sanger Institute

"""
This script will slice the image in XY dimension and save the slices coordinates in json files
"""
import fire
from aicsimageio import AICSImage
import os
from cellpose import core, io, models
import numpy as np
from shapely import Polygon, wkt, MultiPolygon
from glob import glob
import tifffile
import zarr

import logging

logging.basicConfig(level=logging.INFO)

VERSION="0.1.1"


def main(
    image:str,
    x_min:int, x_max:int, y_min:int, y_max:int,
    out_dir:str,
    cell_diameter:int=30,
    cellpose_model:str="cyto3",
    zs:list=[0],
    channels:list=[0, 0],
    resolution_level:int=0,
    **cp_params
    ):

    logging.info(f"Loading Cellpose model: {cellpose_model} (GPU: {core.use_gpu()})")
    model = models.Cellpose(gpu=core.use_gpu(), model_type=cellpose_model)
    # model = denoise.CellposeDenoiseModel(
    #     gpu=core.use_gpu(),
    #     model_type=cellpose_model,
    #     restore_type="denoise_cyto3",
    #     chan2_restore=False
    # )

    if image.endswith(".tif") or image.endswith(".tiff"):
        store = tifffile.imread(image, aszarr=True)
        zgroup = zarr.open(store, mode="r")
        image = zgroup[resolution_level]

        crop = image[y_min:y_max, x_min:y_max]
    else:
        img = AICSImage(image)
        ch_ind = channels[0] if len(np.unique(channels)) == 1 else channels
        lazy_one_plane = img.get_image_dask_data(
            "ZCYX",
            T=0, # only one time point is allowed for now
            C=ch_ind,
            Z=zs)
        crop = lazy_one_plane[:, :, y_min:y_max, x_min:x_max].compute()

    masks, flows, _, _ = model.eval(
        crop,
        channels=channels,
        diameter=cell_diameter,
        channel_axis=1,
        z_axis=0,
        **cp_params,
    )
    os.mkdir(out_dir)
    io.save_masks(
        np.squeeze(crop),
        masks,
        flows,
        file_names=out_dir,
        save_txt=True,
        png=True,
        tif=False,
        save_flows=False,
        save_outlines=True,
        savedir=out_dir,
    )
    # convert cellpose outlines to WTK
    logging.info(f"Converting outlines to WKT format")
    # prefix_list = out_dir.split(".")
    # if len(prefix_list) > 1:
    #     prefix = ".".join(prefix_list[:-1])
    # else:
    #     prefix = prefix_list[0]
    # outlines_file = os.path.join(out_dir, f"{prefix}_cp_outlines.txt")
    outline_file = glob(f"{out_dir}/*_cp_outlines.txt")

    if len(outline_file) > 0:
    # if os.path.exists(outlines_file):
        wkts = []
        with open(outline_file[0], "rt") as f:
            for line in f.readlines():
                # split by comma and make integer
                try:
                    outline = list(map(int, line.strip().split(",")))
                except:
                    continue
                outline = np.array(list(zip(outline[::2], outline[1::2])))
                # transport tile coordinats to original image coordinates
                outline[:, 0] += x_min
                outline[:, 1] += y_min
                poly = Polygon(outline).buffer(0)
                if isinstance(poly, MultiPolygon):
                    poly = poly.geoms[0]
                wkts.append(poly)

        wkt_filename = os.path.join(out_dir, f"{out_dir}_cp_outlines.wkt")
        with open(wkt_filename, "wt") as f:
            f.write(wkt.dumps(MultiPolygon(wkts)))
    else:
        logging.info("No outlines file found")
        with open(os.path.join(out_dir, f"{out_dir}_cp_outlines.wkt"), "wt") as f:
            f.write("")


if __name__ == "__main__":
    options = {
        "run": main,
        "version": VERSION,
    }
    fire.Fire(options)

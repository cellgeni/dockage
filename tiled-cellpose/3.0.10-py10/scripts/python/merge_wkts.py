#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 Wellcome Sanger Institute
import fire
import logging

import shapely
import shapely.ops
import shapely.wkt
import tqdm

# configure logging
logging.basicConfig(level="INFO", format="[%(asctime)s][%(levelname)s] %(message)s")

VERSION="0.0.1"

def merge(sample_id:str, *wkts: list):
    """
    Main function to merge image segmentation tile outlines into a single segmentation file.
    The assumption is that the polygons were already translocated to the same coordinate system.

    Parameters:
        outlines_path (str): The path to the WKT outline segmentation tiles.
    """
    polygons = []
    logging.info(f"Collecting WKT files in '{wkts}'")
    for wkt_file in tqdm.tqdm(wkts):
        # Load multipolygon from WKT file
        with open(wkt_file, "rt") as wkt:
            lines = wkt.read()
            if len(lines) > 0:
                polygons.append(shapely.wkt.loads(lines).buffer(-1).simplify(1))
            else:
                print(lines)
                logging.warning(f"Empty file: {wkt_file}")

    logging.info(f"Merging overlapping polygons")
    stitched_polygons = shapely.ops.unary_union(polygons).buffer(1)

    logging.info(f"Save GeoJSON output")
    with open(f"{sample_id}_merged.geojson", "w") as f:
        f.write(shapely.to_geojson(stitched_polygons))

    logging.info(f"Save WKT output")
    with open(f"{sample_id}_merged.wkt", "w") as f:
        f.write(shapely.wkt.dumps(stitched_polygons))


if __name__ == "__main__":
    options = {
        "run": merge,
        "version": VERSION,
    }
    fire.Fire(options)
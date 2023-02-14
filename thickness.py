# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 23:39:45 2022

@author: pauls
"""

import os
import fiona
import rasterio
from rasterio.mask import mask
from rasterio.plot import show 
from rasterio.warp import calculate_default_transform, reproject, Resampling
import geopandas as gpd
from osgeo import gdal
import glob
import rasterstats
import pandas as pd

folder_path = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/thickness_farinotti"
thickness_farinotti_RGI60_17 = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/thickness_farinotti/thickness_farinotti_RGI60_17.tif"
search_criteria = "R*.tif"
prev_demlist = os.path.join(folder_path,search_criteria)
demlist = glob.glob(prev_demlist)
print(demlist)

vrt_raster = gdal.BuildVRT("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/thickness_farinotti/thickness_farinotti_RGI60_17.vrt",demlist) 
gdal.Translate("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/thickness_farinotti/thickness_farinotti_RGI60_17.tif",vrt_raster)
vrt_raster = None
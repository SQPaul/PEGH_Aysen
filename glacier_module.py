# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 13:53:39 2022

@author: pauls
"""

import pandas as pd
from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt 
import rasterio as rio

dvdt = gdal.Open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet.tif")

dvdt32718 = gdal.Warp("dvdt32718",dvdt,dstSRS="EPSG:32718",resampleAlg="bilinear") 
a = rio.open(dvdt32718)

dvdt_array = np.array(dvdt32718)

with rio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt.tif",driver="GTiff",height=dvdt32718.height,width=dvdt32718.width,count=1,dtype=dvdt_array.dtype,crs=dvdt32718.crs,transform=dvdt32718.meta["transform"]) as dst:
    dst.write(dvdt_array,indexes=1)

#---------------------------------------

import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
from rasterio.mask import mask
from shapely.geometry import box
import geopandas as gpd
from fiona.crs import from_epsg
import pycrs

#input and output
dvdt = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet.tif"
dvdt_f = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_Aysen.tif"

#Open raster in read mode
data = rio.open(dvdt)
show((data,1),cmap="terrain")

#-----------------------------------------

import rasterio  as rio 
from rasterio.plot import show
import numpy as np
import pandas as pd
import fiona
import rasterio.mask

dvdt_raster = rio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet.tif")
show(dvdt_raster)

dvdt_narray = dvdt_raster.read(1)

dvdt = pd.DataFrame(dvdt_narray)

a = pd.DataFrame.max(dvdt)

with fiona.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0.shp", "r") as shapefile:
    shapes = [feature["geometry"] for feature in shapefile]
    
with rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet32718.tif") as src:
    out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
    out_meta = src.meta
    
out_meta.update({"driver": "GTiff",
                 "height": out_image.shape[1],
                 "width": out_image.shape[2],
                 "transform": out_transform})

with rasterio.open("RGB.byte.masked.tif", "w", **out_meta) as dest:
    dest.write(out_image)
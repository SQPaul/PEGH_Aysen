# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:43:39 2022

@author: pauls
"""
#import os
#import fiona
import rasterio
#from rasterio.mask import mask
#from rasterio.plot import show 
#from rasterio.warp import calculate_default_transform, reproject, Resampling
#import geopandas as gpd
from osgeo import gdal
#import glob
#import rasterstats
#import pandas as pd
from rasterio.enums import Resampling
import numpy as np

#RESAMPLING

factor=1/4

with rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/volume_km3_farinotti.tif") as dataset:
    data = dataset.read(
        out_shape=(
            dataset.count,
            int(dataset.height*factor),
            int(dataset.width*factor)
            ),
        resampling=Resampling.bilinear
    )        
    transform=dataset.transform*dataset.transform.scale(
        (dataset.width/data.shape[-1]),
        (dataset.height/data.shape[-2])
    )

new_dimension_raster = data[0,:,:]

vrt_raster = gdal.BuildVRT("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/volum_0.25.vrt",new_dimension_raster) 
gdal.Translate("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/volum_0.25.tif",vrt_raster)
vrt_raster = None
    
#REPROJECTING SHP
glaciers_shp = gpd.read_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0.shp")
#glaciers_shp["geometry"][0] #Plot just one geometry
#glaciers_shp.plot() #Plot all shp 
glacier_32719 = glaciers_shp.to_crs({"init":"EPSG:32719"})
glacier_32719.to_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0_32719.shp")

#CLIPING RASTER BY MASK

#know list of docs
#folder_path = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input"
#doc_names = os.listdir(folder_path)
#doc_names

#Import documents
#glaciers_shp = fiona.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0_32719.shp") #Another way to import
dvdt = rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet.tif")
glaciers_shp = fiona.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0_32719.shp")

for i in range(len(glaciers_shp)):
    glaciers_geom = [glaciers_shp[i]["geometry"]]
    outImage, outTransform = mask(dvdt,glaciers_geom,crop=True)
    outMeta = dvdt.meta
    outMeta.update({"driver":"GTiff",
                    "height":outImage.shape[1],
                    "width":outImage.shape[2],
                    "transform":outTransform})
    name = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/dvdt_aysen_"+str(i)+".tif"
    dvdt_aysen = rasterio.open(name,"w",**outMeta)
    dvdt_aysen.write(outImage)
    dvdt_aysen.close()    

#JOIN RASTERS IN ONE
folder_path = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet"
aysen_glaciers = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/Aysen_glaciers32719.tif"
search_criteria = "d*.tif"
prev_demlist = os.path.join(folder_path,search_criteria)
demlist = glob.glob(prev_demlist)
print(demlist)

vrt_raster = gdal.BuildVRT("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/dvdt_hugonnet_Aysen.vrt",demlist) 
gdal.Translate("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/dvdt_hugonnet_Aysen.tif",vrt_raster)
vrt_raster = None

#ZONAL STATISTICS

#reprojecting shp
bands = gpd.read_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/QGIS/Cuenca/Bandas_elevacion_v4.shp")
bands.plot()
bands_32719 = bands.to_crs({"init":"EPSG:32719"})
bands_32719.to_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/bands_32719.shp")

#Importing reprojected shp
bands_shp = gpd.read_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/bands_32719.shp")
bands_shp.plot()

aysen_glaciers = rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_hugonnet/dvdt_hugonnet_Aysen.tif")
show(aysen_glaciers)
aysen_glaciers.meta
affine = aysen_glaciers.transform

#Raster to np array
aysen_glaciers_array = aysen_glaciers.read(1)

#Calculating zonal statistics 
avg_glac = rasterstats.zonal_stats(bands_shp,
                                   aysen_glaciers_array,
                                   affine=affine,
                                   stats=["mean"],
                                   geojson_out=True)

avg_glac_table = []

for i in range(len(avg_glac)):
    avg_glac_table.append(avg_glac[i]["properties"])

avg_glacier_att = pd.DataFrame(avg_glac_table)
print(avg_glacier_att)

print(avg_glacier_att["mean"])

bands_shp["dvdt_hugonnet"] = avg_glacier_att["mean"]

aysen_glacier_shp = bands_shp.to_crs({"init":"EPSG:32718"})
aysen_glacier_shp.to_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_dvdt.shp")

# Calculate zonal statistics for Volumen

vol_f = rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/volume_km3_farinotti.tif")
vol_f.meta
vol_f.crs

glaciers_shp = gpd.read_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0.shp")
glacier_4326 = glaciers_shp.to_crs({"init":"EPSG:4326"})
glacier_4326.to_file("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0_4326.shp")

glaciers_4326 = fiona.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/Aysen_glaciers_RGIv6.0_4326.shp")

for i in range(len(glaciers_4326)):
    glaciers_geom = [glaciers_4326[i]["geometry"]]
    outImage, outTransform = mask(vol_f,glaciers_geom,crop=True)
    outMeta = vol_f.meta
    outMeta.update({"driver":"GTiff",
                    "height":outImage.shape[1],
                    "width":outImage.shape[2],
                    "transform":outTransform})
    name = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/v_farinotti/vol_aysen_"+str(i)+".tif"
    v_farinotti = rasterio.open(name,"w",**outMeta)
    v_farinotti.write(outImage)
    v_farinotti.close()    

folder_path = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/v_farinotti"
v_aysen_glaciers = r"C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/v_farinotti/v_aysen_glaciers.tif"
search_criteria = "v*.tif"
prev_demlist = os.path.join(folder_path,search_criteria)
demlist = glob.glob(prev_demlist)
print(demlist)

vrt_raster = gdal.BuildVRT("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/v_farinotti/v_farinotti_Aysen.vrt",demlist) 
gdal.Translate("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/v_farinotti/v_farinotti_Aysen.tif",vrt_raster)
vrt_raster = None

#-----------------------------------

#IMPORT RASTER
dvdt_32719 = rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dhdt_Hugonnet.tif") 
#print(dvdt_32719.crs)

#DESTINATION RASTER PROPERTIES
crs_dst = {"init" : "EPSG:32718"}
#print(crs_dst)
transform, width, height = calculate_default_transform(dvdt_32719.crs, crs_dst, dvdt_32719.width, dvdt_32719.height, *dvdt_32719.bounds)
kwargs = dvdt_32719.meta.copy()
kwargs.update({
        "crs":crs_dst,
        "transform":transform,
        "width":width,
        "height":height
            })

#REPROJECT
dvdt_32718 = rasterio.open("C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Modulo_glaciar/input/dvdt_32718.tif","w",**kwargs)
reproject(source=rasterio.band(dvdt_32719,1),
          destination=rasterio.band(dvdt_32718,1),
          src_crs=dvdt_32719.crs,
          dst_crs=crs_dst,
          resampling=Resampling.bilinear
          )
dvdt_32718.close()
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:49:33 2021

@author: pauls
"""

from osgeo import gdal, gdalconst
from pcraster import * 
from os import chdir, getcwd

f_dir = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/QGIS/Python"
chdir(f_dir)

def ConvertToPCRaster (src_fname,dst_fname,ot,VS):
    src_ds = gdal.Open(src_fname)
    dst_ds = gdal.Translate(dst_fname, src_ds, format="PCRaster", outputType=ot, metadataOptions=VS)
    src_ds = None
    dst_ds = None

ConvertToPCRaster("dem.tif","dem.map",gdalconst.GDT_Float32,"VS_SCALAR")

#WORK WITH PCRASTER

#1 Import dem and filled
dem = readmap("dem.map")
aguila(dem)
demfilled = lddcreatedem(dem,1e31,1e31,1e31,1e31)
aguila(demfilled)
report(demfilled,"demfilled.map")
 
#2 Create local drain direction and river network
ldd = lddcreate(demfilled,1e31,1e31,1e31,1e31)
report(ldd,"ldd.map")
accuflux = accuflux(ldd,1)
report(accuflux,"accuflux.map")

#3 Analyze strahler order
strahler = streamorder(ldd)
aguila(strahler)
report(strahler,"strahler.map")

##Repair ldd

#lddrep = lddrepair(ldd)
#report(lddrep,"lddrep.map")

#4 Define outputs
#4.1 In this step check if the outputs basins are over the accuflux (river network)
#4.2 Convert outputs to raster (points with attr=ID), (ID natural numbers)
#4.3 Convert to pcraster and nominal.map
ConvertToPCRaster("outflow.tif","outflow.map",gdalconst.GDT_Float32,"VS_SCALAR")
outflow_catchment = nominal("outflow.map")
report(outflow_catchment,"outflow_catchment.map")

#5 Delineate basin and subbasins
catchment_2 = catchment(ldd,outflow_catchment)
aguila(catchment_2)
report(catchment_2,"catchment.map")
subbasins = subcatchment(ldd,outputs)
report(subbasins,"subbasins.map")

#----------
ConvertToPCRaster("outflow_lospalos.tif","outflow_lospalos.map",gdalconst.GDT_Float32,"VS_SCALAR")
outflow_lospalos_c = nominal("outflow_lospalos.map")
catchment_lospalos = catchment(ldd,outflow_lospalos_c)
report(catchment_lospalos,"catchment_lospalos.map")

#------------- SUBLAKES

ldd = readmap("ldd.map")
ConvertToPCRaster("outflow_lagos.tif","outflow_lagos.map",gdalconst.GDT_Float32,"VS_SCALAR")
outflow_lakes = nominal("outflow_lagos.map")
subcatchment_lakes = subcatchment(ldd,outflow_lakes)
aguila(subcatchment_lakes)
report(subcatchment_lakes,"sub_lakes_3.map")

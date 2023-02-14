# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 11:31:41 2021

@author: pauls
"""

import openpyxl
import pandas as pd
from os import chdir, getcwd

f_dir = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Datos_hidroclimaticos/costeras/fluvio_costeras/1"
chdir(f_dir)

#PREPROCESS INSTRUCTIONS
#1.- Change "AÑO: " by " ".
#2.- Save xls as xlsx.
#3.- Assign col 1 excel the name of the station.
#4.- Change the sheet name in lines 27 and 29.

n=1
k = (0,1,2,3)
k2 = (0,1)
n = (1,2) #xlsx when the station have data
excel = pd.DataFrame()
excel.insert(0,"Date",None)
excel.insert(1,"RIO CUERVO EN DESEMBOCADURA",None)  #2 Assign name station 
for p in n:
    xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Datos_hidroclimaticos/costeras/fluvio_costeras/"+str(1)+"/"+str(p)+".xlsx"
    dga = pd.read_excel(xlsx,sheet_name="RIO CUERVO EN DESEMBOCADURA",engine="openpyxl") #2 Assign sheet name 
    station = str(dga.iloc[4,3])
    if p != 10: #Change for max number
        years = (dga.iloc[9,1],dga.iloc[9+33,1],dga.iloc[9+33*2,1],dga.iloc[9+33*3,1])
        year_1 = dga.iloc[10:42,1:27]
        year_2 = dga.iloc[42+1:42+1+32+1*0,1:27]
        year_3 = dga.iloc[42+1+32+1:42+1+32*2+1*1,1:27]
        year_4 = dga.iloc[42+1+32*2+1+1:42+1+32*3+1*2,1:27]
        years_df = [year_1,year_2,year_3,year_4] 
        for i in k:
            y = years_df[i]
            for j,col in enumerate(y):
                if j == 0:
                    date = y.iloc[1:32,j]
                if j == 1:
                    jan = pd.DataFrame(years_df[i].iloc[1:32,j])
                    jan.columns=[station]
                    jan.insert(0,"Date",date)
                    jan=jan.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jan.iloc[f,0]=str(jan.iloc[f,0])+"-"+str(1)+"-"+str(years[i])
                if j == 3:
                    feb = pd.DataFrame(years_df[i].iloc[1:32,j])
                    feb.columns=[station]
                    feb.insert(0,"Date",date)
                    feb=feb.reset_index(drop=True)
                    for f,row in feb.iterrows():
                        feb.iloc[f,0]=str(feb.iloc[f,0])+"-"+str(2)+"-"+str(years[i])
                if j == 5:
                    mar = pd.DataFrame(years_df[i].iloc[1:32,j])
                    mar.columns=[station]
                    mar.insert(0,"Date",date)
                    mar=mar.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        mar.iloc[f,0]=str(mar.iloc[f,0])+"-"+str(3)+"-"+str(years[i])
                if j == 7:
                    apr = pd.DataFrame(years_df[i].iloc[1:32,j])
                    apr.columns=[station]
                    apr.insert(0,"Date",date)
                    apr=apr.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        apr.iloc[f,0]=str(apr.iloc[f,0])+"-"+str(4)+"-"+str(years[i])
                if j == 9:
                    may = pd.DataFrame(years_df[i].iloc[1:32,j])
                    may.columns=[station]
                    may.insert(0,"Date",date)
                    may=may.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        may.iloc[f,0]=str(may.iloc[f,0])+"-"+str(5)+"-"+str(years[i])
                if j == 11:
                    jun = pd.DataFrame(years_df[i].iloc[1:32,j])
                    jun.columns=[station]
                    jun.insert(0,"Date",date)
                    jun=jun.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jun.iloc[f,0]=str(jun.iloc[f,0])+"-"+str(6)+"-"+str(years[i])
                if j == 13:
                    jul = pd.DataFrame(years_df[i].iloc[1:32,j])
                    jul.columns=[station]
                    jul.insert(0,"Date",date)
                    jul=jul.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jul.iloc[f,0]=str(jul.iloc[f,0])+"-"+str(7)+"-"+str(years[i])
                if j == 15:
                    aug = pd.DataFrame(years_df[i].iloc[1:32,j])
                    aug.columns=[station]
                    aug.insert(0,"Date",date)
                    aug=aug.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        aug.iloc[f,0]=str(aug.iloc[f,0])+"-"+str(8)+"-"+str(years[i])
                if j == 17:
                    sep = pd.DataFrame(years_df[i].iloc[1:32,j])
                    sep.columns=[station]
                    sep.insert(0,"Date",date)
                    sep=sep.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        sep.iloc[f,0]=str(sep.iloc[f,0])+"-"+str(9)+"-"+str(years[i])
                if j == 19:
                    okt = pd.DataFrame(years_df[i].iloc[1:32,j])
                    okt.columns=[station]
                    okt.insert(0,"Date",date)
                    okt=okt.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        okt.iloc[f,0]=str(okt.iloc[f,0])+"-"+str(10)+"-"+str(years[i])
                if j == 21:
                    nov = pd.DataFrame(years_df[i].iloc[1:32,j])
                    nov.columns=[station]
                    nov.insert(0,"Date",date)
                    nov=nov.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        nov.iloc[f,0]=str(nov.iloc[f,0])+"-"+str(11)+"-"+str(years[i])
                if j == 24:
                    dec = pd.DataFrame(years_df[i].iloc[1:32,j])
                    dec.columns=[station]
                    dec.insert(0,"Date",date)
                    dec=dec.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        dec.iloc[f,0]=str(dec.iloc[f,0])+"-"+str(12)+"-"+str(years[i])
            alldataname = (jan,feb,mar,apr,may,jun,jul,aug,sep,okt,nov,dec)
            alldata = pd.concat(alldataname)
            a = (excel,alldata)
            excel = pd.concat(a)
    else:
        years2 = (dga.iloc[9,1],dga.iloc[9+33,1])
        year_1 = dga.iloc[10:42,1:27]
        year_2 = dga.iloc[42+1:42+1+32+1*0,1:27]
        years2_df = [year_1,year_2] 
        for i in k2:
            y = years2_df[i]
            for j,col in enumerate(y):
                if j == 0:
                    date = y.iloc[1:32,j]
                if j == 1:
                    jan = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    jan.columns=[station]
                    jan.insert(0,"Date",date)
                    jan=jan.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jan.iloc[f,0]=str(jan.iloc[f,0])+"-"+str(1)+"-"+str(years2[i])
                if j == 3:
                    feb = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    feb.columns=[station]
                    feb.insert(0,"Date",date)
                    feb=feb.reset_index(drop=True)
                    for f,row in feb.iterrows():
                        feb.iloc[f,0]=str(feb.iloc[f,0])+"-"+str(2)+"-"+str(years2[i])
                if j == 5:
                    mar = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    mar.columns=[station]
                    mar.insert(0,"Date",date)
                    mar=mar.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        mar.iloc[f,0]=str(mar.iloc[f,0])+"-"+str(3)+"-"+str(years2[i])
                if j == 7:
                    apr = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    apr.columns=[station]
                    apr.insert(0,"Date",date)
                    apr=apr.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        apr.iloc[f,0]=str(apr.iloc[f,0])+"-"+str(4)+"-"+str(years2[i])
                if j == 9:
                    may = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    may.columns=[station]
                    may.insert(0,"Date",date)
                    may=may.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        may.iloc[f,0]=str(may.iloc[f,0])+"-"+str(5)+"-"+str(years2[i])
                if j == 11:
                    jun = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    jun.columns=[station]
                    jun.insert(0,"Date",date)
                    jun=jun.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jun.iloc[f,0]=str(jun.iloc[f,0])+"-"+str(6)+"-"+str(years2[i])
                if j == 13:
                    jul = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    jul.columns=[station]
                    jul.insert(0,"Date",date)
                    jul=jul.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        jul.iloc[f,0]=str(jul.iloc[f,0])+"-"+str(7)+"-"+str(years2[i])
                if j == 15:
                    aug = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    aug.columns=[station]
                    aug.insert(0,"Date",date)
                    aug=aug.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        aug.iloc[f,0]=str(aug.iloc[f,0])+"-"+str(8)+"-"+str(years2[i])
                if j == 17:
                    sep = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    sep.columns=[station]
                    sep.insert(0,"Date",date)
                    sep=sep.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        sep.iloc[f,0]=str(sep.iloc[f,0])+"-"+str(9)+"-"+str(years2[i])
                if j == 19:
                    okt = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    okt.columns=[station]
                    okt.insert(0,"Date",date)
                    okt=okt.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        okt.iloc[f,0]=str(okt.iloc[f,0])+"-"+str(10)+"-"+str(years2[i])
                if j == 21:
                    nov = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    nov.columns=[station]
                    nov.insert(0,"Date",date)
                    nov=nov.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        nov.iloc[f,0]=str(nov.iloc[f,0])+"-"+str(11)+"-"+str(years2[i])
                if j == 24:
                    dec = pd.DataFrame(years2_df[i].iloc[1:32,j])
                    dec.columns=[station]
                    dec.insert(0,"Date",date)
                    dec=dec.reset_index(drop=True)
                    for f,row in jan.iterrows():
                        dec.iloc[f,0]=str(dec.iloc[f,0])+"-"+str(12)+"-"+str(years2[i])
            alldataname = (jan,feb,mar,apr,may,jun,jul,aug,sep,okt,nov,dec)
            alldata = pd.concat(alldataname)
            b = (excel,alldata)
            excel = pd.concat(b)
            #excel = str(station)+"_"+str(years2[i])+".xlsx"
            #alldata.to_excel(str(excel),index=False)

    excel["Date"] = pd.to_datetime(excel["Date"],dayfirst=True,infer_datetime_format=True,errors="coerce",exact=False)
    excel.to_excel(str(station)+".xlsx",index=False)
    





# -*- coding: utf-8 -*-
"""
@author: pauls
"""
import openpyxl 
import pandas as pd
import numpy as np

#ET

ET_xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/ET_comparison/ET_WEAPvsGLEAM.xlsx"
ET_all = pd.read_excel(ET_xlsx,sheet_name="WEAP Export",engine="openpyxl")
ET_all = ET_all.iloc[2:,:]
ET_all = ET_all.T.reset_index(drop=True)

Gleam = pd.DataFrame(index=range(2080),columns=range(14))

Gleam_years = pd.DataFrame(index=range(1),columns=range(14))
Weap = pd.DataFrame(index=range(2080),columns=range(14))
Weap_years = pd.DataFrame(index=range(1),columns=range(14))
Gleam_and_Weap_ET = pd.DataFrame(index=range(3),columns=range(14))

for j in range(len(ET_all.columns)):
    if j == 0:
        Dates = ET_all.iloc[1:,j].reset_index(drop=True)
    elif j < 15:
        Gleam.iloc[:,j-1]=ET_all.iloc[1:,[j]].reset_index(drop=True)
        Gleam_and_Weap_ET.iloc[0,j-1] = sum(Gleam.iloc[:,j-1])/40
    else :
        Weap.iloc[:,j-15]=ET_all.iloc[1:,[j]].reset_index(drop=True)
        Gleam_and_Weap_ET.iloc[1,j-15] = sum(Weap.iloc[:,j-15])/40

for i in range(len(Gleam_and_Weap_ET.columns)):
    Gleam_and_Weap_ET.iloc[2,i] = Gleam_and_Weap_ET.iloc[1,i]/Gleam_and_Weap_ET.iloc[0,i] 
        
colnames = ["ET_A01","ET_A02","ET_A03","ET_A04","ET_A05","ET_A06","ET_A07","ET_A08","ET_A09","ET_A10","ET_A11","ET_A12","ET_A13","ET_A14"]
indexnames = ["Gleam","Weap","Betha"]

Gleam_and_Weap_ET.columns=colnames
Gleam_and_Weap_ET.index=indexnames

#PET

PET_xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/ET_comparison/PET_WEAPvsGLEAM.xlsx"
PET_all = pd.read_excel(PET_xlsx,sheet_name="WEAP Export",engine="openpyxl")
PET_all = PET_all.iloc[2:,:]
PET_all = PET_all.T.reset_index(drop=True)

Gleam_PET = pd.DataFrame(index=range(2080),columns=range(14))
Gleam_PET_years = pd.DataFrame(index=range(1),columns=range(14))
Weap_PET = pd.DataFrame(index=range(2080),columns=range(14))
Weap_PET_years = pd.DataFrame(index=range(1),columns=range(14))
Gleam_and_Weap_PET = pd.DataFrame(index=range(3),columns=range(14))

for j in range(len(PET_all.columns)):
    if j == 0:
        Dates_2 = ET_all.iloc[1:,j].reset_index(drop=True)
    elif j < 15:
        Gleam_PET.iloc[:,j-1]=PET_all.iloc[1:,[j]].reset_index(drop=True)
        Gleam_and_Weap_PET.iloc[0,j-1] = sum(Gleam_PET.iloc[:,j-1])/40
    else :
        Weap_PET.iloc[:,j-15]=PET_all.iloc[1:,[j]].reset_index(drop=True)
        Gleam_and_Weap_PET.iloc[1,j-15] = sum(Weap_PET.iloc[:,j-15])/40

for i in range(len(Gleam_and_Weap_PET.columns)):
    Gleam_and_Weap_PET.iloc[2,i] = Gleam_and_Weap_PET.iloc[1,i]/Gleam_and_Weap_PET.iloc[0,i] 
        
colnames_PET = ["PET_A01","PET_A02","PET_A03","PET_A04","PET_A05","PET_A06","PET_A07","PET_A08","PET_A09","PET_A10","PET_A11","PET_A12","PET_A13","PET_A14"]

Gleam_and_Weap_PET.columns=colnames_PET
Gleam_and_Weap_PET.index=indexnames



#ET = ET.iloc[2:,:]
#ET = ET.T.reset_index(drop=True)
#names = ET.iloc[0,:]

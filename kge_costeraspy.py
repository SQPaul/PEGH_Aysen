# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:01:23 2022

@author: pauls
"""

import openpyxl
import pandas as pd
import numpy as np
import hydroeval as he

obs_xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Calibracion/Costeras/caudales_obs.xlsx"
obs_all = pd.read_excel(obs_xlsx,sheet_name="WEAP Export",engine="openpyxl")
obs = obs_all.iloc[3:,1:]
obs = obs.T.reset_index(drop=True)
names = obs_all.iloc[3:,0]

sim_xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Calibracion/Costeras/caudales_sim.xlsx"
sim_all = pd.read_excel(sim_xlsx,sheet_name="WEAP Export",engine="openpyxl")
sim = sim_all.iloc[3:,1:-1]
sim = sim.T.reset_index(drop=True)

kge = pd.DataFrame()

for (j,col) in enumerate(obs):
    obs_var = pd.to_numeric(obs.iloc[:,j],downcast="float")
    sim_var = pd.to_numeric(sim.iloc[:,j],downcast="float")
    kge[j] = pd.DataFrame(he.evaluator(he.kgeprime, sim_var, obs_var),index=["KGE","r","γ","β"])
    print(j)
    
kge.columns = names
  
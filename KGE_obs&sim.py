# -*- coding: utf-8 -*-
"""
@author: pauls
"""

import openpyxl
import pandas as pd
import numpy as np
import hydroeval as he

obs_xlsx =  "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Calibracion/Obs.xlsx"
obs = pd.read_excel(obs_xlsx,sheet_name="WEAP Export",engine="openpyxl")
date = obs.iloc[[2],1:-1]
date = date.T.reset_index(drop=True)
obs = obs.iloc[3:16,:-1]
obs = obs.T.reset_index(drop=True)
names = obs.iloc[[0],:]

sim_xlsx = "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Calibracion/Sim.xlsx"
sim = pd.read_excel(sim_xlsx,sheet_name="WEAP Export",engine="openpyxl")
date_sim = sim.iloc[[2],1:-1]
date_sim = date_sim.T.reset_index(drop=True)
sim = sim.iloc[3:16,:-1]
sim = sim.T.reset_index(drop=True)
names_sim = sim.iloc[[0],:]

stations = ["Rio Aysen en puerto aysen","Rio Blanco antes junta rio aysen","Rio Blancho chico antes junta oscuro","Rio Blanco antes junta huemules","Rio claro en pisicultura","Rio Coyhaique en tejas verdes","Rio Emperador guillermo antes junta manihuales","Rio blanco en desague lago caro","Rio manihuales antes junta rio simpson","Rio nirehuao en villa manihuales","Rio oscuro en camino cerro portezuelo","Rio huemules frente cerro galera","Rio simpson bajo junta coyhaique"]
kge = pd.DataFrame()
#nse = pd.DataFrame()

for (j,col) in enumerate(obs):
    var_obs = obs.iloc[1:,j]
    var_sim = sim.iloc[1:,j]
    for i in range(len(var_obs)):
        if var_obs.iloc[i] == 0:
            var_obs.iloc[i] = np.nan
        if var_sim.iloc[i] == 0:
            var_sim.iloc[i] = np.nan
        var_obs = pd.to_numeric(var_obs,downcast="float")
        var_sim = pd.to_numeric(var_sim,downcast="float")
        kge[j] = pd.DataFrame(he.evaluator(he.kgeprime, var_sim, var_obs),index=["KGE","r","γ","β"])
        print(j)

kge.columns=stations

#for (j,col) in enumerate(obs):
 #   var_obs = obs.iloc[1:,j]
  #  var_sim = sim.iloc[1:,j]
   # for i in range(len(var_obs)):
    #    if var_obs.iloc[i] == 0:
     #       var_obs.iloc[i] = np.nan
      #  if var_sim.iloc[i] == 0:
       #     var_sim.iloc[i] = np.nan
        #var_obs = pd.to_numeric(var_obs,downcast="float")
        #var_sim = pd.to_numeric(var_sim,downcast="float")
        #nse[j] = pd.DataFrame(he.evaluator(he.nse, var_sim, var_obs),index=["NSE"])
        #print(j)
        
#nse.columns=stations
#--------------------------------------------------------------------------------------

#globals()[names.iloc[0,j]] = pd.DataFrame(he.evaluator(he.kgeprime, var_sim, var_obs),index=["KGE","r","γ","β"])
# -*- coding: utf-8 -*-
"""

@author: pauls

"""

import openpyxl
import pandas as pd
import hydroeval as he
import datetime
import statistics as sta
import numpy as np

xlsx =  "C:/Users/pauls/Desktop/Proyectos/PEGH_Aysen/Codes/Libro1.xlsx"
results = pd.read_excel(xlsx,sheet_name="3",engine="openpyxl")
obs = results.iloc[:,[1]]
sim = results.iloc[:,[0]]
kge = pd.DataFrame(he.evaluator(he.kgeprime, sim, obs),index=["KGE","r","γ","β"])

mean_sim = sim["sim"].mean()
mean_obs = obs["obs"].mean()
betha = mean_sim/mean_obs
r = sim["sim"].corr(obs["obs"])
std_sim = sim["sim"].std()
std_obs = obs["obs"].std()
x = [1,np.nan,2]

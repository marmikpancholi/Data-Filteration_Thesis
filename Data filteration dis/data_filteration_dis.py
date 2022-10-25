# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:12:42 2022

@author: Marmik Pancholi, Oli Systems GmbH
"""

import pandas as pd
# from pyomo.environ import ConstraintList, NonNegativeReals, Reals, Var,NegativeReals, Binary, Objective, maximize, minimize, ConcreteModel, value
# from pyomo.opt import SolverFactory
# import matplotlib.pyplot as plt
# from itertools import cycle

#deleting all the negative values as they are unrealistic
df = pd.read_excel('unfiltered_div_dataset.xlsx')
df = df[(df > 0).all(axis=1)]

# #deleting connection time before 07:00
# indexNames = df[df['t_start'] <= 7].index
# df.drop(indexNames, inplace=True)

# #deleting connection time after 15:00
# indexNames1 = df[df['t_start'] >= 15].index
# df.drop(indexNames1, inplace=True)

# #deleting disconnection time after 22:00
# indexNames2 = df[df['t_end'] >= 22].index
# df.drop(indexNames2, inplace=True)

# #deleting disconnection time before 08:00
# indexNames6 = df[df['t_end'] <= 8].index
# df.drop(indexNames6, inplace=True)

#deleting rows with duration of more than 12 hours
indexNames3 = df[df['duration'] >= 12].index
df.drop(indexNames3, inplace=True)

#deleting rows with SOC of more than 99%
indexNames4 = df[df['SOC'] >= 99].index
df.drop(indexNames4, inplace=True)

#deleting rows with SOC of less than 20%
indexNames5 = df[df['SOC'] <= 30].index
df.drop(indexNames5, inplace=True)

cars = [1,2,3,4,5,6,7,8,9,10]

df['EV'] = pd.np.tile(cars, len(df) // len(cars)).tolist() + cars[:len(df)%len(cars)]
df['Avai_SOC'] = df['SOC'] - 30
df['Energy (kWh)'] = df['Avai_SOC']*0.5
df['Status'] = 'Discharging'
# df = df.sort_values(by='t_start', ascending = True)

#convert data to 
df.to_excel(r'C:\Masters Thesis\Codes2\Data filteration dis\filtered_dummy_dataset_dis_31-12-2017.xlsx', index = False)
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 09:13:12 2022

@author: Marmik Pancholi, Oli Systems GmbH
"""

import pandas as pd
from pyomo.environ import ConstraintList, NonNegativeReals, Reals, Var,NegativeReals, Binary, Objective, maximize, minimize, ConcreteModel, value
from pyomo.opt import SolverFactory
import matplotlib.pyplot as plt
from itertools import cycle

#importing the data to a dataframe
df = pd.read_excel('dummy_dataset_ch_31-12-2017.xlsx')

#counts the max occourences for CPID values
a = df['CPID'].value_counts()

#Filters the 10 most occouring CPID values
b = a[0:10]

#creating an empty dataframe
f = []

#just extract the rows with these CPIDs
for i in range(0,10):
    d = df.loc[df['CPID'] == b.index[i]]
    f.append(d)

#merge this whole set of df in a df
result = pd.concat(f)

#Arrange in ascending order
result = result.sort_values(by='StartDate', ascending = True)

#Save to excel file
result.to_excel(r'C:\Masters Thesis\Codes2\Data filteration ch\filtered_dataset_ch_31-12-2017.xlsx', index = False)
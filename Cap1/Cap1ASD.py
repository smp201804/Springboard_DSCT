# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 19:09:35 2019

@author: SMP
"""

import pandas as pd
import re

tdlrasd = pd.read_csv('Toddler_Autism_dataset_July_2018.csv', index_col=None)

print(tdlrasd.head())

tdlrasd.columns = tdlrasd.columns.str.replace(' ', '_')
tdlrasd.columns = tdlrasd.columns.str.replace(r"_$", "")

print(tdlrasd.columns)

print(tdlrasd.head())



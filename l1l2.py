import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('Melbourne_housing_FULL.csv')
print(df.nunique())


print(df.columns)
cols_to_use = ['Suburb','Rooms', 'Type', 'Price','Method', 'SellerG',
        'Distance', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'CouncilArea',
        'Regionname', 'Propertycount']

df = df[cols_to_use]
print(df.head())
print(df.shape)
print(df.isna().sum())


cols_to_fill_zero = ['Propertycount', 'Distance', 'Bedroom2', 'Bathroom', 'Car']

df[cols_to_fill_zero] = df[cols_to_fill_zero].fillna(0)
print()
print(df.isna().sum())

# fill others with the mean value
df['Landsize'] = df['Landsize'].fillna(df.Landsize.mean())

df['BuildingArea'] = df['BuildingArea'].fillna(df.BuildingArea.mean())


df.dropna(inplace= True)
print()
print(df.isna().sum())

df = pd.get_dummies(df, drop_first=True)
print(df.head())
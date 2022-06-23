import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model


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

print(df.Price)

x = df.drop('Price', axis =1)
y = df['Price']

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.3, random_state=2)
reg = LinearRegression().fit(x_train, y_train)

print("Test Score: ", reg.score(x_test, y_test))
print("Train Score: ", reg.score(x_train, y_train))

lasso_reg = linear_model.Lasso(alpha= 50, max_iter=100, tol =0.1)
lasso_reg.fit(x_train, y_train)

print("Lasso Test Score: ", lasso_reg.score(x_test, y_test))
print("Lasso Train Score: ", lasso_reg.score(x_train, y_train))

ridge_reg = linear_model.Ridge(alpha= 50, max_iter=100, tol =0.1)
ridge_reg.fit(x_train, y_train)

print("\n")

print("Ridge Test Score: ", ridge_reg.score(x_test, y_test))
print("Ridge Train Score: ", ridge_reg.score(x_train, y_train))
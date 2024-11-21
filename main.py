#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas 
import pandas as pd
#importing numpy
import numpy as np
#reading csv
df=pd.read_csv("Weather Dataset (1).csv")
print(df.info())
#checking for null values
df.isnull().any()
#finding the mean temprature
meantemp=np.mean(df['Temperature (C)'])
print("the mean temprature is ", meantemp)
#
vartemp=np.var(df['Temperature (C)'])
print("the varient  temprature is ", vartemp)
#
sd=np.std(df['Temperature (C)'])
print("the standard of deviation in temprature is ", sd)

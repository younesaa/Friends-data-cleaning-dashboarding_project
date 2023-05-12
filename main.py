import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#data path
data = "C:\Users\YLAKHNIC\Desktop\containers\stackProjects\python_project\\friends.txt"
# import our data to panda dataframe 
df = pd.read_csv(data)
print(df)
# dimensions of our dataframe
print(df.shape)
# top 5 of our data columns
print(df.head())
# bottom 5 of our data columns
print(df.tail())
# informations about data
print(df.info())
# columns details
print(df.dtypes)
#convect xx to Nan on wheight and height
df["height(cm)"] = pd.to_numeric(df["height(cm)"], errors='coerce')
df["weight(kg)"] = pd.to_numeric(df["weight(kg)"] , errors="coerce")
df["spend_C"] = pd.to_numeric(df["spend_C"], errors='coerce')
#display changes
print(df)
print(df.dtypes)
# dataframe description & columns tuple
print(df.describe())
print(df.columns)
# show data on barplot
df["age"].plot("bar")
plt.show()
# show data on histogram
df["height(cm)"].plot("hist")
plt.show()
df['weight(kg)'].plot('hist')
plt.show()
# split age_sex columns
df[["age","sex"]]=df.age_sex.str.split('_' , expand=True)
df.drop(["age_sex"],axis=1,inplace=True)
df = df[['fname','lname','age','sex','section','height(cm)','weight(kg)','spend_A','spend_B','spend_C']]
df['weight(kg)'].replace(-60, 60, inplace=True)
df['spend_B'].replace(-100,100, inplace=True)
df['height(cm)'].replace(0.0, df['height(cm)'].mean(), inplace=True)
df['weight(kg)'].replace(160.0, 60.0, inplace=True)
print(df.isnull().sum())
print(df)

mean_height = df['height(cm)'].mean()
df['height(cm)'].fillna(mean_height, inplace=True)
mean_height = df['weight(kg)'].mean()
df['weight(kg)'].fillna(mean_height, inplace=True)
mean_height = df['spend_A'].mean()
df['spend_A'].fillna(mean_height, inplace=True)
mean_height = df['spend_B'].mean()
df['spend_B'].fillna(mean_height, inplace=True)
mean_height = df['spend_C'].mean()
df['spend_C'].fillna(mean_height, inplace=True)
print(df.isnull().sum())
print(df)

assert pd.notnull(df).all().all()
assert (df >=0).all().all()

df_tidy = pd.melt(frame=df, id_vars=['fname','lname','age','sex','section','height(cm)','weight(kg)'],value_vars=['spend_A','spend_B','spend_C'], var_name='expenditure', value_name='amount')

print(df_tidy.describe())
print(df_tidy.columns)
print(df_tidy.dtypes)
print(df_tidy)
df_tidy["age"] = pd.to_numeric(df_tidy["age"], errors='coerce')
df_tidy['age'].plot("bar")
plt.show()
# show data on histogram
df_tidy['height(cm)'].plot("hist")
plt.show()
df_tidy['weight(kg)'].plot('hist')
plt.show()


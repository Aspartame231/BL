import pandas as pd
import numpy as np
import datetime
df=pd.read_csv('Main.csv')

x=df['Email']
for row in x:
    y=row.split('.')
    print('First Name-',y[0])
    z=y[1].split('@')
    print('Last Name-',z[0])
    print('\n')
df1=pd.read_csv('Book1.csv')

df = df.merge(df1,on='Email',how="left")


df['City_y'].fillna("London",inplace=True)
print(df['City_y'])

df['Hire date'].fillna("1-05-2020",inplace=True)
print(df['Hire date'])

df['Hire date'] = pd.to_datetime(df['Hire date'])
for index,row in df.iterrows():

    c = row['Hire date'].year
    if c<= 2018:
        print("Experienced")
    else:
        print("No Experience")



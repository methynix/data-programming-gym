import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

data=pd.read_csv("data/school.csv")
df=pd.DataFrame(data)

print("The first 10 rows")
print(df.head(10))

print("The info of the rows")
print(df.info)

print("The description")
print(df.describe())

#checking for missing values and duplicate rows
print(f"Total missing values {df.isnull().sum()}")
print(f"Total duplicate values {df.duplicated().sum()}")

#the variable likely to influence the final_score is attendance(by just looking, not yet calculated)
#but anyways, let us drop the duplicates and replace null values with something suitable

#before, i can maybe check the variance so that i can know what replacer to use

df["attendance"]=df["attendance"].fillna(df["attendance"].mean())
df["sleep_hours"]=df["sleep_hours"].fillna(df["sleep_hours"].mean())
df["assignments_completed"]=df["assignments_completed"].fillna(df["assignments_completed"].mean())

df.drop_duplicates()
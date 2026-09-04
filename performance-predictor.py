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
print(f"Total missing values {df.isnull.sum()}")
print(f"Total duplicate values {df.duplicated.sum()}")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
df = pd.read_csv("uber_cleaned_final.csv", encoding='ISO-8859-1') 
print(df.head())             # First 5 rows
print(df.shape)              # Rows and columns
print(df.columns)            # Column names
print(df.info())             # Data types and non-null counts
print(df.describe())         # Summary stats
print(df.isnull().sum())     # Null value count


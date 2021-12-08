
import pandas as pd
import numpy as np

# To be able to see all rows
pd.set_option("display.max_rows", None)

# Read document
df = pd.read_csv("df.csv", encoding = "utf-8-sig")

# See columns
df_column_list = df.columns
print(df_column_list)

# See all data
print(df)

# Sort data by "Sıklık" and "Somut_Ortalama" columns
df_sorted = df.sort_values(by=["Sıklık", "Somut_Ortalama"], ascending = False)
#print(df_sorted)

# Calculate the average of "Somut_Ortalama"
df_ortalama_somut = sum(df["Somut_Ortalama"])/len(df["Somut_Ortalama"])
print(df_ortalama_somut) #4.90204

# Create new column, labeling words "Somut" or "Soyut based on the average of "Somut_Ortalama" - NOT WORKING THAT WAY
#df_sorted["Somut"] = np.where(df["Somut_Ortalama"] > df_ortalama_somut, 1, 0)
#print(df_sorted)

# Create new DataFrame to write the words in it if they are Somut => Tried cut-off points to get the number of Somut words mentioned in the book
#df_sorted_new = pd.DataFrame()
#df_sorted_new["Somut_Kelimeler"] = np.where(df["Somut_Ortalama"] > 5.33, df["Kelime"], None)
#df_sorted_new["Somut_Degerleme"] = np.where(df["Somut_Ortalama"] > 5.33, df["Somut_Ortalama"], None)
#print(df_sorted_new)

# Count Somut words in the new DataFrame
#count = 0
#for _, w in enumerate(df_sorted_new["Somut_Kelimeler"]):
#    if w != None:
#        count = count + 1

#print(count)
#percentage = count / len(df["Kelime"]) * 100
#print("percentage: % ", percentage)

# Weighted average of the whole data
#sums = sum(df["Somut_Ortalama"]*df["Sıklık"])
#print("ağırlıklı ortalama: ", sums/sum(df["Sıklık"])) # 4.907

#weighted_list = df["Somut_Ortalama"]*df["Sıklık"] / sum(df["Sıklık"])
#print(weighted_list)

import tabula
import pandas as pd

options = {"dtype" : "object"}

dfs = []
for n in range(13):
    dfs.append(tabula.read_pdf("tr_words.pdf", pages = n + 12, pandas_options = options, multiple_tables = True))

for i, d in enumerate(dfs):
    if i == 0:
        df = pd.DataFrame(d[0])
        df = df.set_axis(["Kelime", "Imgelem_Ortalama", "Imgelem_SS", "Somutluk_Ortalama", "Somutluk_SS", "Sıklık"], axis = 1)
    else:
        df = pd.DataFrame(d[0])
    df.to_csv("Turkish_Word_List.csv", mode = "a", encoding = "utf-8-sig", index = False)
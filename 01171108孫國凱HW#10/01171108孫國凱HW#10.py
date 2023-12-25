#HomeWork#10 from  01171108孫國凱HW#10.py

import pandas as pd
import os

os.system("cls")

df1=pd.read_excel("score1.xlsx")
df2=pd.read_excel("score2.xlsx")
df3=pd.read_excel("score3.xlsx")

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) # 設置寬度

original = pd.concat([df1,df2,df3], ignore_index=True)

part1=original.fillna(0)
#print(part1)
part1.to_excel("fillna.xlsx")

part2=original.dropna()
#print(part2)
part2.to_excel("dropna.xlsx")
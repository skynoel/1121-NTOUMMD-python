#HomeWork#5 from  01171108孫國凱HW#5.py

import pandas as pd
import os

os.system("cls")

df=pd.read_excel("樞紐分析表.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) 

df1=df.sort_values(["金額"], ascending=False)
print(df1.head(3))
print("================")
print(df1.tail(3))
print("================")
print(df["業務員"].value_counts())
print("================")
print(df["產品"].value_counts())
print("================")
df2=df[["業務員", "產品"]]#看不懂題意
print(df2)
df3=df[df["產品"].str.contains("柚子")]
df4=df3[df3["商店"].str.contains("三華超商")]
df4=df4.set_index("訂單號碼")
df4.to_excel("三華超商-柚子.xlsx")
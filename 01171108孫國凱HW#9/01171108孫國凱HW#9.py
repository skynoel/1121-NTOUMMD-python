#HomeWork#9 from  01171108孫國凱HW#9.py

import numpy as np
import pandas as pd
import os

os.system("cls")

df=pd.read_excel("樞紐分析表.xlsx")
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 180) 

print(df.pivot_table(index=["業務員","產品"],values=["商店","金額"],aggfunc={"商店":np.size,"金額":"sum"}))
print("==================================================")
print(pd.pivot_table(df,index=["業務員"],columns=["產品"],values="金額",aggfunc="sum",fill_value=0,margins=True))
print("==================================================")
print(pd.pivot_table(df,index=["業務員"],columns=["產品"],values=["商店","金額"],aggfunc={"商店":np.size,"金額":"sum"},fill_value=0,margins=True))
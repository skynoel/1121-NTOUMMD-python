#HomeWork#7 from  01171108孫國凱HW#7.py

import pandas
import os

os.system("cls")
#part1
data1=pandas.DataFrame({
    "name":["Amy","Bob","John","Charles"],
    "salary":[30000,50000,70000,40000]
}, index=["a","b","c","d"])
print(data1)
print("================")
print("資料數量:",data1.size)
print("資料型態 (列,欄):",data1.shape)
print("資料索引:",data1.index)
#part2
print("================")
data1["name"]=data1["name"].str.upper()
data1["revenue"]=[500000,400000,700000,300000]
data1["rank"]=pandas.Series([1,2,6,3],index=["a","b","c","d"])
data1["cp"]=data1["revenue"]/data1["salary"]
print(data1)
#part3
print("================")
print(data1[data1["salary"]>=40000])
#part4
print("================")
print(data1[data1["name"].str.contains("H")])
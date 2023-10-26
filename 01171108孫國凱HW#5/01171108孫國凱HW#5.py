#HomeWork#5 from  01171108孫國凱HW#5.py

import random,statistics

#part1
with open("chardata.txt", mode="r+",encoding="utf-8") as char1:
    x=char1.read()
    print("檔案內容為：",x)
#part2
numdata=list()
with open("numdata.txt", mode="r+",encoding="utf-8") as num1:
    for i in num1:
        numdata.append(int(i))
    print("該串數列為:",numdata)
    random.shuffle(numdata)
    print("隨機調換順序後：",numdata)
    print("數列 =",numdata)
    print("中位數 median =",statistics.median(numdata))
    print("平均數 mean =",statistics.mean(numdata))
    print("標準差 stdev =",statistics.stdev(numdata))
    

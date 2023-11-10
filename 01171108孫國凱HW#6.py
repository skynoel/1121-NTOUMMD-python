#HomeWork#6 from  01171108孫國凱HW#6.py
import pandas

#part1
s1 = pandas.Series([18,16,20,25,19],index=["A", "B", "C", "D", "E"])
print("最大值: ",s1.max())
print("總和: ",s1.sum())
print("加成值: ",s1.prod())
print("標準差: ",s1.std()) 
print("中位數: ",s1.median())
print("平均數: ",s1.mean())
print("最小(2)位數:\n",s1.nsmallest(2))

#part2

s1 = pandas.Series(["您好", "Python", "Pandas"])
print("串接字串: ",s1.str.cat(sep="-"))
print("==全變大寫:::")
print(s1.str.upper())
print("==計算字串長度:::")
print(s1.str.len())
print('==置換字串:::  ("您好" 改為 "Hello")')
print(s1.str.replace("您好" ,"Hello"))
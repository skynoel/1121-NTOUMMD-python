#　HomeWork#2 from  01171108孫國凱HW#2.py

import calendar
from calendar import weekday

# part1
str = "strHello Python HomeWork#2 from 0010100姓名"
print(str)
i=1
while(i==1):
    inp = input("請輸入一個字元：")
    if(inp=="?"):
        print('"!!! 結束while迴圈 !!!"')
        i=0
        break
    else:
        if(inp in str):
            print('"該字元:\'',inp,'\'在該句子中"')
        else:
            print('"該字元:\'',inp,'\'不在該句子中"')

# part2
year=int(input("請輸入年份："))
month=int(input("請輸入月份："))
while(month >=13 or month<=0):
    print("錯誤！")
    month=int(input("請輸入月份："))
if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
   date=int(input("請輸入日期：")) 
   while(date>=32 or date<=0):
       print("錯誤！")
       date=int(input("請輸入日期："))
else:
    date=int(input("請輸入日期：")) 
    while(date>=31 or date<=0):
       print("錯誤！")
       date=int(input("請輸入日期："))
day=int(input("請輸入星期(1~7)"))
while(day>=8 or day<=0):
    print("錯誤！")
    day=int(input("請輸入星期(1~7)"))
DtoE={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
print("今天是", year,"年",month,"月",date,"日",DtoE[day])
realday=int(weekday(year, month, date))
print("但其實", year,"年",month,"月",date,"日","是",DtoE[realday+1])
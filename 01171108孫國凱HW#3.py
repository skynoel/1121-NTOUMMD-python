#HomeWork#3 from  01171108孫國凱HW#3.py
# part1
import time

def add(n1,n2):
    return n1+n2
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def remainder(x,y):
    return x%y
def getint(x,y):
    return x//y
def square(x):
    return x*x

type=int(input("請輸入你想做的運算:1=加,2=減,3=乘,4=除,5=取餘數,6=取整數,7=次方,0=退出："))
while(type!=0):
    number1=float(input("請輸入第一個數："))
    if type!=7:
        number2=float(input("請輸入第二個數："))
    if type==1:
        print("答案是：",add(number1,number2))
    elif type==2:
        print("答案是：",minus(number1,number2))
    elif type==3:
        print("答案是：",multiply(number1,number2))
    elif type==4:
        print("答案是：",divide(number1,number2))
    elif type==5:
        print("答案是：",remainder(number1,number2))
    elif type==6:
        print("答案是：",getint(number1,number2))
    elif type==7:
        print("答案是：",square(number1))
    else:
        print("在幹嘛，不要亂打")
    type=int(input("請輸入你想做的運算:1=加,2=減,3=乘,4=除,5=取餘數,6=取整數,7=次方,0=退出"))
if type==0:
    print("成功退出")
#part 2
time.sleep(1)
print("進入第二部分")
print("輸出乘法表")
time.sleep(1)
for i in range(1, 10):
    for j in range(1, 10):
        print("%d * %d = %2s" % (i, j, i*j),end="  ")        
    print("\n")







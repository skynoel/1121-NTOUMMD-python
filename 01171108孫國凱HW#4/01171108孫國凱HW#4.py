#HomeWork#4 from  01171108孫國凱HW#4.py
import geometry.point  
result = geometry.point.distance(3,4)
print("(3,4)與原點的距離=", result)

import geometry.line
result=geometry.line.slope(1,1,5,5)
print("(1,1),(5,5)兩點之斜率=", result)
result=geometry.line.lengthOfPoints(1,1,5,5)
print("(1,1),(5,5)兩點之距離=", result)

import geometry.circle
r = (int(input("請輸入一圓之半徑:")))
result=geometry.circle.areaOfCircle(r)
print("半徑", r, "之圓面積=", result)
result=geometry.circle.circumference(r)
print("半徑", r, "之圓周=", result)
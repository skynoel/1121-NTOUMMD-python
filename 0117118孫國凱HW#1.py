#　HomeWork#1 from  01171108孫國凱HW#1.py

# part1
List = [12, 60, 15, 70, 90]
print(List,"長度為:",len(List))
List.remove(15)
List.remove(70)
print(List)
List.append(12)
List.append(33)
print(List)
List.insert(List.index(60),5)
List[List.index(60)]=5
List[List.index(90)]=5
print(List,"長度為:",len(List))

#part2
Turple=(3, 4, 5)
print(Turple,"長度為:",len(Turple))
Turple=Turple + (6,7)
print(Turple,"長度為:",len(Turple))

#part3
s1={1,2,3,4,5}
s2={4,5,6,7,8}
Union=s1|s2
Intersection=s1&s2
print("交集:",Intersection,"聯集:",Union)
s3={"NTOU","MMD"}
s3.remove("MMD")
print(s3)

#part4
字典={"NTOU":"國立臺灣海洋大學 ", "MMD":"商船學系", "CSE":"資工系"}
print(字典["NTOU"],字典["MMD"])
dict={x:x ** 2 for x in range(2,10)}
print(dict)
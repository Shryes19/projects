# Q.9
#
# is_on = True
# while is_on:
#     num = input("Enter: ")
#     if num == 'stop':
#         is_on=False
#         print(type(num))
#     else:
#         num = int(num)
#         if num%2 == 0:
#             print("even",type(num))
#         else:
#             print("odd")

# ********************************************************************************* #

# Q.16
# for i in range(100,1000):
#  i = str(i)
#  t = i[::-1]
#  print("palindrome" if t == i else "No")

#************************************************************************************#

# Q.18
# n = 145
# n = str(n)
# s=0
#
# for i in range(len(n)):
#      i = int(n[i])
#      m = 1
#      for j in range(1,i+1):
#          m= m * j
#      s = s + m
# if s == int(n):
#      print("Strong number")
# else:
#     print("Not a strong number")

#**************************************************************************************************#

# Q.24
# n=4
# for i in range(1,n+1):
#     k = 97
#     for j in range(i):
#
#         print(chr(k),end="")
#         k+=1
#     print()

#*********************************************************************************************************#

# n=4
# x=0
# for i in range(0,n):
#     s=""
#     for j in range(n):
#         if j == x:
#             s += "1"
#         else:
#             # print("0",end="")
#             s+="0"
#     x += 1
#     print(s)
# print('\n\n')
#
# k=1
# for i in range(1,5):
#     for j in range(4):
#         print(f"{k} ",end="")
#         k += 1
#     print()

#*********************************************************************************************************#

# s = "You are my world"
# s += " "
# print(s)
# st = ""
# c=0
#
# for _ in s:
#     if _ != " ":
#         c+=1
#     else:
#         st += str(c)
#         c=0
# print(st[0:1],".",st[1:],sep="")

#*********************************************************************************************************#

# def even(a):
#     for i in range(10):
#         print(f" {a}",end="")
#         a-=1
#
# def odd(a):
#     k=a
#     for i in range(10):
#         if k==1:
#             print(f" {a} ", end="")
#         else:
#             print(f" {a}",end="")
#         a+=1
#
#
# a=100
# b=81
# for i in range(5):
#     even(a)
#     print()
#     odd(b)
#     print()
#     a-=20
#     b-=20

#*************************************************************************************************************#

# n=10
# k=1
# c=1
#
# for i in range(1,n+1):
#    print(k,"  ",end="")
#    k+=c
#    c,k=k,c
# print("\n\n")
#*************************************************************************************************************#

# n=8
# for i in range(1,n+1,3):
#     if (n-i)>=2:
#         print(i*(i+1)*(i+2))
#
#     elif (n-i)>=1:
#         print(i* (i + 1))
#     else:
#         print(i)

#***************************************************************************************************************#

# n=int(input("n: "))
# v = n//2
# for i in range(1,n+1):
#     if i == v:
#         continue
#     else:
#         print(i," ",end="")

#**************************************************************************************************************#

class MyDate:
    def __init__(self, d,m,y):
        self.dd = d
        self.mm = m
        self.yy = y
    def __str__(self):
        return str(self.dd)+" "+str(self.mm)+" "+str(self.yy)
    # def getmonth(self):
    #     return self.mm

class Person(MyDate):
    def __init__(self, n, a, d, m, y):
        super().__init__(d, m, y)
        self.name = n
        self.age = a
        self.dob = MyDate(d,m,y) #Person has date of birth
    def __str__(self):
        return self.name+" "+str(self.age)+" "+str(self.dob)
    def get_month(self):
        return self.mm
    #client code

p1 = Person("sindhu", 56, 2, 4, 1999)
p2 = Person("indhu", 53, 2, 8, 1919)
p3 = Person("bindhu", 51, 2, 1, 2000)


p_objects = [p1, p2, p3]
for obj in sorted(p_objects, key = Person.get_month):
        print(obj)


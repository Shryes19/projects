# l = [1,7,4,6,10]
# n_l = []
# for i in range(0,len(l)-1):
#     n_l.append(abs(l[i]-l[i+1]))
# print(sorted(n_l))

#**************************************************************************************#

# l = [1,5,2.5,"Hi",True,7.5,"Hello",False,5,(1,0)]
# l_1 = []
# n_l = []
#
#
# j=0
# while j != len(l):
#     t1 = type(l[j])
#
#     for i in l:
#         if type(i) == t1:
#             l_1.append(i)
#     #print(n_l,l_1)
#     if l_1 not in n_l:
#         n_l.append(l_1)
#         print(l_1)
#     l_1 = []
#     j += 1

#***************************************************************************************#

# l = [1,2,3,1,2,5,2,7,1]
# n_l = []
# for i in l:
#     if i not in n_l:
#         n_l.append(i)
# print(n_l)

#***************************************************************************************#

# lst = [1, 5, 1, 3, 7, 4]
# target = 4
# k=0
# for i in lst:
#     k+=1
#     if i > target:
#         print(i)
#         break
#     if k==len(lst):
#         print(None)

#******************************************************************************************#

# n=5
# s=0
# for i in range(1,n+1):
#    s += i*(i+1)
#    if i == n:
#        print(f"{i}*{i + 1} = ",end="")
#    else:
#        print(f"{i}*{i + 1} + ", end="")
# print(s)

#*************************************************************************************************#

# m = [23,45,67]
# n = [12,65,98,23,55]
# l = []
#
# for i in range(len(m)):
#     l.append(m[i])
#     l.append(n[i])
#     if i == len(m)-1:
#         for j in range(i+1,len(n)):
#             l.append(n[j])
# print(l)

#***********************************************************************************************#

# l1 = [11,22,14]
# l2 = [45,77,88]
# l3 = [90,99,55,10]
# l = []
# m_l = []
#
# for i in range(len(l1)):
#     l.append(l1[i]%10)
#     l.append(l2[i]%10)
#     l.append(l3[i]%10)
#     m_l.append(l)
#     l=[]
# print(m_l)

#******************************************************************************************************#
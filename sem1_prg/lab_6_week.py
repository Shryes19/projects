# s1 = {"ram", "sham", "ravi"}
# s2 = {"kumar", "ram"}
# print(f"Students attended both events: {s1.intersection(s2)}")
# print(f"Students attended only one event: {s1.symmetric_difference(s2)}")
# print(f"Students attended both events: {s1.union(s2)}")
# print()
#
# #*******************************************************************************************#
#
# students = {
#     "Rohan":85,
#     "spoorthi":90,
#     "Aditi":78,
#     "Tanya":92
# }
# marks = max(students.values())
# for i in students.items():
#     if i[1] == marks:
#         print(f"Max marks by {i[0]} is {marks}")
#         break
# print(f"Avg marks: {(sum(students.values()))/len(students)}")
#
# v = int(input("Enter student marks: "))
# students[input("Enter student name: ")] = v
# print(students)
# print()
# #*********************************************************************************************#
#
# sentence = "Hello how are you"
# vowel = 'aeiou'
# c=0
# l=[]
#
# for i in sentence.lower():
#     if i in vowel:
#         c+=1
#     else:
#         pass
#
# print(c)
#
# l=sentence.split()
# m = len(l[0])
# s=l[0]
# for i in l:
#     if len(i) > m:
#         m = len(i)
#         s = i
# print(f"Max length of {s} is {m}")
# print(f"Reversed string: {sentence[::-1]}")
# print()
# #************************************************************************************************#

# l = [1,2,5,2,2,5,2,4,4,4,4,4,4,4]
# f_l = []
# d={}
# n_d={}
# t=()
# for i in l:
#     d[l.count(i)] = i
# print(d)
# l=list(d.keys())
# print(sorted(l))
# for i in l:
#     n_d[i]=d[i]
# print(n_d)
#
# for k in n_d:
#     t=(k,n_d[k])
#     f_l.append(t)
# print(f_l)
#
# def get_key(item):
#     return item[1]
#
# sorted_arr = sorted(d.items(), key=get_key, reverse=True)
#
# print(sorted_arr)

# for key,value in sorted_arr:
#     m=''
#     key = str(key)
#     for j in range(value):
#         m+=str(key)
#     f_l.append(m)
# print(f_l)
# print()
# #******************************************************************************************#
#
# d = {
#     "p1" : {"chips":10, "soap":5, "chocolate":2},
#     "p2" : {"bowl":15, "bat":20, "chips":10}
# }
# s = set()
# bill=0
# for i in d:
#     for j in d[i]:
#         if j not in s:
#             s.add(j)
#             bill+=d[i][j]
# print(f"Total cost: {bill}")
# print()
# #******************************************************************************************** #
#
# bookings = []
# while True:
#     i = input("Enter booking in format ""Customer name-MovieName-SeatNumber"" ")
#     if i.lower() == "exit":
#         break
#     else:
#         bookings.append(i)
# s = set(bookings)
# print(s)
# print()
# #*********************************************************************************************#
#
# s1 = "Astronomer"
# s2 = "Moon starer"
# l1={}
# l2={}
# for i in s1.lower():
#     if i != " ":
#         l1[i] = s1.lower().count(i)
# for j in s2.lower():
#     if j != " ":
#         l2[j] = s2.lower().count(j)
# print(l1,"\n",l2)
# print("Anagrams" if l1==l2 else "Not anagrams")
# print()
# #********************************************************************************************#
#
# s = "Hello aam"
# s = s.lower()
# s = list(s)
# l=[]
#
# for i in s:
#     if i!= " ":
#         if s.count(i) == 1:
#             l.append(i)
# print(f"The non-repeating characters: {l}")
#
# #*********************************************************************************************#
b=[1,2,3]
def x(a):
    a[1]=100

x(b)
print(b)
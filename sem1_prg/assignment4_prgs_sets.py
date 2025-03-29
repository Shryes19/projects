# n = 4
# s =set()
# for i in range(2,n+1):
#     s.add(i)
# for i in s:
#     print(i*i)

#*********************************************************************************#

# n = "how much wood would a wood chuck chuck if a wood chuck could chuck wood"
# l = n.split()
# s = set()
# for i in l:
#     s.add(i)
# for i in s:
#     print(i)

#*********************************************************************************#

# m = {1,2,3,4}
# n = {5,6}
# for i in m:
#     for j in n:
#         print(i*j,"  ", end="")


#*********************************************************************************#

# s1 = {"apple", "banana", "orange"}
# s2 = {"jackfruit", "grapes", "mango"}
# print(s1.intersection(s2) if s1.intersection(s2) else "No common elements")

#**********************************************************************************#

# hackathon1 = {"Alice", "Bob", "Charlie", "David"}
# hackathon2 = {"Charlie", "Eve", "Frank", "Alice"}
# print("Students who took part only in the first hackathon:", list(hackathon1.difference(hackathon2)))

#***********************************************************************************#

n = [1,4,5,6,7]
s = 0
l=[]
list1 = []
n_l=[]
for i in range(len(n)):
    list1.append(n[0:i + 1])
    list1.append(n[i:i+1])
    list1.append(n[i:i + 2])
    list1.append(n[i:i + 3])


for j in range(0,len(n)):
    for k in range(j, len(n), 2):
        l.append(n[k])
    l=[]
    list1.append(l)
print(list1)

for i in list1:
    if i not in n_l:
        n_l.append(i)
print(n_l)

# set1 = set(list1)
# print(set1)
# for i in set1:
#     s += int(i)
# print(s)

#***************************************************************************************#

# str1 = input()
# str2 = ""
# def modify(str1):
#     global str2
#     for i in range(0,len(str1)-1,2):
#         str2 = str2+str1[i+1]+str1[i]
#     return str2
# print(modify(str1))

#***********************************************************************************#

# s = "YOU AND PES"
# print(s.replace("YOU","I"))

#***********************************************************************************#

# s1 = "sindhu"
# s2 = "pai"
# s=""
# j=0
# for i in s2:
#    s = s + s1[j] + i
#    j+=1
# print(s)

#***************************************************************************************#

# string1 =  "whatsapp"
# string2 =  "wat"
# for i in string2:
#    string1=string1.replace(i,"")
# print(string1)

#***************************************************************************************#

# s1 = "elegant man"
# s2 = "a gentleman"
# d1={}
# d2={}
# for i in range(len(s2)):
#    d1[s1[i]] = s1.count(s1[i])
#    d2[s2[i]] = s2.count(s2[i])
# # print(d1)
# # print(d2)
# if d1==d2:
#    print("Anagrams")
# else:
#    print("Not anagrams")

#***************************************************************************************#
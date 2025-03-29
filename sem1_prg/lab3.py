# l = []
# n = int(input("Enter n:"))
# for i in range(0,n):
#
#     l.append(int(input("Enter the number: ")))
#
# for i in range(len(l)):
#     print(l[i])
# print("\n\n\n\n")
# #*********************************************************************#
#
# l = [4,7,1,5]
# if (sorted(l) == l):
#     print("List is sorted")
# else:
#     print("Sorted list is: ",sorted(l))
# print("\n\n\n\n")
#
# #*********************************************************************#
#
# w=""
# s = input("Enter the string: ")
# for i in range(len(s)-1,-1,-1):
#     w += s[i]
# print(w)
# print("\n\n\n\n")
#
# #***********************************************************************#
#
# l = [1,2,3,4]
# l_E = []
# l_O = []
# for i in range(len(l)):
#     l_E.append(l[i]) if l[i]%2==0 else l_O.append(l[i])
# print(f"Even list: {l_E}\nOdd list: {l_O}")
# print("\n\n\n\n")

#**********************************************************************#

# l = []
# l2 = []
# c = []
# n = int(input("Enter n:"))
# if n == 0:
#     print("No element in the list")
# elif n == 1:
#     print("Least frequency element is: ", l[0])
# else:
#     for i in range(0, n):
#         l.append(int(input("Enter the number: ")))
#
#     for i in range(len(l)):
#         c.append(l.count(l[i]))
#     a = c.index(min((c)))
#     b = l[a]
#     print(f"Min count of {b} is {min(c)}")
# print("\n\n\n\n")

#***********************************************************************#

l = [("A", "P"), ("B", "A"), ("C", "P"), ("D", "A"), ("E", "P"), ("F", "P"), ("G", "A"), ("H", "P"),
                      ("I", "P"), ("J", "P")]

p_c = 0
a_c = 0


for i in range(len(l)):

    if l[i][1] == "P":
        p_c += 1
    else:
        a_c += 1
print(f"No. of present students: {p_c}\nNo. of absent students: {a_c}")

n = input("Enter the name of student: ")
a = input("Enter the attendance of student: ")

if (n,a) in l:
    pass
else:
    if a == "P":
        b = "A"
        l[l.index((n, b))] = (n, a)

    else:
        b = "P"
        l[l.index((n,b))] = (n,a)

print(l)

n2 = input("Enter the name of new student: ")
a2 = input("Enter the attendance of new student: ")
l.append((n2,a2))
print(l)
print("\n\n\n\n")

#****************************************************************************************#

l1 = ['abc', 'xyz']
l2 = ['mno', 'abc']
l = l1+l2
k = []
print("Merged lists: ",l)

print(set(l)) # l = ["abc","xyz,"mno"]

n = int(input("Enter the value of n: "))
for i in range(n):
    a = l.pop(0)
    l.append(a)
    print(l)

l1=[]
l2=[]

for i in l:
    z = i[0].lower()
    if z == "a" or z == "e" or z == "i" or z == "o" or z == "u":
        l1.append(i)
    else:
        l2.append(i)

print(f"Songs starting with vowel: {l1}\nSongs starting with consonants: {l2}")

import math

x = (int(input("Enter x\n"))*math.pi)/180
n = int(input("Enter n\n"))

i = 1
s = 0
j = 0

while True:

    f = 1
    for r in range(1, i + 1):
        f *= r
    v = float(float(math.pow(x, i)) / f)
    s = s + int(math.pow(-1,j))*v
    i = i + 2
    j = j + 1
    if j == n:
        break

if len(str(s))>3:
    if str(s)[3] == "9":
        l = str(s)[2]
        # str(s)[2] = str(int(l) + 1)
        print(str(s)[0]+str(s)[1]+str(int(l) + 1))

else:
    print(str(s)[0] + str(s)[1] + str(s)[2])



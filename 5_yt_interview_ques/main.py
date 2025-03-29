i = 43
i = str(i)
sum = 0

for c in i:
    sum += int(c)
num = sum

c = 0

for r in range(1,num+1):
    if num % r == 0:
        c += 1

if c == 2:
    print(f"Since {num} is prime number,{i} is a Googly prime number.")
else:
    print(f"Since {num} is not a prime number,{i} is not a Googly prime number.")
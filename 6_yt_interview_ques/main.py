s = "apples"
c1 = s[0]
c2 = ""
new_s = ""

for c in s:
    if c != c1:
        c2 = c
        break

for c in s:
    if c == c1:
        new_s = new_s + c2

    elif c == c2:
        new_s = new_s + c1

    else:
        new_s = new_s + c

print(new_s)

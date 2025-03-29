s = "0122225"
s = s[::-1]
c1 = s[0]
c2 = ""
count = 0

for ch in s:
    if ch != c1:
        c2 = ch
        break

for ch in s:
    if ch == c2:
        count += 1

print(count)

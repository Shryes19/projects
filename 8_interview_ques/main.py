s = "11234"

i=0
j=2
k=1
r = ""
l=[]

for ch in s:
    ch = int(ch)
    print(chr(ch+64),end="")
print()

while len(s) > 2 and j <= len(s):
    ch = s[i:j:1]
    i += 1
    j += 1
    ch = int(ch)
    r += chr(ch+64)
    ch = str(ch)
    v = s.replace(ch, "")

    if int(ch) <= 26 :
        for c in v:
            c = int(c)
            r += chr(c + 64)

        if k > 0 and i > 1:
            print(r)
            z = r[0]
            for c in r:
                l.append(c)
            l[0] = l[k]
            l[k] = z
            print(l)
            r = ""

            for c in l:
                r = r + c
            l=[]
            k+=1



        print(r)
        print()
        r = ""


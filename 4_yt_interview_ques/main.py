s = "10110111011110111110111111"
if s[len(s)-1] != "0":
    s += "0"

c = ""

for ch in s:
    if ch != "0":
        # print(ch, end="")
        c = c + ch

    else:
        l=len(c)
        print(chr(l+64),end="")
        c = ""

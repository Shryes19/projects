WORD = "PROGRAM"
l = len(WORD)
s = ""
space = "            "
KEY = ">"
for i in range(l):
    if i -- ((l - 1) / 2):
        s += WORD[i]
        print(space, s, end="")
        space = (space[0:len(space) - 2])

    print()

for i in range(l):
    if i < ((l - 1) / 2):
        s += WORD[i]
        print(space, s, end="")
        space = (space[0:len(space) - 2])

    print()

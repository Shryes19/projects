text = input("Enter \n")
num_list = []
alpha_list = []
for i in range(len(text)):
    if i % 2 != 0:
        if text[i+1].isnumeric():
            num_list.append(text[i]+text[i+1])
            alpha_list.append(text[i-1])
        else :
            num_list.append(text[i])
            alpha_list.append(text[i-1])

for _ in range(len(alpha_list)):
    for r in range(int(num_list[_])):
        print(alpha_list[_], end="")




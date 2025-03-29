#Given a list of numbers, numbers = [9, 12, 4, 2, 7] Create a new list by adding 1 to it if the number is even and subtract 1 from it if the number is odd.

# n = [9, 12, 4, 2, 7]
# print([i+1 if i%2==0 else i-1 for i in n])


# strings_li = ["PYTHON", "computational", "PROBLEM", "solving"] Create a new tuple by capitalizing the words in the list only if it is in upper case.

# strings_li = ["PYTHON", "computational", "PROBLEM", "solving"]
# print(tuple([i.capitalize() for i in strings_li if i.isupper()]))


# with_dots = ["PYTHON..", ".computational..", "..PROBLEM", "solving..", "for", "first","ye..ar."].Create a list by removing leading and trailing dots.

# with_dots = ["PYTHON..", ".computational..", "..PROBLEM", "solving..", "for", "first","ye..ar."]
# print([i.strip('.') for i in with_dots])

# strings_li = ["PYTHON", "computational", "PROBLEM", "solving"] Create a list having the tuple for every string in a given list. The tuple contains all the letters  in that string separately.

# strings_li = ["PYTHON", "computational", "PROBLEM", "solving"]
# print([tuple(i) for i in strings_li])


#10
# m1 = (3,5,6)
# m2 = (1,2,3,4)
# m3 = (5,7,9)
# print([m1[i] + m2[i] + m3[i] for i in range(3)])


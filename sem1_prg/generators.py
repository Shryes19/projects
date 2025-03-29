# gen = (i**3 for i in range(1,10))
# for i in gen:
#     print(i)




# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
#
# def generate_primes(start, end):
#
#     for num in range(start, end):
#         if is_prime(num):
#             yield num
#
#
# for prime in generate_primes(10, 50):
#     print(prime)



# def running_average():
#
#     total = 0
#     count = 0
#     while True:
#         number = yield
#         if number is None:  # Stop the generator if None is sent
#             break
#         total += number
#         count += 1
#         yield total / count
#
# # Example usage
# gen = running_average()
# next(gen)  # Prime the generator
#
# # Send numbers to the generator
# print(gen.send(10))  # Output: 10.0
# print(gen.send(20))  # Output: 15.0
# print(gen.send(30))  # Output: 20.0
#
# # Stop the generator
# gen.send(None)



# from itertools import combinations
# def generate_combinations(elements):
#
#     n = len(elements)
#     for r in range(1, n + 1):
#         for combo in combinations(elements, r):
#             yield combo
#
# # Example usage
# elements = ['a', 'b', 'c']
# for combo in generate_combinations(elements):
#     print(combo)


# def palindrome(s):
#     s = str(s)
#     if s == s[::-1]:
#         return True
#
# def next_palindrome(s):
#     i=0
#     while True:
#         if palindrome(s+i):
#             yield s+i
#         i+=1
#
# # obj = next_palindrome(155)
# for p in next_palindrome(155):
#     print(p)
#
from tkinter import *
w = Tk("Hi")
w.geometry("300x200")
l=Label(w, text ='Select Your Hobbies:', fg="Blue",bg='black',font = "100")
l.pack()
Checkbutton1 = IntVar() # holds integer data passed to the checkbutton

Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

cb1=Checkbutton(w, text="Painting",variable = Checkbutton1,
onvalue = 1,
offvalue = 0,
height = 2,
width = 10)

cb2=Checkbutton(w, text = "Dancing", variable = Checkbutton2,
onvalue = 1,
offvalue = 0,
height = 2,
width = 10)

cb1.pack()
cb2.pack()

w.mainloop()

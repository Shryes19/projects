# def odd():
#     def calc(n):
#         for i in range(1,n,2):
#             print(i)
#     return calc
# c = odd()
# c(10)

#*********************************************************************#

# def outer_div(func):
#     def inner(x, y):
#         if x < y:
#             x, y = y, x
#         return func(x, y)
#
#     return inner
#
# @outer_div
# def divide(a, b):
#     return a / b
#
#
# print(divide(10,5))

#*********************************************************************#
# def convert_to_data_type(data_type):
#     def decorator(func):
#         def wrapper(*args):
#             result = func(*args)
#             return data_type(result)
#         return wrapper
#     return decorator
#
# @convert_to_data_type(str)
# def add_numbers(x, y):
#     return x + y
#
# a = int(input("Enter the number"))
# b = int(input("Enter another number"))
# result = add_numbers(a,b)
# print("Result:", result, type(result))
#
# @convert_to_data_type(str)
# def concatenate_strings(x, y):
#     return x + y
#
# a = input("Enter first word")
# b = input("Enter second word")
# result = concatenate_strings(a, b)
# print("Result:", result, type(result))

#*********************************************************************#


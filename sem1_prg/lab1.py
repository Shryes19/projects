# b = eval(input("Enter the base:\n"))
# h = eval(input("Enter the height:\n"))
# print(f"Area of triangle:\n{0.5*b*h}")

#*************************************************************************************#


# m = int(input("Enter the money in rupee:\n"))
# print(f"Money in shilling:\n{m/0.65}")
#
# #**************************************************************************************#
#
#
# a = eval(input("Enter the total amount:\n"))
# d = 0.1*a
# print(f"Discounted money:\n{a-d}")
#
# #*************************************************************************************#
#
#
# name = input("Enter your name:\n")
# fun_fact = input("Enter your fun fact:\n")
# print(f"My name is {name} and the fun fact about me is {fun_fact}")
#
# #************************************************************************************#
#
#
# amount = int(input("Enter total amount:\n"))
# n = int(input("Enter total number of friends:\n"))
# print(f"Each has to pay:\n{amount/n}")

#***********************************************************************************#


n = eval(input("Enter no. of workers:\n"))
m = eval(input("Enter work hours:\n"))
if m >= n:
    print(f"Work for each worker is:\n{m//n}\nWork left:\n{m%n} ")
else:
    print(f"Work for each worker is:\n{(m/n)}\nWork left:\n0 ")

#**********************************************************************************#


f_l = int(input("Enter floor length:\n"))
f_b = int(input("Enter floor breath:\n"))
t_l = int(input("Enter tile length:\n"))
t_b = int(input("Enter tile breath:\n"))
cost = int(input("Enter cost of each tile:\n"))
labor_charge = int(input("Enter labor charge:\n"))


a_f = f_b * f_l
a_t = t_b * t_l

t = a_f/a_t

print(f"Number of tiles:\n{t}")
print(f"Total cost:\n{(cost*t)+labor_charge}")

#**************************************************************************************#


num = int(input("Enter the number:\n"))

d = num%10  #4
c = num//10  #123
c= c % 10  #3
b = num//100  #12
b = b % 10  #2
a = num//1000  #1
a = a % 10  #1
print(f"{a}\n{b}\n{c}\n{d}\n")
print(f"Sum: {a+b+c+d}")

#************************************************************************************#


r = eval(input("Enter radius:\n"))
a = 3.14*r*r
p = 2*3.14*r
b = a/4
print(f"area of red: {b}\nperimeter: {p/4}")
c = (a - a/4)/3
print(f"area of blue: {c}\nperimeter: {p/4}")
d = a - (b+c)
print(f"Area of yellow: {d}\nperimeter: {p/2}")

#********************************************************************************************#


age = int(input("Enter your age:\n"))
days = age*365
print(f"months: {age*12}\ndays: {days}\nhours: {days*24}")

#************************************************************************************************#

p = eval(input("Enter principal amount:\n"))
r = eval(input("Enter rate:\n"))
t = eval(input("Enter time in years:\n"))
print(f"Simple interest: {(p*r*t)/100}")

#******************************************************************************************#


C = eval(input("Enter temperature celcius:\n"))
F = (C * (9/5)) + 32
print(f"Temperature fahrenheit:\n{F}")

#*****************************************************************************************#


s = int(input("Enter number of servings:\n"))
print(f"Cups of sugar req.:\n{s*(1/6)}")

#**************************************************************************************************#


n = eval(input("Enter number of pizza's:\n"))
s = eval(input("Enter slice per pizza:\n"))
p = eval(input("Enter number of people:\n"))

t_s = n*s
print(f"Slice per person:\n{t_s//p}\nSlice left out:\n{t_s%p}")
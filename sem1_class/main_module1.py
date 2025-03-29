# names = input()+' '
# l=[]
# s=""
# for i in names:
#     if i != " ":
#        s+=i
#     else:
#         l.append(s)
#         s=''
#
# n_l = [str(n)+'!'  if n[0].lower()=='a' else str(n) for n in l]
# for i in n_l:
#     print(i)



# from functools import reduce
#
# def get_book_details():
#     while True:
#         try:
#             title = input().strip()
#             year = int(input().strip())
#             price = float(input().strip())
#             if not title or year < 0 or price < 0:
#                 raise ValueError
#             return title, year, price
#         except ValueError:
#             print("Invalid input. Please enter this book's details again.")
#
# def main():
#     l=[]
#     try:
#         n = int(input().strip())
#         if n <= 0:
#             print("Please enter a valid number.")
#             return
#     except ValueError:
#         print("Please enter a valid number.")
#         return
#
#     books = []
#     for _ in range(n):
#         books.append(get_book_details())
#
#     filtered_books = list(filter(lambda book: len(book[0]) > 10 and book[1] > 2010, books))
#     # print(filtered_books)
#     l=list(map(lambda x: f"{x[0]} ({x[1]}): ${x[2]}", filtered_books))
#     t_p = reduce(lambda x,y: x+y[2], filtered_books,0)
#     for i in l:
#         print(i)
#     if len(filtered_books) != 0:
#
#         avg = t_p/len(filtered_books)
#         print(f"Average Price: ${avg}")
#         print(f"Total matching books: {len(filtered_books)}")
#
#     else:
#         print(f"Average Price: $0.00")
#         print(f"Total matching books: 0")
#
# main()


def stu_details():
    name = input()
    marks = float(input())
    return name,marks


n = int(input())
l=[]
for i in range(n):
    l.append(stu_details())
# print(l)

l2 = [(i[0],i[1])  for i in l if i[1]>80.0]
# print(l2)
if len(l2) != 0:
    d={}
    for i in l2:
        d[i[0]] = i[1]

    for key,value in d.items():
        print(f"{key}: {value}%")
else:
    print("No students passed.")



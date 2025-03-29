file = open("movies.txt", "r")
content = file.read()
content+="\n"

l = []
genre = []
director = []
movie = []
s = ""
for i in content:
    if i != "," and i != "\n":
        s = s + i
    else:
        l.append(s)
        s = ""


def get_genre(a):
    for i in range(0, len(a), 3):
        genre.append(a[i])
    #print(genre)


def get_director(a):
    for i in range(1, len(a), 3):
        director.append(a[i])
    #print(director)


def get_movie(a):
    for i in range(2, len(a), 3):
        movie.append(a[i])
    #print(movie)


get_movie(l)
get_genre(l)
get_director(l)


def total_movies(a):
    n = len(a)
    print("The total number of movies is", n)


# total_movies(movie)

def unique_genre(a):
    p = set(a)
    n = len(p)
    print("The total number of uniqe genre is:", n)


# unique_genre(genre)

def movie_per_genre():
    p = set(genre)
    temp = list(p)
    x = []
    for i in temp:
        for j in range(0, len(genre)):
            if genre[j] == i:
                x.append(movie[j])
        print("The list of movies in genre", i, ":", x)
        x = []


def director_per_genre():
    p = set(genre)
    temp = list(p)
    x = []
    for i in temp:
        for j in range(0, len(genre)):
            if genre[j] == i:
                x.append(director[j])
        print("The list of directors in genre", i, ":", x)
        x = []


def num_of_director():
    p = set(genre)
    temp = list(p)
    x = []
    for i in temp:
        for j in range(0, len(genre)):
            if genre[j] == i:
                x.append(director[j])
        print("The number of directors in genre", i, ":", len(x))
        x = []


# num_of_director()
# director_per_genre()
# movie_per_genre()

def movie_per_director():
    p = set(director)
    temp = list(p)
    x = []
    for i in temp:
        for j in range(0, len(director)):
            if director[j] == i:
                x.append(movie[j])
        print("The list of movies directed by", i, ":", x)
        x = []


# movie_per_director()
def num_per_director():
    p = set(director)
    temp = list(p)
    x = []
    for i in temp:
        for j in range(0, len(director)):
            if director[j] == i:
                x.append(movie[j])
        print("The number of movies directed by", i, ":", len(x))
        x = []


# num_per_director()

def a1():
    p = set(director)
    x=set()
    y=set()
    d={}
    l=[]
    l2=[]
    for i in p:
        for j in range(0, len(director)):
            if director[j] == i:
                x.add(genre[j])
                y.add((movie[j]))

        d[i] = f"{x},{y}"
        # print(d)
        # d={}
        for m in x:
            for n in range(0,len(genre)):
                if genre[n] == m and director[n] == i:
                    l.append(movie[n])
            if i not in l2:
                print(f"{i}:")
                l2.append(i)
            print((m,l))
            l=[]

        x=set()
        y=set()


def choose():
    print("Choose one option:")
    print("""
1.	Find the total number of movies.
2.	Find the number of unique genres.
3.	Display the list of movies in each genre.
4.	Find the number of directors in each genre.
5.	Find the list of directors who have directed movies in each genre.
6.	Find the number of movies directed by each director.
7.	Find the list of movies directed by each director.
8.	Find the number of movies directed by each director in each genre

    """)
    a = int(input())
    return a


u = choose()


def exe(b):
    if b == 1:
        total_movies(movie)
    elif b == 2:
        unique_genre(genre)
    elif b == 3:
        movie_per_genre()
    elif b == 4:
        num_of_director()
    elif b == 5:
        director_per_genre()
    elif b == 6:
        movie_per_director()
    elif b == 7:
        num_per_director()
    elif b == 8:
        a1()
    else:
        print("Invalid input")


exe(u)





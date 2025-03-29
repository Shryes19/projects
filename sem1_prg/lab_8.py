def sum(n):
    if n =='':
        return 0
    else:
        return int(n[0])+(sum(n[1:]))

print(sum('256'))


s = ''
def decimal_to_binary(n):
    n=int(n)
    global s
    if n == 1:
        return '1'
    else:
        m = int(n) % 2
        n = int(n) // 2
        return str(m)+str(decimal_to_binary(n))

x=(decimal_to_binary('212'))
print(x[::-1])


def count_ways_to_reach(n):

    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways_to_reach(n - 1) + count_ways_to_reach(n - 2) + count_ways_to_reach(n - 3)
print(count_ways_to_reach(5))


def flatten_list(l):
    f_l = []
    for i in l:
        if type(i) == int:
            f_l.append(i)
        else:
            f_l.extend(flatten_list(i))
    return f_l
print(flatten_list([1,2,[3,4]]))


def string_compression(s):
    if s == ' ':
        return ''
    t=(s[0])
    c=0
    for i in s:
        if (i) == t:
            c+=1
        else:
            c = str(c)
            return t+c+str(string_compression(s[int(c):]))
print(string_compression('aabbbc'+' '))



def isPowerOf4(n):
    if n==1:
        return True
    elif n<4:
        return False
    else:
        return isPowerOf4(n/4)



def callbackMechanism():
    x=[ ("890", "ram", (95,78,99)), ("123", "kishan", (90,98,89)), ("567", "arjun", (59,68,100)) ]
    def func_marks(l):
        return l[2]
    def func_name(l):
        return l[1]
    print(sorted(x,key=func_name))
    print(sorted(x,key=func_marks,reverse=True))


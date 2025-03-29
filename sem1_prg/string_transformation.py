import math
import os
import random
import re
import sys






def transformSentence(sentence):
    # Write your code here
    sentence.strip()
    l = sentence.split()
    print(l)
    s=''
    for i in l:
        start = i[0]
        for j in range(len(i)):
            if j==0:
                s+=i[0]
                print(s,'1')
            elif i[0] == start:
                s+=start.lower()
                print(s,'2')
            else:
                if i[j].lower() > i[j-1].lower():
                    s+=i[j].upper()

                elif i[j].lower() == i[j-1].lower():
                    s+=i[j].upper()
                    print(s)
                else:
                    s += i[j].lower()
        s+=' '
    return s


if __name__ == '__main__':

    sentence = input()

    result = transformSentence(sentence)

    print(result)
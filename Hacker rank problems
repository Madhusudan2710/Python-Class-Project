#1)Say “Hello, World!” With Python

my_string = "Hello, World!"
print(my_string)

#2)Arithmetic Operators

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)

#3)Python Division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)

#4)Loops

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i**2)

#5)Print Function

if __name__ == '__main__':
    n = int(input())
    st = ''
    for i in range(1, n + 1):
        st += str(i)
    print(st)

#6)Python if- else

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
    else:
        print("Weird")

#7)Python List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input())

l = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if n != (i + j + k):
                l.append([i, j, k])
print(l)

#8)Find the runnerup score!
n = int(input())
ui = input()
arr = ui.split(' ')
list1 = []
for i in arr:
    list1.append(int(i))
list2 = sorted(list(set(list1)))
print(list2[-2])

#9)Nested Lists
rec = []
names = []
scores = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    rec.append([name, score])
    #names+=[name]
    scores += [score]
scores.sort()
new_score = list(set(scores))
for i in range(len(rec)):
    if new_score[1] in rec[i]:
        names.append(rec[i][0])
t = sorted(names)
for i in t:
    print(i)

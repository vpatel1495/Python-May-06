#Assignment 2
#Problem 1
x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5+5j], 4000]
del x[4][0:2]
print(x)

x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5+5j], 4000]
del x[4][6]
print(x)

x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5+5j], 4000]
del x[4][4][2:4]
print(x)

x = [1, 2, 3, 4, [10, 20, 30, 40, [100, 200, 300, 400], "rishabh_", 5+5j], 4000]
del x[4][3:6]
print(x)



#Problem 2
x = list(range(1, 22))
y = 1
for i in range(0, 21):
    if (x[i]+y)%2 == 0:
        print(y, x[i], 'is a pair whose sum is even')
    else:
        print( )
    y= y+1



#Problem 3

def split(word):
    return[char for char in word]

from collections import Counter

sent=input('Write a string with special characters: ')
newsent = (split(sent))
n=len(newsent)
speclist=[]
i=0

while i < n:
    if (ord(newsent[i])< 65 and ord(newsent[i])>90) and (ord(newsent[i])<97 and ord(newsent[i])>122):
        x=newsent[i]
        speclist.append(x)
        i = i+1

Counter(speclist)



#Problem 4

def cube(x):
    x=x*x*x
    return x

numlist=list(range(1, 51))


for i in range(1, 50):
    x = cube(numlist[i])
    if (x % 2) == 1:
        print(x)



#Problem 5

import copy
x=input('Type in a list separating each object by a space')
y=x.split()
newlist=copy.copy(y)
newlist=y*3
print(newlist)



#Problem 6

def calc_word_length(y, n):
    for i in range(0, n):
        z=len(y[i])
        print('Length of ', y[i], ' is ', z)


x=input('Enter a sentence: ')
y=x.split()
n=len(y)

calc_word_length(y, n)



#Problem 7

x=(input('Type a list with no spaces in between: '))
print(x.isdigit())









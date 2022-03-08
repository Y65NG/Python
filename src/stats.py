import random
import numpy as np
import matplotlib.pyplot as plt

def shuffle(arr):
    """
    Shuffles an array.
    """
    temp = arr[:]
    for i in range(len(arr)):
        j = random.randint(0, len(temp)-1)
        temp[i], temp[j] = temp[j], temp[i]
    return temp

def stats(num, l, n):
    '''
    num: tested number
    l: length of arr
    n: repeat n times
    '''
    arr = list(range(1, l + 1))
    count = [0] * l
    for i in range(n):
        arr = shuffle(arr)
        pos = arr.index(num)
        count[pos] += 1
    return count

num = 1
l = 10
n = 100000
count = stats(num, l, n)
print(count)
plt.bar(range(1, l + 1), count)
plt.show()
# print(stats(2, 10, 100000)) 

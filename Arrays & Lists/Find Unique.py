# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.

import sys


def findUnique(arr, n):
    #Your code goes here
    count = 100
    for i in range(0, n):
        if arr.count(arr[i]) < count:
            count = arr.count(arr[i])
            res = arr[i]
    return res

#Taking Input Using Fast I/O


def takeInput():
    n = int(sys.stdin.readline().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1

# You have been given an integer array/list(ARR) of size N which contains numbers from 0 to (N - 2). 
# Each number is present at least once. 
# That is, if N = 5, the array/list constitutes values ranging from 0 to 3 and among these, there is a single integer value that is present twice. 
# You need to find and return that duplicate number present in the array.

import sys


def duplicateNumber(arr, n):
    #Your code goes here
    count = 1
    for i in range(0, n):
        if arr.count(arr[i]) > count:
            res = arr[i]
    return res

#Taking Input Using Fast I/O


def takeInput():
    n = int(sys.stdin.readline().strip())

    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split()))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0:

    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1

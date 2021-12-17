# You have been given an integer array/list(ARR) of size N. 
# It has been sorted(in increasing order) and then rotated by some number 'K' in the right hand direction.

# Your task is to write a function that returns the value of 'K', that means, 
# the index from which the array/list has been rotated.

from sys import stdin


def arrayRotateCheck(arr, n):
    #Your code goes here
    for i in range(n - 1):
        if(arr[i] > arr[i + 1]):
            return (i + 1)
    return 0


#Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0:

    arr, n = takeInput()
    print(arrayRotateCheck(arr, n))

    t -= 1

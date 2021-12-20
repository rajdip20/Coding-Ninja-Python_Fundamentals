# For a given two-dimensional integer array/list of size (N x M), 

# you need to find out which row or column has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''

from sys import stdin
MIN_VALUE = -2147483648


def findLargest(arr, nRows, mCols):
    #Your code goes here
    isRow = True
    largestSum = MIN_VALUE
    num = 0
    for i in range(nRows):
        rowSum = 0
        for j in range(mCols):
            rowSum += arr[i][j]
        if rowSum > largestSum:
            largestSum = rowSum
            num = i
    for j in range(mCols):
        colSum = 0
        for i in range(nRows):
            colSum += arr[i][j]
        if colSum > largestSum:
            largestSum = colSum
            num = j
            isRow = False
    if isRow:
        print("row "+str(num)+" "+str(largestSum))
    else:
        print("column "+str(num)+" "+str(largestSum))


#Taking Input Using Fast I/O
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])

    if nRows == 0:
        return list(), 0, 0

    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0:

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1

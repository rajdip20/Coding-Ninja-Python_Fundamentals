# Given a number N, figure out if it is a member of fibonacci series or not. 
# Return true if the number is member of fibonacci series else false.
# Fibonacci Series is defined by the recurrence
#   F(n) = F(n-1) + F(n-2)
#   where F(0) = 0 and F(1) = 1

import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x


def checkMember(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


n = int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")

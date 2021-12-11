# You are given first three entries of an arithmetic progression. 
# You have to calculate the common difference and print it.

a = int(input())
b = int(input())
c = int(input())

if(1 <= a <= 100 and 1 <= b <= 100 and 1 <= c <= 100):
    if(a < b):
        d = b-a
    if(b < c):
        e = c-b
    if(d == e):
        print(d)

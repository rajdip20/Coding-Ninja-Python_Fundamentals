# Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately.

#Digits mean numbers, not the places! That is, if the given integer is "13245", even digits are 2 & 4 and odd digits are 1, 3 & 5.


a = int(input())
x = 0
y = 0
while(a > 0):
    n = a % 10
    if(n % 2 == 0):
        x = x + n
    else:
        y = y + n
    a = a//10
print(x, y)

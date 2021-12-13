# Write a Program to determine if the given number is Armstrong number or not. 
# Print true if number is armstrong, otherwise print false.
# An Armstrong number is a number(with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
# For example,
#   371, as 3^3 + 7^3 + 1^3 = 371
#   1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634

num = input()
n = [int(i) for i in num]
count = 0
for j in range(len(n)):
    count = count+n[j]**len(n)
if count == int(num):
    print("true")
else:
    print("false")

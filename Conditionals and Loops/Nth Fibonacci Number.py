# Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -

# F(n) = F(n-1) + F(n-2),
# Where, F(1) = F(2) = 1

x = int(input())
n1, n2 = 0, 1
count = 0

if x <= 0:
    exit()
elif x == 1:
    print(n2)
else:
    while count < x:
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
    print(n1)

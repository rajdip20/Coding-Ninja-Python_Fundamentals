# Given an integer n, find if n is positive, negative or 0.
# If n is positive, print "Positive"
# If n is negative, print "Negative"
# And if n is equal to 0, print "Zero".

n = int(input())

if(-100 <= n <= 100):
    if(n < 0):
        print("Negative")
    elif(n > 0):
        print("Positive")
    else:
        print("Zero")

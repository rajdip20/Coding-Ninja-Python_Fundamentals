# Write a program to determine if given number is palindrome or not. 
# Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121


def checkPalindrome(n):
    temp = n
    rev = 0
    while(n > 0):
        dig = n % 10
        rev = rev*10 + dig
        n = n//10
    if(temp == rev):
        return True
    else:
        return False


n = int(input())
isPalindrome = checkPalindrome(n)
if isPalindrome == True:
    print("true")
else:
    print("false")

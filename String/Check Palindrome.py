# Given a string, determine if it is a palindrome, considering only alphanumeric characters.


str = input()
if str == str[::-1]:
    print("true")
else:
    print("false")

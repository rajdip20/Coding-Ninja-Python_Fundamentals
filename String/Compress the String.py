# Write a program to do basic string compression. 
# For a character which is consecutively repeated more than once, 
# replace consecutive duplicate occurrences with the count of repetitions.


def ab(a):
    i = 0
    x = ''
    while(i < len(a)):
        j = i+1
        c = 1
        while j < len(a) and (a[i] == a[j]):
            j += 1
            c += 1
        if c == 1:
            x += a[i]
        else:
            x += a[i]+str(c)
        i = j
    return x


a = input()
print(ab(a))

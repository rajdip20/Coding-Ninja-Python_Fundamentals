# Aadil has been provided with a sentence in the form of a string as a function parameter. 
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.

s = input()
new = s.split()
for i in range(len(new)):
    sad = new[i][::-1]
    print(sad, end=" ")

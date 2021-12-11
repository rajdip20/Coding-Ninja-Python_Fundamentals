# Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), 
# you need to convert all Fahrenheit values from Start to End at the gap of W, 
# into their corresponding Celsius values and print the table.

S = int(input())
E = int(input())
W = int(input())

while True:
    C = 0
    if S <= E:
        C = (S-32)*5/9
        print(S, int(C))
        S = S + W

    else:
        break

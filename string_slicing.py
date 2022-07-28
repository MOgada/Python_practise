x = input ("Enter the string....")
n = int(input ("Enter number of strings to remove"))
y = len(x)

print(y)

if n >= y:
    print ("The strings to remove are greater than the word itself")
elif n < y:
    print(x[int(n):])


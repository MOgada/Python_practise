num = [] #This is a blank array

for i in range(0,5):
    #ask for iput values in each iterative position.
    print("Enter number at location:", i, ":")

    #accept float number from user 
    x = float(input())

    #add it to the list
    num.append(x)

#print the appended values in the array
print (num)
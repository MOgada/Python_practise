number1 = 20
number2 = 30
product = number1 * number2
sum = number1 + number2
#This numbers are defined variables

#If else statement to ensure that if a product is greater than 1000 it outputs the sum
if product >= 1000:
    print("The result is:"+ str(sum))
elif product < 1000:
    print("The result is",end="" + str(product))

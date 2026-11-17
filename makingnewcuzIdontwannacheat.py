def addition (a,b):
    sum = a + b 
    return sum

def subtraction (c,d):
    difference = c - d 
    return difference

def multiplication (e , f):
    product = e * f
    return product

def division ( g , h ):
    quotient = g / h 
    return quotient

print ("==== FUNCTION CALCULATOR ====")

while True:
    try:

        print ("\n Addition : ")
        num1= float(input("Enter first number for addition : "))
        num2= float(input("Enter Second number for addition : "))

    except ValueError as ex:
        print (ex)
        continue
    else :
         print ("Result = ", addition(num1,num2))
         break

while True :
    try:

        print ("\nSubtraction : ")
        digit1= float(input("Enter first digit for subtraction : "))
        digit2 = float(input("Enter second number for subtraction : "))

    except ValueError as ex :
        print (ex)
        continue

    else :
        print ("Result = ", subtraction(digit1,digit2))
        break

while True :
    try:

        print ("\nMultiplication : ")
        int1= float(input("Enter first digit for multiplication : "))
        int2 = float(input("Enter second number for multiplication : "))

    except ValueError as ex :
        print (ex)
        continue

    else :
        print ("Result = ", multiplication(int1,int2))
        break

while True :
    try:

        print ("\nDivision : ")
        numone = float(input("Enter first digit for Division  : "))
        numtwo = float(input("Enter second number for Division : "))

        result = division (numone,numtwo)

    
    except ZeroDivisionError:
        print ("A number cannot be divided by 0!!")
        continue

    except ValueError as ex:
        print (ex)
        continue
    
    else :
        print ("Result = ", result )
        break

    


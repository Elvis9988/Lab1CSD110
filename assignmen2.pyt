# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# creating takeInput function to take user input
def takeInput(): 
    num1 = int(input ("Enter first number: "))
    num2 = int(input ("Enter second number: "))
    opt = (input ("Enter operator (+,-,*,/): "))
    
    # passing to displayResult
    displayResult(num1, num2, opt)

# creating displayResult function to perform calculations and print result
def displayResult(num1, num2, opt):
    if opt == "+":
        result = num1 + num2
        print (num1, "+", num2, "=" , result)
    elif opt == "-":
        result = num1 - num2
        print (num1, "-", num2, "=" , result)
    elif opt == "*":
        result = num1 * num2
        print (num1, "*", num2, "=" , result)
    elif opt == "/":
        result = num1 / num2
        print (num1, "/", num2, "=" , result)
        
# calling takeInput function 
takeInput()





    



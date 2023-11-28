# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# using constants as global variable
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# using function userinput to get user input and perform calculation
def userinput():
    pennies = int(input ("enter number of pennies: "))
    nickels = int(input ("enter number of nickels: "))
    dimes = int(input ("enter number of dimes: "))
    quarters = int(input ("enter number of quarters: "))
    totalCent = (pennies * PENNY_VALUE) + (nickels * NICKEL_VALUE) + (dimes * DIME_VALUE) + (quarters * QUARTER_VALUE)
    totalDollars = totalCent/PENNIES_IN_DOLLAR
    if totalDollars > 1:
        print ("Sorry, the amount you entered was more than one dollar")
    elif totalDollars < 1:
        print ("Sorry, the amount you entered was less than one dollar.")
    else:
        print ("Congratulations!")
        print("The amount you entered was exactly one dollar!")
        print("You win the game")
  
# calling the function userinput      
userinput()





# Author: Elvis Tamrakar, Student Id: 23056848
# By submitting this work, I assert that it is my own work and not copied from someone else or from some other source. 
# Copied work will be assigned a grade of 0 and be subject to further academic penalties at the discretion of the College.

# taking input from the user and using variables 
name = input ("Enter patient's name: ")
boolean = input("Has the patient been here before? (y/n): ")
height = int(input("What is the patient's height? (in cm): "))
weight = float(input("What is the patient's weight? (in kg): "))
datein = input("When was the patient last weighed in? (1/1/2000 if never weighed): ")
weight2 = float(input("What was the patient's weight? (in kg, -1 if never weighed): "))
healthassessment = int(input("Practitioner’s overall assessment of the patient’s health: "))
if weight2 == -1:
    changeinweight = 0
else:
    changeinweight = weight2 - weight
    

# calculating bmi using the appropriate formula
bmi = round((weight/(height**2))*10000, 1)

# assigning status according to the patient's bmi 
if bmi >= 30:
    status= "obese"
elif bmi >= 25 and bmi<=29.9:
    status= "overweight"
elif bmi >= 18.5 and bmi <= 24.9:
    status= "healthy"
elif bmi >= 17 and bmi <= 18.4:
    status= "underweight"
else:
    status= "too thin"

# assigining IMS values according to the status
if status == "obese" or status == "too thin":
    IMS = 0 
elif status == "overweight" or status == "underweight":
    IMS = 3
else:
    IMS = 5

# changing IMS values according to weightchange
if changeinweight == 0:
    IMS = IMS + 1
elif changeinweight < 1:
    IMS = IMS - 1
    
    
# modifying IMS values with respect to status and changeinweight
if status == "underweight" and changeinweight < 0:
        IMS = IMS - 3
elif status == "underweight" and changeinweight >= 1: 
        IMS = IMS + 2
elif status == "too thin" and changeinweight < 0:
        IMS = IMS - 5
elif status == "too thin" and changeinweight >= 1: 
        IMS = IMS + 5
elif status == "overweight" and changeinweight > 1:
        IMS = IMS - 3
elif status == "overweight" and changeinweight < 1:
        IMS = IMS + 2 
elif status == "obese" and changeinweight > 1:
        IMS = IMS - 5
elif status == "obese" and changeinweight < 1:
        IMS = IMS + 5

IMS = IMS + healthassessment

#showing PHA with respect to IMS values
if IMS > 5:
    PHA = "Great Condition!"
elif IMS < 5 and IMS > 3:
    PHA = "Need a little work"
elif IMS < 3 and IMS > 1:
    PHA = "Need a little work"
elif IMS < 1:
    PHA = "At risk!"

# output with respect to regular patient or first patient
if boolean == "n":
    print ("Melanie Diet Clinic")
    print ("*----------------------*")
    print ("Receipt for patient name: ", name )
    print ("Patient weight: ", weight)
    print ("----------------------------------")
    print ("BMI: ", bmi)
    print ("Health: ", IMS)
    print ("----------------------------------")
    print ("          Overall: ", PHA  )
elif boolean == "y":
    print ("Melanie Diet Clinic")
    print ("*----------------------*")
    print ("Receipt for patient name: ", name )
    print ("Patient weight: ", weight)
    print ("Patient's weight loss:", changeinweight)
    print ("----------------------------------")
    print ("BMI: ", bmi)
    print ("Health: ", IMS)
    print ("----------------------------------")
    print ("          Overall: ", PHA )   
else: 
    print ("Error")
    


    


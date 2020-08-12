"""
    Premium Amount Calculation

    1. Gender:male, Place : City, Health : Excellent ,
       Age: 21 to 41 and Policy Amount > 200000 then,
       Premium : Rs.6 Per thousand

    2. Gender:female, Place : City, Health : Excellent ,
       Age: 21 to 41 and Policy Amount > 100000 then,
       Premium : Rs.3 Per thousand

    3. Gender:male, Place : Village, Health : Poor ,
       Age: 21 to 41 and Policy Amount > 10000 then,
       Premium : 6% of Policy amount
"""


gender = input("Enter Gender :")
place = input("Enter Place :")
health = input("Enter Health :")
age = int(input("Enter Age :"))
policyamt = int(input("Enter Policy Amount :"))

if gender=="male" and place=="city" and health=="excellent" and age>=21 and age<=41 and policyamt>200000:
    premium=policyamt*6/1000
    print("Premium is Rs.6 per thousand  = Rs.",premium)
elif gender=="female" and place=="city" and health=="excellent" and age>=21 and age<=41 and policyamt>100000:
    premium=policyamt*3/1000
    print("Premium is Rs.3 per thousand  = Rs.",premium)
elif gender=="male" and place=="village" and health=="poor" and age>=21 and age<=41 and policyamt>10000:
    premium=policyamt*6/100
    print("Premium is 6 percent of policy amount = Rs.",premium)
else:
    print("Person not elegible")
    

"""
Assignment:
A certain grade of steel is graded according to the following conditions
	
	1. Hardness must be greater than 50
	2. Carbon content must be less than 0.7
	3. Tensile strength must be greater than 5600
	
    The grades are as follows:
	Grade is 10 if all three conditions are met
	Grade is 9 if conditions (i) and (ii) are met
	Grade is 8 if conditions (ii) and (iii) are met
	Grade is 7 if conditions (i) and (iii) are met
	Grade is 6 if only one condition is met
	Grade is 5 if none of the conditions are met
	
Write a program, which will require the user to give values of hardness, carbon content and tensile strength of the steel under consideration and output the grade of the steel.

"""    
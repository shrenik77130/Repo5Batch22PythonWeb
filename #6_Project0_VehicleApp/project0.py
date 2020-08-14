'''
WAP to create following menus to calculate and show ticket amount 

1. Private Vehicle (Rs.12 per km)
2. AC Vehicle (Rs.8 per km)
3. Reservation (Rs.5 per km)
4. Local Vehicle (Rs.2 per km)

WAP to input departure and arrival city name, distance. Calculate and show total fair amount
'''

import time
from os import system

departure = input("Enter Departure City Name :")
arrival = input("Enter Arrival City Name :")
distance = float(input("Enter Distance :"))



print("1. Private Vehicle")
print("2. AC Vehicle")
print("3. Reservation")
print("4. Local Vehicle")

choice = int(input("Enter Choice :"))

if choice==1:
    print("You selected Private Vehicle (Rs.12 per km)")
    fareamt = distance*12
    
elif choice==2:
    print("You selected AC Vehicle (Rs.8 per km)")
    fareamt = distance*8
    
elif choice==3:
    print("You selected Reservation (Rs.5 per km)")
    fareamt = distance*5
    
elif choice==4:
    print("You selected Local Vehicle (Rs.2 per km)")
    fareamt = distance*2
    
print("generating ticket...")
time.sleep(3)
system("cls")

print("\n ------------------------------- Ticket -------------------------------")
print(f"Departure City : {departure}")
print(f"Arrival City : {arrival}")
print(f"Departure City : {distance} km")
print(f"Fare Amount : Rs.{fareamt}")
print(" ---------------------------- Happy Journey ----------------------------")
    
    
 
    
    
    
    
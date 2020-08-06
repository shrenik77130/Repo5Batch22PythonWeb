#WAP to input 5 digit integer number. replace its
#last digit with the product of its first and last digit

no = int(input("Enter  Digit Integer Number :")) #83749


no = (no//10)*100   +    (no//10000)*(no%10)

print("After replace Last Digit, Number = ",no)


#837472

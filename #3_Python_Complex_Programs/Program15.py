#WAP to input three digit number and print its reverse

no = int(input("Enter 3 Digit Number :")) #276 -> 27 -> 2

rem=no%10 #6
rev=rem
no=no//10

rem=no%10 #7
rev=rev*10+rem
no=no//10

rem=no%10 #2
rev=rev*10+rem

print("Reverse = ",rev)



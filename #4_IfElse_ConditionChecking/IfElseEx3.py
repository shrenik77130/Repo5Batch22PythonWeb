#WAP to input three numbers and check which is max

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))
c=int(input("Enter value of c :"))

if a>b and a>c:
    print("a is Max")
elif b>a and b>c:
    print("b is Max")
else:
    print("c is Max")

#Ass: WAP to input any number and check that number
#is Palindrome Number or not.
#e.g.   215->512 : Not Palindrome
#       171->171 : Palindrome Number

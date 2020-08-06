#WAP to input two numbers and perform Swapping

a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))

print(f"value of a = {a} and value of b = {b}")

a,b = b,a

print("After interchange")
print(f"value of a = {a} and value of b = {b}")

#Ass: WAP to input two numbers and perform swapping
#without temporary variable

a=10
b=20

a=a+b #30
b=a-b #10
a=a-b #20 


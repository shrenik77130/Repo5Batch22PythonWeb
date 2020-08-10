'''
WAP to input any character and chek that entered character is vowel or consonent
'''

ch=input("Enter any Character :") #d

if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print(ch," is vowel")
else:
    print(ch," is Consonent")
    

#Method-2
print("Using Method 2")

if ch in "aeiouAEIOU":
    print(ch," is vowel")
else:
    print(ch," is Consonent")   

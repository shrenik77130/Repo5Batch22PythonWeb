'''
WAP to input any character and print its ASCII Code
ASCII -  Americal Standard Code for Information Interchange
'''

ch=input("Enter any Character :") #"7"

# ord() is builtin function in python to get ASCII code of any character
code = ord(ch)

print("ASCII Code = ",code)


'''
ASCII Codes Table (-128 to 127)

A to Z      : 65 to 90
a to z      : 97 to 122
"0" to "9"  : 48 to 57
special symbols : -128 to 47, 58 to 64, 91 to 96, 123 to 127
'''
#WAP to input string. count and print how many are capital characters, small characters and digits


sample_string = "Hello 12world39 END"

ucnt=lcnt=ncnt=0
for ch in sample_string:
    if ch.isupper():
        ucnt+=1
    elif ch.islower():
        lcnt+=1
    elif ch.isnumeric():
        ncnt+=1
        
print("Capital Charactes = ",ucnt)
print("Small Characters = ",lcnt)
print("Digit Count = ",ncnt)
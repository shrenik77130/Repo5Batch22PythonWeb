'''
WAP to print following pattern

*
* *
* * *
* * * *
* * * * *

'''

r=1
while r<=5:
    
    c=1
    while c<=r:
        print("*",end=" ")
        c=c+1
        
    print()
    r=r+1
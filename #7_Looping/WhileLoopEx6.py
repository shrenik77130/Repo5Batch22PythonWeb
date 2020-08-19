'''
WAP to print following pattern

Q1.                  Q2.
* * * * *            1 1 1 1 1
* * * *              2 2 2 2
* * *                3 3 3 
* *                  4 4
*                    5

'''

r=1
while r<=5:
    
    c=r
    while c<=5:
        print("*",end=" ")
        c=c+1
        
    print()
    r=r+1
    
r=1
while r<=5:
    
    c=r
    while c<=5:
        print(r,end=" ")
        c=c+1
        
    print()
    r=r+1
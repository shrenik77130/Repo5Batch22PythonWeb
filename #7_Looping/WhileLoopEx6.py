'''
WAP to print following pattern

Q1.                  Q2.
* * * * *            1 1 1 1 1
* * * *              2 2 2 2
* * *                3 3 3 
* *                  2 2 
*                    1

'''

r=1
while r<=5:
    
    c=r
    while c<=5:
        print("*",end=" ")
        c=c+1
        
    print()
    r=r+1
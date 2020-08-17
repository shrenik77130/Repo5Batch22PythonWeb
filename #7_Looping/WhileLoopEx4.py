'''
WAP to print following pattern

Q1.                     Q2.
* * * * *               1 2 3 4 5
* * * * *               1 2 3 4 5
* * * * *               1 2 3 4 5
* * * * *               1 2 3 4 5 
* * * * *               1 2 3 4 5

'''

r=1
while r<=5:
    
    c=1
    while c<=5:
        print("*",end=" ")
        c=c+1
    
    print()
    r=r+1
    
    
    
'''
Note
when r is 1, c-loop print 5 starts, when r become 2, c-loop print again 5 stars and so on
'''
    
    
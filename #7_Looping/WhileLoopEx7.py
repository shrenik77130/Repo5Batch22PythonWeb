'''
WAP to print following pattern

@1                      @2
    *                       *
   * *                     ***
  * * *                   *****
 * * * *                 *******     
* * * * *               *********

'''

r=1
while r<=5:
    
    s=r
    while s<=4:
        print(end=" ")
        s=s+1
    
    c=1
    while c<=r:
        print("*",end=" ")
        c=c+1
        
    print()
    r=r+1
    

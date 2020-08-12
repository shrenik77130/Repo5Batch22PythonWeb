#Program1

"""
    In Relational, Logical Operator, The Expression evaluation results wither in
    true (1) or false (0)
"""
a=5
b=6

ans=a>b
print("\n a=%d \t b=%d \t ans=%d"%(a,b,ans))

# Program2
x=21
y=29

ans=(x<10) == (y%3!=3)
print("\n a=%d \t b=%d \t ans=%d"%(a,b,ans))


# #Program3
a=2
a+=1

b=9
b+=a

ans=(a<b / (b>=a+5))
print("\n a=%d \t b=%d \t ans=%d"%(a,b,ans))

# #Program4
x=True
y=False

ans= x==y
print(ans)

print("\n x=%d \t y=%d \t ans=%d"%(x,y,ans))

# # #Program5

x=5
y=x-2

ans=x>2 and y%3==0
print("\n x=%d \t y=%d \t ans=%d"%(x,y,ans))

# #Program6 : Any Non zero value is always "true" (1)

x=99
y=9

ans = x+y >105 and 19
print("\n x=%d \t y=%d \t ans=%d"%(x,y,ans))

# #Program7
x=y=z=0
a=b=c=1

ans= (x+a < b+c) or (y+c % z+b !=0) and (1/(x+a+y+b) > 0)
print("\n ans=%d"%(ans))

# #Program8

a=[10,20,30,40,50]

result=40 in a
print(a)
print(result)

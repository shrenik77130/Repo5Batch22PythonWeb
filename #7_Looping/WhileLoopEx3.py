#WAP to input n1 and n2. print numbers between them which are divisible by 5 and by 3

n1=int(input("Enter n1 :")) #11
n2=int(input("Enter n2 :")) #50

while n1<=n2:
    if n1%5==0 and n1%3==0:
        print(n1,end="\t")
        
    n1=n1+1
        
        
#Ass: WAP to input n1 and n2. print numbers from last to first 
#WAP to input n1 and n2. print prime numbers between them

n1=int(input("Enter n1 :")) #7
n2=int(input("Enter n2 :")) #100

for no in range(n1,n2+1,1):
    cnt=0
    for d in range(1,no+1,1):
        if no%d==0:
            cnt+=1
            
    if cnt==2:
        print(no,end="\t")
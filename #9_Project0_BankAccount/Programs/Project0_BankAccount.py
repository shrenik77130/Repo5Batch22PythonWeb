'''
WAP to perform following transactions on bank account 
1. open account
2. show account
3. deposit amount
4. withdraw amount

take details userid, firstname, lastname, account no, opening balance to open new bank account.
'''
                #              0                           1               2  3  4
bankrecords=[]  #[[1,'smith','kapoor',1001,7000],[2,'...','...',1002,6500],[],[],[]]

while True:
    print("1. Open Account")
    print("2. Show Account")
    print("3. Deposit Amount")
    print("4. Withdraw Amount")
    print("5. Exit")

    choice = int(input("Enter Choice :"))

    if choice == 1:
        print("-----------------------------------------------")
        userid=int(input("Enter User Id :"))
        firstname=input("Enter First Name :")
        lastname=input("Enter Last Name :")
        accno=int(input("Enter Account Number :"))
        balance=float(input("Enter Opening Balance :"))
        print("-----------------------------------------------")
        
        account=[userid,firstname,lastname,accno,balance]
        bankrecords.append(account)
        
    elif choice == 2:
        user_accno = int(input("Enter Account Number to Show Account :")) #1232
        
        pos=-1
        for i in range(0,len(bankrecords),1):
            if user_accno==bankrecords[i][3]:
                pos=i
                
        if pos==-1:
            print("\n #ERROR : Invalid Account Number.")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(bankrecords[pos])
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
    elif choice == 3:
        user_accno = int(input("Enter Account Number to Deposit Amount :")) #1232
        
        pos=-1
        for i in range(0,len(bankrecords),1):
            if user_accno==bankrecords[i][3]:
                pos=i
                
        if pos==-1:
            print("\n #ERROR : Invalid Account Number.")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            amount = float(input("Enter Amount to deposit :"))
            bankrecords[pos][4] = bankrecords[pos][4] + amount
            print("Hello ", bankrecords[pos][1]," Account credited with Rs.", amount)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
    elif choice == 4:
        #Assinment
        pass
                   
    elif choice == 5:
        break
                
    
    
    
#WAP to solve List Questions

data = [
    [12,15,65,89,41], ["Red","Blue","Green"], [12,45,"one","two",7.54,56.54,True,False]
]

for R in data:
    print(R," Total values in List = ",len(R))


#Q1. Interchaange First and Last Element of list "data"
data[0],data[-1] = data[-1],data[0]

print("After interchage List Values = ",data)

#Q2. append new numbers in list containing only numbers
x=int(input("Enter x :"))
data[-1].append(x)

print("After append x , values in data[0] = ",data[-1])


cars = ["Bmw","Auddii","Mini Cooper","Ford","Ferrari"]

#Q3. add new car after 2 element in list "cars"
cars.insert(2,"Skoda")
print("Cars after insert at second position :",cars)








#WAP to create List of numbers and demonstrate List Functions


x = [10,11,12,13,14,15]

print(x)

print("First Number = ",x[0])
print("Last Number = ",x[-1])

print("First Two Number  = ",x[0:2])
print("Last Three Number  = ",x[-3:])

x.append(21)
x.append(22)
x.append(23)
x.append(24)

print("After append, list = ",x)

x.extend([100,200,300,400])

print("After extend, list = ",x)

x.remove(100)

print("After Remove, List = ",x)

x.pop(2)
print("After pop, list = ",x)





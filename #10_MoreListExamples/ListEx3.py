#WAP to create and show Dynamic List

emptylist = list()

while True:
    name = input("Enter Name :")
    city = input("Enter Name of City :")
    contact = input("Enter Contact Number :")

    record = [name,city,contact]

    emptylist.append(record)
    print("Record added in List")

    if input("Do you want to add new records? :") == "yes":
        pass
    else:
        break

print("\n",emptylist)

item={1:"tea",2:"Poha",3:"milk",4:"appe"}
price={1:10,2:20,3:50,4:20}
ikey=[]
qu=[]
print("*"*85)
print(f"{" "*30} Morya Hotel")
print("*"*85)
while True:
    print("""
                Menu
          1.Tea       2.Poha
          3.Milk      4.Appe
          """)
    name=input("Enter item name: ")
    quantity=input("Enter Quantity: ")
    ikey.append(name)
    qu.append(quantity)
    print(ikey)
    print(qu)
    ch=input("Do you want to continue: ")
    if ch=="n":
        print("-"*85)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format("Item Name","Quantity","Price","Total Amount"))
        print("-"*85)
        total=0
        for i in range(len(ikey)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(item[ikey[i]],qu[i],price[ikey[i]],qu[i]*price[ikey[i]]))
            print("-"*85)
            total=total+qu[i]*price[ikey[i]]
        print("Your Total Amount is: ",total)
        print("Thank You! \nVisit Again.....!")
        print("-"*85)
        break
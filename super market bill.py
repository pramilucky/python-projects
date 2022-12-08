from datetime import datetime

name = input("Enter your name:")

# list of items
lists= '''
Rice           Rs 20/kg
Wheat          Rs 50/kg
Gram flour     Rs 30/kg
Sugar          Rs 50/kg
Paneer         Rs 100/kg
Oil            Rs 150/liter
Horlicks       Rs 50/each
Soaps          Rs 20/each
Colgate        Rs 50/each
Biscuits       Rs 100/each
'''
# declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for items
items={'rice':20,
'wheat':50,
'gram flour':30,
'sugar':50,
'paneer':100,
'oil':150,
'horlicks':50,
'soaps':20,
'colgate':50,
'biscuits':100}

option= int(input("for list of items press 1:"))
if option ==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to purchase press 1 or 2 for exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your item quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            # for multiple items
            pricelist.append((item,quantity,items,price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount= gst+totalprice
        else:
            print("sorry you entered item is not available still now")
    else:
        print("you entered wrong number")
    inp = input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print("*"*25,"RAJI SUPERMARKET","*"*25)
            print("*"*30, " ","VISHAKAPATNAM"," ","*"*30)
            print("name:",name,30*" ","Date:",datetime.now())
            print("-"*80)
            print("sno"," "*8,'items'," "*8,'Quantity'," "*3,'price')
            

            for i in range(len(pricelist)):
                print(i," "*8, " "*5,ilist[i]," "*5,qlist[i]," "*8,plist[i])
            print("-"*80)
            print(" "*50,'TotalAmount:','Rs',totalprice)
            print("gst amount"," "*50,'Rs',gst)
            print("-"*50)
            print(" "*50,'finalAmount:','Rs',finalamount)
            print("-"*50)
            print("*"*30, 'THANK YOU FOR VISITING',"*"*30)
            print("-"*50)
            


            





















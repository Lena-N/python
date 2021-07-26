#input
PID=int(input("enter the product ID : "))
PD=input("enter the designation : ")
Cat=input("enter the category : ")
UP=float(input("enter the unit price : "))
Qty=int(input("enter the quantity : "))
DR=float(input("enter the discount rate : "))
MN=int(input("enter the month number : "))

#processing
up1=UP
Tot1=UP*(1-DR/100)

if MN in [1,2,3]:
    UP+=(5/100)*UP
elif MN in [4,5,6]:
    UP+=(12.5/100)*UP
elif MN in [7,8,9]:
    UP+=(8/100)*UP
else :
    UP=UP+(5.5/100)*UP 

Tot2=UP*(1-DR/100)

#output
print("Product ID: "+str(PID))
print("Designation : "+str(PD))
print("Category: "+str(Cat))
print("Quantity: "+str(Qty))
print("Discount rate: "+str(DR))
print("Main Price :\n unit price:$ %f \n the total price :$ %f "%(up1,Tot1))
#print("the total price is %f $" %(Tot1))

print("Spring Price: \n the unit price :$ %f \nTotal Amount :$ %f"%(UP,Tot2))
#print("Total Amount :$ %f" %(Tot2))
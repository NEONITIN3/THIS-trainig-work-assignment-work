class supermarket:
    pname=input("enter the product name=")
    qnt=int(input("enter the Qnt. = "))
    price=eval(input("enter the price= "))
s1=supermarket()
s2=supermarket()
#basic method of calling to
print(s1.pname,s1.price,s1.qnt, sep=" ")
print(s2.pname,s2.price,s2.qnt, sep=" ")


class market:
    def __init__(self,pname,qnt,price):
        self.productname=pname
        self.itemsno=qnt
        self.priceofproduct=price
s1=market("BADAM",231,2300)
s2=market("kaaju",765,7890)
print(s1.productname,s1.priceofproduct,s1.itemsno, sep=" ")
print(s2.productname,s2.priceofproduct,s2.itemsno, sep=" ")

#another way



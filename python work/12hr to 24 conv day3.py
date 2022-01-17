#12hr to 24 hr
l=input("enter the time").split(":")
#print(l)
l1=" : ".join(l)
print(l1)
l2=[int(l1[0])+12 if "PM" in l1 else l1]
print(l2)

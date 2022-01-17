#push all the zero at end of the list

l=input("enter the list ").split(",")
l.sort()
print(l[::-1])

#second way
l=input("enter the list ").split(",")
for i in l:
    if(int(i)==0):
        l.remove(i)
        l.append(i)
print(l)


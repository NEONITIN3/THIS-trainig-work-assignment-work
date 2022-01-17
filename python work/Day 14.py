# print("\U00001F600")
# print("\U0001F600")
# print("\U000001F600")

''''''
'''Q1'''
c=0
l=[]
for i in range(2000,3201):
    if (i%7==0 and i%5==0):
        l.append(i)
        c+=1
print("number is ",l)
print("number of divisor ",c)




'''Q2'''
n = int(input("Enter the number"))
fact = 1
while(n>0):
    fact = fact*n
    n = n-1
print(fact)

'''Q3solution '''

n=int(input())
d={i:i*i for i in range(1,n+1)}
print(d)
d1=[(k ,v) for k, v in d.items()]
print(d1)

'''Q4'''
n = input("input please=  ").split(",")
lst1 = list(n)
tup = tuple(n)
print(lst1)
print(tup)

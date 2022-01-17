# d=input("enter the D value= ").split(",")
# print(type(d))
#w=input("enter the w value= ").split(",")
# s=0
# print(d)
# for i in d:
#     s=s+i

#w1=sum(w)
# print(s)
# def total_fun(*args):
#     s=d1-w2
#     print(s)
# total_fun(d1,w2)
#D 100,W 100,D 300
# s=input("enter").split(",")
#s=" ".join(l)
# print(s)
# print(type(s))
# print(s[0])
# print(s[1])
#print("D" in s[0] )
# s1=list(s)
# print(s1)
def fun(l2):
    amt=0
    for i in range(len(l2)):
        if(l2[i][0]=="D"):
            amt=amt+int(l2[i][1])
        else:
            amt=amt-int(l2[i][1])
    return amt
l1=input("enter the value = ").split(",")
lis=list(map(lambda x:x.split(" "),l1))
print(fun(lis))
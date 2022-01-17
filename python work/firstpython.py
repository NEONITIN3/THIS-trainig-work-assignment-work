
import sys
var = 19
print(var)
var =90
print(var)
sp="A"
s="neo nitin"
d=90.9

print(s)

#type and size of var

print(type(var))
print(type(s))
print(type(d))
print(sys.getsizeof(sp))

n=-10
print(n)
print(type(n))
print(sys.getsizeof(n))
print(sys.getsizeof(s))
print(sys.getsizeof(var))
print(sys.getsizeof(sp))

#Another way of declaration
a,b=6,3
print(a)
print(b)
p=1,2,3,4,5,6,9,54,5
print(p)
p=1,2,3,4,5,6,9,0,-2,54,5
print(p)

#type casting
num=390
num1="439"
print(num+int(num1))
print(type(num1))

#char to int types
s="A"
n=4
print(n+int(ord(s)))

s="98"
n=4
print(n+int(s))

s="67"
n=4
print(str(n)+s)


  #input by user '''
#var =input('enter value 1= ')
""" by default its take string type"""

x="89"
"""now input should be int"""
#n = int(input("enter the value for n= "))
#print(int(x)+n)

#eval automatically take data type
#n = eval(input("enter the value for n= "))
#print(int(x)+n)

#multiple value in same time;
#x1,x2,x3=input('enter the 3 values = ').split(",")
#print(x1,x2,x3)


#arthmetic operators
z=10
w=2
print(z+w)
print(z-w)
print(z*w)
print(z/w)
print("for //")
print(z//w)

print(z%w)

print("for ** ")
print(z**w)

#relational operators
print(z>w)
print(z<w)
print(z>=w)
print(z<=w)
print(z!=w)
print(z==w)

#assigment operator
d=12
c=d
print(c)
print(c)
#print(z=num)


#bitwise operators

x=4
#100
y=2
#101

"""and operator)"""
print(x&y)

"""or Opretor"""
print(x|y)

'''XOR operator'''
print(x^y)

print(~x)

'''left shift'''
print(x>>y)

'''right shift'''
print(x<<y)

#print input and output 

a,b,c=10,23,23
print(a)
print(a,b)
print(a,b,c)

print(a, end="**")
print(a,b)
print(a,b,c)

#separator
print(a,b,c ,sep=" now ")



#controlling the output with if else if

x=0
z=90
x=eval(input("enter x value ="))
if(x>z):
    print('yes')
elif(x==0):
    print('x==0 hai')
else:
    print('x is less than z')

#swap two variable value w/t 3rd variable;
x=10
y=90
x,y=y,x
print('x=',x,'y=',y)



#user/email validation only for try 3 times

user="abcd"
email="abcd@gmail.com"
pwd="123"
c=1
us=input("enter your name/even= ")
p=input("enter your pass= ")
if((us==user or us==email) and p==pwd) and c<3:
    print("success login")
else:
    if c==3:
        print("logged out")
    else:
        c+=1
        print("try again")
us=input("enter your name/even= ")
p=input("enter your pass= ")
if((us==user or us==email) and p==pwd) and c<3:
    print("success login")
else:
    if c==3:
        print("logged out")
    else:
        c+=1
        print("try again")
us=input("enter your name/even= ")
p=input("enter your pass= ")
if((us==user or us==email) and p==pwd) and c<3:
    print("success login")
else:
    if c==3:
        print("logged out")
    else:
        c+=1
        print("try again")
us=input("enter your name/even= ")
p=input("enter your pass= ")
if((us==user or us==email) and p==pwd) and c<3:
    print("success login")
else:
    if c==3:
        print("logged out")
    else:
        c+=1
        print("try again")


#odd even
x=int(input('enter the values='))
if(x%2==0):
        print(x**2)        
else:
    print(x**3)
            


#day2
    
num1,num2=input("enter two numbers= ").split(",")
if(int(num1)==int(num2)):
    print("they are equals then =", num1+num2)
else:
    print("they are not equals so=", 2*(num1+num2))



'''
5rs and 1rs note and amount given adjest that notes'''
amount = eval(input("enter total amount: "))
a5rs_note = eval(input("enter available 5rs coin: "))
a1rs_rote = eval(input("enter available 1rs coin: "))

r5_note = amount//5
r1_note = amount%5
if(((r5_note*5) + r1_note)==amount and r1_note<=a1rs_rote and r5_note<=a5rs_note):
    print("total 5 rs coin: ",r5_note)
    print("total 1 rs coin: ",r1_note)
else:
    print("-1")


#anotherway
   
avial_5 = eval(input("Avil 5 Rupee"))
avial_1 = eval(input("Avil 1 Rupee"))
amt = eval(input("Amount"))
if(amt>=5):
    no_5 = amt//5
    if(no_5>=avial_5):
        no_5 = avial_5
    amt = amt -(5*no_5)

if(amt>=1):
    no_1 = amt//1
    if(no_1>=avial_1):
        no_1 = avial_1
    amt = amt - (1*no_1)

if(amt == 0):
    print(no_1)
    print(no_5)
else:
    print(-1)




























a=0
b=9
#print(b/a)
# ZeroDivisionError: division by zero




x=10
try:
    print(x)
    b=int(input("Enter value: "))
    if b==4:
        raise ValueError
    c=b/x
    print(c)
except ValueError:
    print("please give value other than 4")
except NameError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("No Exception")
finally:
    print("The 'try except' is finished")





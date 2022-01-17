#for accessing the global variable we used global key word other wise its take loacal preferenec
x=10
def fun():
    x=90
    print(x)
fun() #90 because its give preference to local
x=100
def fun():
    x=900+1
    print(x)
print(x)
fun()

#if we want to access that global x then used global keyword
x=100
def fun():
    global x
    x=900+x
    print(x)
print(x)
fun()
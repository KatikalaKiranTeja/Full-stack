#Non-parameterized function

def add():
    a = 10
    b = 20
    print(a+b)
add() 

def add():
    a = 17
    b = 12
    print(a+b)
add()

#Parameterized function

def add(a,b):
    print(a+b)
add(10,5)

#Keyword Argument

def movies(title, actor):
    print(title)
    print(actor)
movies(title="SSMB29", actor="MaheshBabu")

def demo(fname, sname):
    print(f"Hi {fname}{sname}")
demo(fname="Kiran", sname="Teja")

#Arbitary Arguments/*args

def add(*a):
    print(a)
add(2+4,8+9) #It gives the output in tuples

#**Keyword arguments

def details(name, pin, city):
    print(f"Hi i am {name} and my pin {pin} and i am from {city}")
details("Kiran", 525, "Gudiwada")
    
#default parameters

def Hotel(itemname, price, quantity, gst=0.05):
    totalprice=price*quantity
    include_gst=totalprice+totalprice*gst
    print(f"{quantity} {itemname} bill is {include_gst}")
Hotel("Idlt", 5, 5)
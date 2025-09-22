number=7
if number%2==0:
    print("It is even")
else:
    print("It is odd")
#-------------------------------------------------------------

number = 25
if number%5 == 0 and number%10!=0:
    print("satisfy")

#-------------------------------------------------------------

a = 4
b = 7
if a > b:
    print(f"the biggest num is {a}")
elif b > a:
    print(f"the biggest number is {b}")
else:
    print("no biggest number")
#-------------------------------------------------------------
a = 4
b = 7
if a < b:
    print(f"the smallest num is {a}")
elif b < a:
    print(f"the smallest number is {b}")
else:
    print("no smallest number")

#-------------------------------------------------------------
number = int(input())
def divisible():
    if number%2 == 0 and number%3 == 0 and number%6 == 0:
        print("number is divisible by 2,3 and 6")
    else:
        print("not divisible")
divisible()
#------------------------------------------------------------

person_age =int(input())
def vote():
    if (person_age >= 18):
        print("person is eligible to vote")
    else:
        print("not eligible")
vote()
#------------------------------------------------------------

maths=40
physics=36
chemistry=30
def total_marks():
    if maths > 35 and physics > 35 and chemistry > 30:
        print("pass")
    else:
        print("fail")
total_marks()
#-----------------------------------------------------------

maths=40
physics=30
chemistry=30
def total_marks():
    if maths >= 35 or physics >= 35 or chemistry >= 30:
        print("pass")
    else:
        print("fail")
total_marks()
#--------------------------------------------------

maths=40
physics=36
chemistry=30
def total_marks():
    if maths >= 35 and physics >= 35 or chemistry >= 30:
        print("pass")
    else:
        print("fail")
total_marks()
#-------------------------------------------------------------

def biggest_num(a, b, c):
    if a > b and a > c:
        print(f"biggest num is {a}")
    elif b > a and b > c:
        print(f"biggest num is {b}")
    else:
        print(f"biggest num is {c}")
biggest_num(10, 12, 15)
#---------------------------------------------------------------

num = 25
def per_sq():
    if (num**0.5):
        print("perfect square")
    else:
        print("not a perfect square")
per_sq()

#-----------------------------------------------------------------

members = 18
def cars_needed():
    if (members%5==0):
        print(members//5)
    else:
        print(members//5+1)
cars_needed()


#-------------------------------------------------------------------

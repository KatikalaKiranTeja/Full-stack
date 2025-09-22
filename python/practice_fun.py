#--->Add two numbers

def add(a,b):
    print(a+b)
add(4,8)

#--->return square of a number

def square(a,b):
    print(a*b)
square(8,3)

#--->Factorial of a num

def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a * fact(a-1)
fact(5)
print(f"factorial of a is {fact(5)}")

#--->Find greatest of two numbers

def greatest(a,b):
    if a>b :
        print(f"The is greatest num is a : {a}")
    elif b>a:
        print(f"The is greatest num is b : {b}")
    else:
        print(f"Both numbers are equal  ")
greatest(2,25)

#--->Return whether a number is even or odd

def even_odd(num):
    if num%2==0:
        return "Num is Even"
    else:
        return "Num is odd"
print(even_odd(10))
print(even_odd(21))

#---->Check if a number is prime

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(f"The prime num is {is_prime(8)}")
print(f"The prime num is {is_prime(2)}")
print(f"The prime num is {is_prime(19)}")

#--->To return maximum of three numbers

def maximum(a,b,c):
    if a>=b and a>=c:
        return f"{a} is maximum_of_three num a  "
    elif b>=a and b>=c:
        return f"{b} is maximum_of_three num  b"
    else:
        return f"{c} is maximum_of_three num  c"
    
print(maximum(2,1,0))
print(maximum(1,5,4))
print(maximum(1,2,6))

#--->To reverse a Num

def reverse_num(num):
    reversed_num = str(num)[::-1]
    print(reversed_num)
reverse_num(123)

#--->To find sum of digits of a number

num=123456789
def sum_of_even_digits():
    total=0
    for i in str(abs(num)):
        if int(i)%2==0:
            total +=int(i)
    return total
sum_of_even_digits()
print(sum_of_even_digits())

#--->simulate a basic calculator(add,sub,mul,div)
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))

#--->To check if a number is divisible by both 3 and 5

def check_number(num):
    if num%3==0 and num%5==0:
        print("The num is divisible by both 3 and 5")
    else:
        print("Not divisible")
check_number(25)
check_number(15)

#--->To return a square root of a number

import math
def square_root(num):
    return math.sqrt(num)
print(square_root(36))

#--->To find  maximum value from a list

list = [1,3,6,9,21,5,55]
def max_value():
    max_value = list[0]
    for i in list:
        if i > max_value:
            max_value=i
    print("Maximum value:",max_value)

max_value()

#--->To validate if age is eligible for driving
def age_eligible(age):
    if age>=18:
        print("Age is Eligible for driving")
    else:
        print("Not eligible")
age_eligible(18)

#--->To swap two numbers
def swap(a,b):
    a,b=b,a
    print(a,b)
swap(2,3)


def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num*0.5)):
        if num%i==0:
            return False
        return True
    
num=9
if is_prime(num):
    print("it is prime")

else:
    print("not prime")
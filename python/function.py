#It is the function which gives always same o/p----->static function
#def sample(): # function definition
 #   print("hello") # function body
#sample() # it is a function call

#It is the function which gives always different o/p----->dynamic function
# to define dynamic function-->we need parameters and arguments
# def sample(name): 
#     print(f"hello {name}") 
#     return
# sample("Kiran") 
# sample("Bhanu") 
# sample("Vamsi") 
# sample("Vimal") 

#Function with return

# def Theater(movie):
#     print(f"now showing {movie}")
#     return "Thankyou - visit again"
# print(Theater("Kingdom"))

# x=print(Theater("Kingdom"))
# print(x)

#return is used to return some values from function and then re-use
# that value anywhere in the program

# (add of 2 num)*(sub of 2 num)

# def add(a,b):
#     add=a+b
#     return add
# this function will return sum

# def sub(a,b):
#     sub=a-b
#     return sub
# # this function will return sum

# x=add(12,7)
# y=sub(12,7)
# op=x*y
# print(op)


#-->Using functions to check whether a num is armstrong are not

def Armstrong(num):
    num1=num
    num2=num
    sum=0
    count=0

    while(num>0):
        count +=1
        num = num//10

    while(num1>0):
        sum=sum+(num%10)**count
        num1=num1//10
    while(num2>0):
        sum=sum+(num%10)**count
        num2=num2//10
    if num2 == sum:
        return True
    else:
        return False

num=153
if Armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")

#-->check prvs and next numbers of given num is armstrong or not?

def Armstrong(num):
    num1=num
    sum=0
    count=0

    temp=num
    while(temp>0):
        count +=1
        temp = temp//10

    while(num1>0):
        digit=num1%10
        sum +=digit**count
        num1=num1//10
    return sum == num

num=153

if Armstrong(num-1):
    print(f"{num-1} is an Armstrong number")
else:
    print(f"{num-1} is not an Armstrong number")


if Armstrong(num+1):
    print(f"{num+1} is an Armstrong number")
else:
    print(f"{num+1} is not an Armstrong number")
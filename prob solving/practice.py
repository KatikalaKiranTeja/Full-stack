# num1=float(input("Enter the first num:"))
# num2=float(input("Enter the second num:"))
# result=num1+num2
# print(f"sum= {num1} + {num2} = {result}")
# num3=float(input("Enter the num3:"))
# num4=float(input("Enter the num4:"))
# if num4==0:
#     print("Error: Division by zero is not allowed")
# else:
#     div_result=num3/num4
#     print(f"Division :",div_result)


#==>  Area of a triangle

# base=float(input("Enter the base :"))
# height=float(input("Enter the height :"))
# Area = 0.5 * base * height
# print("Area of the triangle is ",Area)


#==> write a prog to swap a two numbers

# a=10
# b=20
# temp=a
# a=b
# b=temp
# print("Swaped values of a,b are :",a,b)


#==>write a program to generate a random number

# import random
# print(f"Ranndom numbers : {random.randint(1,100)}")


#==> write a python program to convert kilometers to miles

# kilometers = float(input("enter distance in kilometers :"))
# covertion_factor = 0.621371
# miles = kilometers * covertion_factor
# print(f"{kilometers} kilometers is equal to {miles} miles")

#==> write a python program to convert celsius to fahrenhiet

# celsius = float(input("Enter temperature in celsius :"))
# fahrenhiet = (celsius * 9/5)+32
# print(f"{celsius }  degree celsius is equal to {fahrenhiet} derees fahrenhiet")


#==> write a python program to display calender

# import calendar

# year = int(input("Enter year :"))
# month = int(input("Enter month :"))
# cal = calendar.month(year,month)
# print(cal)


#==> swap two numbers

# a=10
# b=15

# a,b=b,a
# print(f"a={a} b={b}")


#==> write a program to check if a number is positive, Negative or zero

# num = int(input("Enter number :"))
# if num>0:
#     print("Positive number")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative number")


#==>  write a program to check if a num is even or odd

# num = int(input("Enter a number ="))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


#==> write a program to check leap year

# year =int(input("Enteer year :"))
# if (year%4 == 0 and year%100 != 0 ) or year%400==0:
#     print("leap year")
# else:
#     print("Not a leap year")


#==> write a program to print it is prime or not

# num=int(input("Enter number :"))
# flag = False
# if num==1:
#     print(f"{num } is not a prime")
# elif num >1:
#     for i in range(2,num):
#         if num%i==0:
#             flag = True
#             break
# if flag:
#     print(f"{num} is not a prime number")
# else:
#     print(f"{num} is a prime number")



# lower = 1
# upper = 10
# print(f"Prime numbers betwee {lower} and {upper} are :")
# for i in range(lower, upper+1):
#     if i>1:
#         for num in range(2,i):
#             if i%num==0:
#                 break
#         else:
#             print(i)


#==> write a program to find the factorial of a number

# num=int(input("Enter number :"))
# fact=1
# if num<0:
#     print("Factorial does not exist negative number")
# elif num==0:
#     print("factorial of number 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact=fact*i
#     print(f"The factorial of {num} is {fact}")


#==>  write a program to print multiplication table

# num = int(input("Enter number :"))
# for i in range (1,11):
#     print(f"{num}x{i}={num*i}")


#==> write a program to check Fibonacci sequence

# num=int(input("Enter number :"))
# a,b=0,1
# count = 0
# print("Fibonacci sequence")
# while count < num:
#     print(a)
#     temp=a+b
#     a=b
#     b=temp
#     count +=1

#==> IN for loop

# num=int(input("Enter number :"))
# a,b=0,1
# count = 0
# for i in range(num):
#     print(a,end=" ")
#     a,b = b,a+b
#     count +=1

#==> In functions

# def fibonacci(num):
#     a,b=0,1
#     sequence=[]
#     for i in range(num):
#         sequence.append(a)
#         a,b=b,a+b
#     return sequence

# print(fibonacci(12))



#==> write a program to check Armstrong number
#==> It is in while loop

# num = int(input("Enter a number :"))
# num_str=str(num)
# num_digit = len(num_str)
# sum_of_power = 0
# temp_num = num

# while temp_num>0:
#     digit = temp_num%10
#     sum_of_power += digit ** num_digit
#     temp_num //=10
# if sum_of_power == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")


# num=153
# num1=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum += digit**num1
#     temp //=10
# if sum==num:
#     print(f"{num} is an Armstrong number ")
# else:
#     print(f"{num} is not an Armstrong number")


#==> In for loop

# num=153
# power=len(str(num))
# total=0
# for digit in str(num):
#     total += int(digit)**power

# if total == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not Armstrong number")


#==>  It is in functions
# def is_armstrong(num):
#     num1=len(str(num))
#     total=sum(int(digit)**num1 for digit in str(num))
#     return total == num
# print(is_armstrong(153))
# print(is_armstrong(9474))
# print(is_armstrong(944))



#===> write a python program to find the sum of natural numbera

# limit = int(input("Enter the limit :"))
# sum=0
# for i in range(1,limit+1):
#     sum +=i
# print(f"The sum of natural numbers up to {limit} is {sum}")


def swapp(s):
    if len(s)==0:
        return
    res=""
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            res += chr(ord(i)+32)
        elif ord(i)>=97 and ord(i)<=122:
            res += chr(ord(i)-32)
        else:
            res += i
    return res
s = "KiRaNtEjA"
print(swapp(s))







# num=int(input("Enter a number :"))
# if num%2==0:
#     print("Number is Even")
# else:
#     print("Odd")


# num=int(input("Enter Number :"))
# if num>0:
#     print("Positive Number")
# elif num<0:
#     print("Negative Number")
# else:
#     print("Zero")

# age=int(input("Enter Age :"))
# if age>=18:
#     print("Person Eligible to vote")
# else:
#     print("Not Eligible")


# a=10
# b=19
# if a>b:
#     print("a is greater ")
# else:
#     print("b is greater")


# num=int(input("Enter number :"))
# if num%5==0 and  num%11==0:
#     print("The Number is divisible by both 5 and 11")
# else:
#     print("Not divisible")


# score = int(input("Enter score :"))
# if 90 <= score <= 100:
#     print("Grade A")
# elif 80 <= score <= 89:
#     print("Grade B")
# elif 70 <= score <=79:
#     print("Grade C")
# elif 60 <= score <=69:
#     print("Grade D")
# else:
#     print("Grade F")


# year = int(input("Enter year :"))
# if year%4==0 and year%100 !=0 or year%400==0:
#     print("leap year")
# else:
#     print("Not")


# a=12
# b=10
# c=7
# if a<b and a<c:
#     print("a is smallest number")
# elif b<a and b<c:
#     print("b is smallest number")
# else:
#     print("c is smallest number")


# def check_charcter_type(char):
#     if len(char) !=1:
#         return "please enter a single character"
#     if char.isalpha():
#         if char.lower() in 'aeiou':
#             return "Vowel"
#         else:
#             return "Consonent"
#     elif char.isdigit():
#         return "Digit"
#     else:
#         return "Special Character"
    
# char=input("Enter a character :")
# result = check_charcter_type(char)
# print(result)


# def is_valid_triangle(angle1, angle2, angle3):
#     total=angle1+angle2+angle3
#     if total==180 and angle1>0 and angle2>0 and angle3>0:
#         return "Valid Triangle"
#     else:
#         return "Not Valid"
    
# angle1=int(input("Enter angle1 :"))
# angle2=int(input("Enter angle2 :"))
# angle3=int(input("Enter angle3 :"))
# result=is_valid_triangle(angle1,angle2,angle3)
# print(result)


# a=int(input("Enter number a :"))
# b=int(input("Enter number b :"))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)


# a=int(input("Enter side1 ="))
# b=int(input("Enter side2 ="))
# c=int(input("Enter side3 ="))

# if a == b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")


# num=int(input("Enter number :"))
# if (num & 1) ==0:
#     print("Even")
# else:
#     print("Odd")


# cost_price=int(input("Enter cost price :"))
# selling_price=int(input("Enter selling price :"))

# if selling_price > cost_price:
#     profit=selling_price - cost_price
#     print("Profit :",profit)
# elif cost_price > selling_price:
#     loss=cost_price - selling_price
#     print("Loss :",loss)
# else:
#     print("No profit ,No loss")
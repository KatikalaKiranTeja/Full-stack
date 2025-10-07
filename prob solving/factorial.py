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



#==> in functions
def fact(num):
    if num==0 or num==1:
        return 1
    return num*fact(num-1)
print(f"factorial of 5 is {fact(5)}")


#==> In for loop

num=5
fact=1
for i in range(2,num+1):
    fact *=i
print(f"Factorial of {num} is {fact}")


#==> while loop

num=6
fact=1
i=2
while i<=num:
    fact *=i
    i+=1
print(f"Factorial of {num} is {fact}")
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
fact(5)
    
print(f"Factorial of {6} is",fact(6))


num = 6
fact=1
if num < 0:
    print("it does not exit venue")
elif num==0:
    print("the fact of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact*i
    print(f"The factorial of {num} is {fact}")
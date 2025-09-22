for x in range(1,10):
    print(x)

for x in range(1,20):
    if x%2==0:
        print("Even numbers are :",x)

for x in range(1,20):
    if x%3==0:
        print("Odd numbers are :",x)

total=0
for x in range(1,101):
    total += 1
    print(total)


for x in range(1,11):
    print(f"5x{x}={5*x}")


for x in range(1,50):
    if x%3==0:
        print("The numbers divisible by 3 is :",x)

num=5
factorial=1
for x in range(1, num+1):
    factorial *=x
    print(f"Factorila {num} is {factorial}")

num = 456
n=num
sum=0
length=len(str(num))
for x in range (length):
    d=n%10
    n=n//10
    sum=sum*10+d
print(sum)

for x in range(1,11):
    print(f"square is {x**2}")
    

num=23456
count=0
for i in str(abs(num)):
    count +=1
print(count)

num_of_digits=4567
sum=0
for x in str(abs(num_of_digits)):
    sum +=int(x)

print(sum)

for x in range(1,50):
    if x%3==0 and x%5==0:
        print(x)


#-->Print the sum of numbers from 1 to 100
total=0
for x in range(1,101):
    total +=x
print(total) 

#-->Print even numbers from a list
nums=[1,4,7,10,12,15]
for x in nums:
    if x%2==0:
       print(x,end=" ")

#-->Print the multiplication table of a number (e.g., 5)
num=5
for x in range(1,11):
    print(f"5x{x}={5*x}")

#-->Calculate factorial of a number using a for loop
num=5
factorial=1
for x in range(1, num+1):
    factorial *=x
print(f"Factorila {num} is {factorial}")

#-->Find the maximum number in a list
input = [5,10,3,8,2]
max_num = input[0]
for x in input:
    if x>=max_num:
        max_num=x 

print("max num ",max_num)

#-->Reverse a string using a for loop
input="hello"
op=""
for x in input:
    op=x + op
print(op)
#------------------------
input="hello"
for x in range(len(input)-1,-1,-1):
    print(input[x],end="")



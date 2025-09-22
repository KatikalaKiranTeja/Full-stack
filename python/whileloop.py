count=1
while count<=5:
    print(count)
    count += 1
print("out of the loop")

count=5
while count>0:
    print(count)
    count -= 1
print("out of the loop")

num=1
while num<=5:
    print(num)
    num += 1
    if num ==3:
        break
print("out of the loop")

number=int(input("enter your number(-1 to q)"))
while number != -1:
    print(number)
    number=int(input("enter your number(-1 to q)"))   
else:
    print("in else block") 
print("Out of the loop")


num=25480
while(num>0):
    ld=num%10
    print(ld,end="")
    num=num//10


num=862492
rev=0
#logic : (i*num)+anothernum
while(num>0):
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev)

#PALINDEOME
num=152251
num1=num
rev=0
while(num>0):
    id=num%10
    rev=rev*10+id
    num=num//10
print(rev)
if (num1==rev):
    print("it is palindrome")
else:
    print("it is not a palindrome")

#add the digits in a given num
num=123
sum=0
while (num>0):
    sum +=num%10
    num=num//10
print(sum)

#Squares
num=123
sq=0
while (num>0):
    id=num%10
    sq +=id**2
    num=num//10
print(sq)

#find the len of given num without converting into string
num=4567
count=0
while(num>0):
    count +=1
    num=num//10
print(count)

#sum of only even num in given ip
#count only odd num in given ip
num=1238765
sum=0
while (num>0):
    ip =num%10
    if(ip%2==0):
        sum = sum+ip
    num=num//10
print(sum)

num=1238765
count=0
while (num>0):
    ip =num%10
    if(ip%2!=0):
        count +=1
    num=num//10
print(count)

#--->Armstrong Number
num=152
num1=num
num2=num
sum=0
count=0
while(num>0):
    count +=1
    num = num//10
    print(count)
while(num1>0):
    sum=sum+(num%10)**count
    num1=num1//10

if num2==sum:
    print("Armstrong")
else:
    print("Not")
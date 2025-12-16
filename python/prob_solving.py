num=12345
sum=0
while num>0:
    sum += num%10
    num = num//10
print(sum)

num=9
sq=num**2
res=0
while sq>0:
    r = sq%10
    res += r
    sq = sq//10
if res==num:
    print("neon number")
else:
    print("not a neon number")


#===> Prime Number
def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num)):
        if num%i==0:
            return False
        return True
    
num=2
if prime(num):
    print("It is prime num")
else:
    print("Not a prime")
def prime(num):
    if num<=1:
        return False
    for i in range(2,int(num)):
        if num%i==0:
            return False
    return True
    
num=2
print(prime(num))


#===> Perfect Square using forloop and Functions
import math
num=8
def perf_sq(num):
    if math.sqrt(num)**2:
        return True
    else:
        return False
print(perf_sq(num))


n=17
flag=0
for i in range(1,n//2):
    if i**2==n:
        flag=1
        break
if flag==0:
    print("Not a perfect square")
else:
    print("Perfect square")

import math
def strong_num(num):
    num1=num
    sum_of_fact=0
    while num1 > 0:
        d=num1%10
        sum_of_fact +math.factorial(d)
        num1 //=10
    return sum_of_fact == d
num=145
if strong_num(num):
    print(f"{num} is strong number")
else:
    print("Not a strong number")

a=145
n=a
res=0
while n>0:
    fact=1
    r=n%10
    for i in range(1,r+1):
        fact*=i
    res +=fact
    n //=10
print(res)
if res==a:
    print("strong num")
else:
    print("Not")
    


ip="aabbaaccbb"
d = {}
for i in ip:
    if i in d:
        d[i] +=1
    else:
        d[i] =1
result =""
for i in d:
    result=result+i+str(d[i])
print(result)



ip="aaabbababa"
d={}
for i in ip:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
res=""
for i in d:
    res=res+i+str(d[i])
print(res)
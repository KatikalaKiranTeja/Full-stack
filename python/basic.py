a=6
b=7
sum=a+b
print(sum)
diff=a-b
print(diff)
prod=a*b
print(prod)
print("======================")

name=input("Enter name :")
age=int(input("Enter age :"))
print(f"Hello {name}, you will be {age+5} in five years.")



#==>  Control statements

n=20
for i  in range(1,n):
    if i%2==0:
        print(i)
print("==============")
  
  
# Multiplication table 
        
n=1
while n<=10:
    print(f"Multiplication table of {n}")
    i=1
    while i<=10:
        print(f"{n}x{i}={n*i}")
        i +=1
    n +=1
    
n=1

for n in range(1,11):
    print(f"Multiplication table for {n} ")
    for i in range(1,11):
        print(f"{n}x{i}={n*i}")




#===> Data Structures

list=[1,2,6,9,0]
max_value=max(list)
min_value=min(list)
for i in list:
    if i > max_value:
        max_value=i
    if i < min_value:
        min_value=i
print("maximum value :",max_value)
print("minimum value :",min_value)

d={"kiran":"9173671552",
    "vimal":"8753892621",
    "vamsi":"6307286221"
    }
for name , phonenum in d.items():
    print(f"Name:{name} , phone:{phonenum}")


#===>  Functions

n=5
fact=1
for i in range(1,n+1):
    fact *=i
print(f"factorial of {n} is {fact}")

def fact(n):
    for i in range(n):
        if n<=1:
            return 1
        else:
            return n*fact(n-1)
n=6
print(fact(n))

def list_sum(num):
    total = 0
    for i in num:
        total += i
    return total
num=[1,4,6,5,9]
print("sum of num :",list_sum(num))



def sum(n):
    total=0
    i=0
    while i<len(n):
        total +=n[i]
        i += 1
    return total

num=[1,2,3,4,5]
print("sum of num :",sum(num))


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
limit=20
primes=[]
for i in range(2,limit+1):
    if is_prime(i):
        primes.append(i)
print("Original primes :",primes)

if len(primes)>=2:
    primes = primes[-2:]+primes[:-2]
print("After primes :",primes)

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for i in range(2,101):
    if is_prime(i):
        print(i,end=" ")







    




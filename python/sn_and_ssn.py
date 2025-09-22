ip=[1,1,10,5,-6,9,1,2]
sn=ip[0]
ssn=ip[0]
for i in ip:
    if i<sn:
        ssn=sn
        sn=i
    elif i<ssn and i!=sn:
        ssn=i
print("The first smallest number is ",sn)
print("The second smallest number is ",ssn) 
        

#===> first largest and second largest number

ip=[10,10,9,-4,12,3]
ln=ip[0]
sln=ip[0]
for i in ip:
    if i>ln:
        sln=ln
        ln=i
    elif i>sln and i!=ln:
        sln=i
print("The first largest number is ",ln)
print("The second largest number is ",sln)


#====>prime number

n=23
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
        break
if flag:
    print("prime")
else:
    print("not prime")


def is_prime(n):
    if n<2:
        print("not prime")
        return
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            return
print("prime") 


n=25
def is_prime(x):
    if x<=1:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
for i in range(1,n):
    if is_prime(i):
        print(i,"prime")
    else:
        print(i,"not prime")


        
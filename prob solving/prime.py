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



lower = 1
upper = 10
print(f"Prime numbers betwee {lower} and {upper} are :")
for i in range(lower, upper+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:
                break
        else:
            print(i)


#==> In functions

def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num+1):
        if num%i==0:
            return False
        return True
print(is_prime(7))

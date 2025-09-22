#For Loop

#for x in range (1,10,3):
 #   print(x)
#---------------------------------------

#for x in range (1,11):
#    print(f"2x{x}={2*x}")
#---------------------------------------

#for x in range(20,51):
##    if(x%3==0):
#        print(x)
#---------------------------------------
        
#for x in range(10,41):
#    if(x%3==0 and x%5==0):
#        print(f"{x}-frezzbuzz")
#    elif(x%5==0):
#        print(f"{x}-buzz")
#    elif(x%3==0):
#        print(f"{x}-frizz")
#---------------------------------------

#for x in range(10,0,-1):
#    print(x)
#---------------------------------------

#str = "fullstack"
#for x in str:
#    print(x)
#---------------------------------------

#li=['hi','hello']
#for x in li:
#    print(x)
#---------------------------------------
#str = "something"
#for x in str:
#    print(f"{x}-hi")
#---------------------------------------

#str = "something"
#for x in range(0,len(str),2):
#    print(str[x])
#---------------------------------------

str = "something"
for x in range(len(str)-1,-1,-1):
   print(str[x],end="")
#---------------------------------------

#ip = "hello"
#for x in range(len(ip)-1,-1,-1):
#    print(ip[x])
#---------------------------------------

#ip = "hello"
#op = ""
#for x in range(len(ip)-1,-1,-1):
#    op += ip[x]
#print(op)
#---------------------------------------

# print num from (100,0) in reverse oder which is divisible by 5
# def reverse():
#     for i in range(100,0,-1):
#         if (i%5==0):
#             print(i)
# reverse()
#----------------------------------------

#write a function to print tables in reverse

# def table():
#     for x in range (10,0,-1):
#         print(f"5x{x}={5*x}")
# table()

#check whether the given string is palindrome or not using a function

# def palindrome():
#     x="madam"
#     y=""
#     for i in range(len(x)-1,-1,-1):
#         y += x[i]
#     print(y)
#     if (x==y):
#         print("it is palindrome")
#     else:
#         print("it is not a palindrome")
# palindrome()

#compare each one of age and check they are eligible or not
# l1=["kiran", "vimal", "vamsi", "gopi"]
# l2=[24,17,18,20]
# for i in range(len(l1)):
#     if l2[i] >= 18:
#         print(l1[i],"-",l2[i],"eligible")
#     else:
#         print(l1[i],"-",l2[i],"not eligible")

#using forloop add n=1+2+3==>6
# n = 123
# total = 0

# for i in str(n):
#     total += int(i)

# print(total)


#biggest num in n
# n=123459789
# total=-1
# for i in str(n):
#     if int(i) > total:
#         total = int(i)
# print("maximum number is",total)

# n=123459789
# total=-1
# while n>0:
#     i = n%10
#     if i >= total:
#         total = i
#     n = n//10
# print(total)

#find smallest num in n

# n=123459789
# total=n
# for i in str(n):
#     if int(i) <total:
#         total = int(i)
# print("mininum number is",total)

#------------------------------------------------
# Amount =100
# choc_price=Amount
# wrappers=100
# while wrappers >= 3:
#     extra = wrappers//3
#     choc_price += extra
#     wrappers =  extra + wrappers % 3 
# print(choc_price)

# list=["Hi","kiran", "welcome"]
# #for i in list:
#  #   print(i)
# for i in range(len(list)):
#     print(list[i])

#-----------------------------------------------------
# ip=['k','i','r','a','n']
# op = ' '
# for i in ip:
#     op +=f'{i}_'
# print(op)

#-------------------------------------------------------
# ip=['k','i','r','a','n']
# op = ""
# for i in range(len(ip)-1,-1,-1):
#     op +=f"{ip[i]}_"
# print(op)

#---------------------------------------------------------
# find the smallest number without using builtin functions

# ip = [2,4,6,4,3,7]
# smallest = ip[0]
# for x in ip:
#     if x<smallest:
#         smallest=x
# print("smallest num is",smallest)



# ste1 ={"hi","hello","hey"}
# for i in ste1:#we do not use range in sets it is not applicable
#     print(i)

# los=[{1,2,3},{4,5,6},{"hii"}]
# for i in los:
#     print(i)

# s = "gfg"
# for i in s:
#     print(i)
#     print(i)

# total = 0
# num = int(input("Enter number (0 to stop): "))
# while num != 0:
#     total += num
#     num = int(input("Enter number (0 to stop): "))
# print("Total sum:", total)


# n = int(input())

# Your code here
# for i in range(n):
#     if i == 0:
#         print('* ' * n)
#     elif i == n - 1:
#         print('* ' * n)
#     else:
#         print('*', ' ' * (2 * n - 3), '*', sep='')

#-----------------------------------------------     
#Factorial of a number 
# def factorial (n):
#     if n<0:
#         return "factorial of -ve num not occur"
#     if n==0 or n==1:
#         return 1
#     return n *factorial(n-1)
# print(factorial(5))


#---------------------------------
# for i in range(5):
#     if i == 3:
#         break
#     print(i, end="")
# else:
#     print("Done")

# #---------------------------------
# for i in range(5):
#     if i == 2:
#         continue
#     if i == 4:
#         break
#     print(i)
# #---------------------------------
# x = 0
# for i in range(10):
#     if i % 2 ==0:
#         continue
#     if i > 5:
#         break
#     x += i
# print(x)
# #---------------------------------
# for i in range(10):
#     if i == 5:
#         break
#     if i % 2 ==0:
#         continue
#     print("Hello")
# #---------------------------------


#even num length names in forward direction
# list1=['kiran','ramesh','vimal','arun','bhanu','vamsi','gopi','nagendra','pranav','anil']
# for i in range(len(list1)):
#     if i%2==0:
#         print(list1[i])


# #even num length names in backward direction
# list1=['kiran','ramesh','vimal','arun','bhanu','vamsi','gopi','nagendra','pranav','anil']
# for i in range(len(list1)-1,-1,-1):
#     if i%2==0:
#         print(list1[i])


#using while loop even num length names in forward direction

# list1=['kiran','ramesh','vimal','arun','bhanu','vamsi','gopi','nagendra','pranav','anil']
# i=0
# while i < len(list1):
#     if i%2==0:
#         print(i,list1[i])
#     i+=1
   

# #using while loop even num length names in backward direction
# list1=['kiran','ramesh','vimal','arun','bhanu','vamsi','gopi','nagendra','pranav','anil']
# index=len(list1)-1
# while index >=0:
#     if index%2==0:
#         print(index,list1[index])
#     index -= 1
   


# num=50
# i=1
# while i < num:
#    print(i)
#    i +=1

# num=123
# sum=0
# while num>0:
#     sum +=num%10
#     num//=10
# print(sum)

# num=124356789
# sum=0
# while num>0:
#     sum +=num%10
#     num //=10
# print(sum)


# num=98765321
# rev=0
# while num>0:
#     digit=num%10
#     rev =rev*10+digit
#     num //=10
# print(rev)


# num=123
# rev=0
# while num>0:
#     digit=num%10
#     rev =rev * 10 +digit
#     num//=10

# print(rev)

# num=5
# num1=num
# fact=1
# while num1>0:
#     fact *=num1
#     num1 -=1
# print(f"factorial of {num} is {fact}")

# num=9
# num1=num
# fact=1
# while num1>0:
#     fact *=num1
#     num1 -=1
# print(f"factorial of {num} is {fact}")


# num=1234567
# count=0
# while num>0:
#     num = num//10
#     count +=1
# print("Number of digits",count)

# num = 987654321
# count = 0
# while num>0:
#     num =num // 10
#     count +=1
# print(count)


# num=7
# a,b = 0,1
# count =0
# while count < num:
#     print(a,end="")
#     a,b=b,a+b
#     count +=1

# num=12
# a,b = 0,1
# count = 0
# while count < num:
#     print(a,end="")
#     a,b = b, a+b
#     count +=1


# num=50
# i=2
# while i<=num:
#     print(i)
#     i +=2

# num=100
# i=2
# while i<=num:
#     print(i)
#     i += 2

# num=121
# num1=num
# rev =0
# while num1>0:
#     digit = num1%10
#     rev = rev*10+digit
#     num1 = num1//10
# if rev==num:
#     print("palindrome")
# else:
#     print("not")


# num=4567
# num1=num
# rev =0
# while num1>0:
#     digit = num1%10
#     rev = rev * 10 +digit
#     num1 = num1//10
# if rev == num:
#     print("palindrome")
# else:
#     print("Not a palindrome")


# str = "madam"
# rev = ""
# i = len(str)-1
# while(i>=0):
#     rev +=str[i]
#     i -=1

# if rev==str:
#     print("palindrome")
# else:
#     print("Not palindrome")


s ="banana"
freq ={}
i = 0
while i<len(s):
    char = s[i]
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
    i +=1
print(freq)

s = "cherry"
freq = {}
i =0
while i<len(s):
    char=s[i]
    if char in freq:
        freq[char] +=1
    else:
        freq[char]=1
    i +=1
print(freq)
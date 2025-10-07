
# ip="aabbaaccbb"   #O/P = a4b4c2
# d = {}
# for i in ip:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i] =1
# result =""
# for i in d:
#     result=result+i+str(d[i])
# print(result)



# ip="aaabbababa"
# d={}
# for i in ip:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i] = 1
# res=""
# for i in d:
#     res=res+i+str(d[i])
# print(res)


# #using inbuild function
# ip="aaabbababa"
# l=[]
# res=""
# for i in ip:
#     if i not in l:
#         l.append(i)
#         res=res+i+str(ip.count(i))
# print(res)

# s="vahujdyec"
# l=[]
# res=""
# for i in s:
#     if i not in l:
#         l.append(i)
#         res=res+i+str(s.count(i))
# print(res)


# s="aabbaaccbb"
# count=0
# res=""
# for i in range(1,len(s)):
#     if s[i] ==s[i-1]:
#         count +=1
#     else:
#         res +=s[i-1] +str(count)
#         count = 1
# res +=s[-1]+str(count)
# print(res)



#===> Largest among two numbers
# a=10
# b=2
# c=8
# if a>b and a>c:
#     if b>c:
#         print(a+b)
#     else:
#         print(a+c)
# elif b>a and b>c:
#     if a>c:
#         print(b+a)
#     else:
#         print(b+c)

# else:
#     if a>b:
#         print(a+c)
#     else:
#         print(c+b)




# list=[1,2,3,4,5]   #O/P = [4,5,1,2,3]
# list1=list[len(list)-2::]+list[0:len(list)-2]
# print(list1)

# l=[1,2,3,4,5] 
# l1=[]
# l1.append(l[-2])
# l1.append(l[-1])
# l.remove(l[-2])
# l.remove(l[-1])
# l1 = l1+l
# print(l1)
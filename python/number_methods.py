# num= float('inf')
# list=[100,1000,10000,100000]
# for i in list:
#     if i>num:
#         num=i
# print(num)


num= float('-inf')
list=[-20,30,-50,10]
for i in range(len(list)):
    if abs(list[i])>num:
        num=abs(list[i])
print((num))


# num=1234
# print(divmod(num,2))


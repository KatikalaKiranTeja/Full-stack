# rows = 5
# for x in range(1,rows):
#     for y in range(1,x):
#         print("*"*y)
# print()


# rows = 5
# for i in range(1,rows + 1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


n=5
for i in range(n,0,-1):
    s=" "*(n-i)
    if i==1:
        print("*"+s+"*"*(i)+s+"*")
    else:
        if i==n:
            print("* "+"  "*(i-1)+"*")
            print("*"+s+"* "+"  "*(i-2)+"*"+s+"*")
        else:
            print("*"+s+"* "+"  "*(i-2)+"*"+s+"*")
            
for i in range(2,n+1):
    s=" "*(n-i)
    if i==1:
        print("*"+s+"*"*(i)+s+"*")
    else:
        if i==n:
            print("*"+s+"* "+"  "*(i-2)+"*"+s+"*")
            print("* "+"  "*(i-1)+"*")
            
        else:
            print("*"+s+"* "+"  "*(i-2)+"*"+s+"*")
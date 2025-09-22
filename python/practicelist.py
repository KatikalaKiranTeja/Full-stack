# list = [2,3,4,6,7]
# print(list[3])

# list = [2,3,4,6,7]
# list[2]=9
# print(list)

# list = [2,3,4,6,7]
# list.append(77)
# print(list)

# list = [2,3,4,6,7]
# list[0]=23
# print(list)

# list = [2,3,4,6,7]
# list.remove(2)
# print(list)

# list = [2,3,4,6,7]
# list.pop(3)
# print(list)

# list = [2,3,4,6,7]
# print(len(list))

# list = [2,3,4,6,7]
# if 5 in list:
#     print("yes 5 is in list")
# else:
#     print("not in list")

# list = [2,3,4,6,7]
# for i in list:
#     print(i)

# list = [2,3,4,6,7]
# list.sort()
# print(list)

# list = [2,36,48,6,7]
# list.sort(reverse=True)
# print(list)

# list = [2,36,48,6,7]
# reversed_list=list[::-1]
# print(reversed_list)

# list = [2,3,4,6,7]
# copy = list[:]
# print(copy)

# list = [2,3,4,6,7]
# copy_list = list.copy()
# print(copy_list)

# list = [2,3,4,6,7,2,2,2]
# list.clear()
# print(list)

# list = [2,3,4,6,7,2,2,2]
# print(list.count(2))

# list = [2,3,4,6,7,2,2,2]
# print(list.index(7))

# l1 = [2,3,4,6,7,2,2,2]
# l2 = [1,2,3,4]
# l = l1+l2
# print(l)

# list = [2,3,4]
# list1 = list*3
# print(list1)

# l1 = [2,3,4,6,7,29,2,26]
# l = l1[1::2]
# print(l)

# l1 = [2,3,4,6,7,8,2,21]
# l = l1[2:6]
# print(l)

# l1 = [2,3,4,6,7,8,2,21]
# if all(i > 0 for i in l1):
#     print("positive")
# else:
#     print("Negative")

l1=["hi","hello","how","are","you"]
result = ','.join(l1)
print(result)

l1=[1,3,44,55,23,545,465]
maximum=max(l1)
print(maximum)

l1=[1,3,44,55,23,545,465]
minimum=min(l1)
print(minimum)

l1=[1,3,44,55,23,545,465]
total=sum(l1)
print(total)

l1=[1,3,44,55,23,545,465]
total = [x**2 for x in l1]
print(total)

l1=[1,3,44,55,23,545,465]
even=[x for x in l1 if x%2==0]
print(even)

l1=[1,3,44,55,23,545,465]
odd =[x for x in l1 if x%2 !=0]
print(odd)

"""Duplicates"""

l1 = [1, 3, 44, 55, 23, 545, 465, 3, 55, 1]
seen = set()
duplicates = set()
for item in l1:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print("Duplicates:", list(duplicates))

"""Remove Duplicates in a List"""
l1 = [1, 3, 44, 55, 23, 545, 465, 3, 55, 1]
seen = []

for item in l1:
    if item not in seen:
        seen.append(item)
print( list(seen))

l1 = [1, 3, 44, 55, 23, 545, 465, 3, 55, 1]
unique = list(set())
print(unique)

list = []
if not list:
    print("empty")

n=5
zeros=n*0
print(zeros)

list=[10,20,30,40,50]
i,j=1,3
list[i],list[j] = list[j],list[i]
print(list)

list=[10,20,30,40,50]
last =list[-1]
print(last)

text = "hello"
char_list = list(text)
print(char_list)

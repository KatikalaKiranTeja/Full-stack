#-->Create a list of string using comprehensions
str = "Welcome"
op = [x for x in str]
print(op)

# str = "Welcome"
op = [x+'-hello' for x in str]
print(op)

# #-->Create a list of num from(1 to 10) using comprehensions
op=[x for x in range(1,11)]
print(op)

# #-->Square of a num
op=[x*2 for x in range(1,11)]
print(op)

# #-->Create a list of even numbers from 1 to 10
op=[x for x in range(1,11) if x%2==0 ]
print(op)

# #-->Create a num of list from given list with multipy 2 for every even number
ip=[1,4,7,9,11,13,24,56,108,234,125]
op=[x*2 for x in ip if x%2==0 ]
print(op)


#-->Convert all to uppercase using list comprehension
fruits = ["apple", "banana", "cherry"]
op=[x.upper() for x in fruits]
print(op)

#-->Get numbers divisible by both 3 and 5
nums = list(range(1, 51))
op=[x for x in nums if x%3==0 or x%5==0]
print(op)

nums = list(range(1, 51))
op=[x for x in nums if x%3==0 and x%5==0]
print(op)

#-->Use list comprehension to flatten it into: [1, 2, 3, 4, 5, 6]
matrix = [[1, 2], [3, 4], [5, 6]]
op=[x for rows in matrix for x in rows] 
print("Flattened matrix:",op)

#-->From 1 to 10, create a list of tuples: (number, number squared)
num = tuple(range(1,10))
op=[(x,x*2) for x in num ]
print(op)

#-->Reverse all words in a list
words = ["python", "code", "chat"]
op=[x[::-1] for x in words ]
print(op)

#-->Use list comprehension to find common elements
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
op=[x for x in a if x in b]
print("Common elements :",op)

#-->Extract all vowels into a list
text = "comprehensions"
vowels = [x for x in text if x in "aeiou"]
print("Vowels are :",vowels)

#-->Replace all negative numbers with 0
nums = [4, -1, 2, -3, 0
op=[x if x>=0 else 0 for x in nums ]
print("Updates list :",op)


#-->find factorial of num using comprehensions
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
op=[factorial(n) for n in range(1,6)]
print(op)






















# num =0
# while num<11:
#     print(num)
#     num+=1
#-->Factorial of a number using while loop
#   
# num=5
# fact=1
# temp = num
# while temp>0:
#     fact *=temp
#     temp -=1
# print(f"factorial of {num} is {fact}")

#-->The program should repeatedly ask the user for a number and calculate its factorial until the user enters a negative number to stop.

# while True:
#     num =int(input("Enter a number :"))
#     if num<0:
#         print("program stopped")
#         break
#     factorial=1
#     i=1
#     while i<=num:
#         factorial *= i
#         i += 1
#     print(f"factorial of {num} is {factorial}")


#-->Fibonacci series using while loop

# n=int(input("Enter the number of Fibonacci terms:"))
# a,b=0,1
# count =0
# while count < n:
#     print(a, end=" ")
#     a,b=b, a+b
#     count +=1


#-->Reverse a number using while loop

# num=int(input("Enter number :"))
# rev=0
# while num>0:
#     id = num%10
#     rev = (rev*10)+id
#     num = num//10
# print(rev)


#-->Sum of digits
# num=12345
# sum=0
# while num>0:
#     sum += num%10
#     num = num//10
# print(sum)

#-->Multiplication table for a given number using while loop

def multiplication_table():
    n = int(input("Enter a number: "))
    count = 1
    print(f"Multiplication Table for {n}:")
    while count <= 10:
        print(f"{n} x {count} = {n * count}")
        count += 1

multiplication_table()

#-->Count the Vowels in a String using while loop
def count_vowels():
    string = input("Enter a string: ")
    vowels = "aeiou"
    count = 0
    index = 0
    while index < len(string):
        if string[index].lower() in vowels:
            count += 1
        index += 1
    print(f"Vowel count: {count}")

count_vowels()

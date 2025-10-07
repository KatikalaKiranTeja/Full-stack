score = int(input("Enter the student's score (0-100): "))

# Check and print the grade
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
elif 0 <= score < 60:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")


#==>check if leap year or not

year = int(input("Enter Year ="))
if (year%4==0 and year%100==0) or year%400==0:
    print("Leap year")
else:
    print("Not a leap year")





def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Get user input
num = int(input("Enter a number: "))

# Decision logic
if num % 2 == 0:
    print("Even")
elif is_prime(num):
    print("Odd Prime")
else:
    print("Odd Composite")

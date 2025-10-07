#==> write a program to check Armstrong number
#==> It is in while loop

# num = 153
# num_str=str(num)
# num_digit = len(num_str)
# sum_of_power = 0
# temp_num = num

# while temp_num>0:
#     digit = temp_num%10
#     sum_of_power += digit ** num_digit
#     temp_num //=10
# if sum_of_power == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not an Armstrong number")


# num=153
# num1=len(str(num))
# sum=0
# temp=num
# while temp>0:
#     digit=temp%10
#     sum += digit**num1
#     temp //=10
# if sum==num:
#     print(f"{num} is an Armstrong number ")
# else:
#     print(f"{num} is not an Armstrong number")


#==> In for loop

# num=153
# power=len(str(num))
# total=0
# for digit in str(num):
#     total += int(digit)**power

# if total == num:
#     print(f"{num} is an Armstrong number")
# else:
#     print(f"{num} is not Armstrong number")


#==>  It is in functions
def is_armstrong(num):
    num1=len(str(num))
    total=sum(int(digit)**num1 for digit in str(num))
    return total == num
print(is_armstrong(153))
print(is_armstrong(9474))
print(is_armstrong(944))

def fact(a):
    if a==0 or a==1:
        return 1
    else:
        return a*fact(a-1)
fact(5)
print(f"factotail of 5 is {fact(5)}")


def is_palindrome(str):
    if str==str[::-1]:
        return ("palindrome")
    else:
        return ("not a palindrome")

print(is_palindrome("madam"))



def custom_power(base,exponent):
    result=1
    for i in range(exponent):
        result *= base
    return result
print(custom_power(2,5))
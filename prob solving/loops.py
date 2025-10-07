for i in range(1,50):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Bizz")
    else:
        print(i)


num=121
sum=0
while num>0:
    sum +=num%10
    num =num//10
print(sum)


num=5
for i in range(1,11):
    print(f"{num}x{i}={num*i}")
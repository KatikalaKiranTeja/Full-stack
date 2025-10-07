class calculator:
    
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
    def reminder(self,a,b):
        return a%b
print("Types of operations")

print(" 1.add \n 2.sub \n 3.mul \n 4.div \n 5.reminder \n 6.exit")

while True:
    cal1=calculator()
    n=int(input("Enter option:"))
    if n==6:
        break
    elif n==1:
        a,b=map(int,input("Enter values :").split())
        print(cal1.add(a,b))
    elif n==2:
        a,b=map(int,input("Enter values :").split())
        print(cal1.sub(a,b))
    elif n==3:
        a,b=map(int,input("Enter values :").split())
        print(cal1.mul(a,b))
    elif n==4:
        a,b=map(int,input("Enter values :").split())
        print(cal1.div(a,b))
    elif n==5:
        a,b=map(int,input("Enter values :").split())
        print(cal1.reminder(a,b))
    else:
        print("Please enter a valid option")



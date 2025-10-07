class greeting:
    def visit(self):
        print('hello sir')
    def exit(self):
        print("thank you! visit again")
g1=greeting()
g1.visit()
g1.exit()


# if we not given the self parameter we may get this error
# typeerror: greeting.exit() takes 0  positional arguments but 1 was given

class greeting:
    def __init__(self,name):
        self.name=name
        
    def visit(self,name):
        print(f'hello sir {name}')
    def exit(self):
        print(f"thank you!{self.name} visit again")
g1=greeting("kiran")
g1.visit("teja")
g1.exit()



class calsi:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def addition(self,a,b):
        return a+b
    def substraction(self):
        return self.first-self.second
calsi1=calsi(100,99)
print(calsi1.addition(10,19))
print(calsi1.substraction())

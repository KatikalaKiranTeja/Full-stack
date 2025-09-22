#scope-->It ia nothing but if/accessibility of a variable
#-->we have different types of scope
# 1.Global 2.Local/function 3.enclosed scope

x="MaheshBabu"
def tollywood():
    print(f"{x} is accessible in tollywood")
def bollywood():
    print(f"{x} is accessible in bollywood")
#function inside function
    def localwood():
        print(f"{x} is accessible in localwood")
    localwood()
tollywood()
bollywood()
print(f"{x} can access globally")    

#=========================================================

x="MaheshBabu"
def tollywood():
    print(f"{x} is accessible in tollywood")
    x1="Tillu"  # x1 is having function scope/local scope

def bollywood():
    print(f"{x} is accessible in bollywood")
    x2="Ranbeer Kapoor"
#function inside function
    def localwood():
        print(f"{x} is accessible in localwood")
        print(x2)
        x3="Sampoornesh Babu" #Enhanced scope
        print(x3)
    localwood()
    #print(x3)
# we cannot access outside of enclosed function
tollywood()
bollywood()
print(f"{x} can access globally")    

#===============================================

# Global Scope: A variable with global scope is accessible from anywhere in the program.
#                It's declared outside of any function or block

#Local Scope: A variable with local scope is only accessible within the specific function, 
#             block, or method where it's defined.

# This is a GLOBAL variable.
# It is defined outside any function, making it accessible everywhere.

x="MaheshBabu"
def tollywood():

# The 'tollywood' function can access the global variable 'x'.
    print(f"{x} is rule tollywood")

def bollywood():
# This is a LOCAL variable.
# It is defined inside this function and is only accessible here.    
    x3="Hrithik Roshan"
    print(f"{x3} rule bollywood")

tollywood()
bollywood()
print(f"{x} will also rule golbally")

#========================================================

# This is a global variable. It can be accessed anywhere.
x1 = "I am a global variable." 
x3 = " I am also global variable"

def my_combined_scope():
  # This is a local variable. It is only accessible within this function.
  x3 = "I am a local variable." 

  print("--- Inside the function ---")
  print(f"Global variable x1: {x1}")
  print(f"Local variable x3: {x3}")
  print("--------------------------")

# Call the function to show the variables in action.
my_combined_scope()

# Now, we try to access the variables outside the function.
print("--- Outside the function ---")
print(f"Global variable x1: {x1}")
print(x3)

def keyword():
    x="Hello" #-->this is local variable
    def keyword1():
        x1="Hii" #-->this is non local
        print(x1)
    keyword1()
    print(x)
keyword()


x=50 
def demo():
    global x
    x=35
    print(x)
demo()
print(x)

a=125
def outer():
    a=12 
    def inner():
        nonlocal a
        a=15
        print(a,"printing a in inner function")
    inner()
    print(a,"printing a in outer function")
outer()
print(a)
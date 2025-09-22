name="kiranteja"
print(name)
print(name[0])
print(name[-1])

name="kiran"
name1="teja"
print(name+" "+name1)

name="kiran"
print(name*3)

name="kiranteja"
print(name[0:6])

name="kiranteja"
print(name[::-1])

substring="kiran teja"
string="kiran teja"
if substring in string:
    print("it exists")
else:
    print("not exists")

string="kiran teja"
print(len(string))

string="kiran teja"
print(string.upper())

string="KIRAN TEJA"
print(string.lower())

string="kiran teja"
capitalize=string[0].upper() + string[1:]
print(capitalize)

string="kiran teja"
print(string.title())

string="    kiran teja"
print(string.lstrip())

string="kiran teja  "
print(string.rstrip())

string="  kiran teja   "
print(string.strip())

string="kiran teja"
print(string.replace(" ",","))

string="kiran teja"
print(string.count('a'))

string="kiran teja"
print(string.get())

string="kiran teja"
print(string.find("kiran"))

string="kiran teja"
print(string.rfind("t"))

string="kiran teja"
substring=string.find("teja")
print(substring)

string="My name is kiran teja "
string.split()
print(string.split())

string="My name is kiran teja "
joined=" ".join(string)
print(joined)

string="Hello My name is kiran teja "
if string.startswith("Hello"):
    print("hello is in string")

string="Hello My name is kiran teja "
if string.endswith("teja"):
    print("teja is in string")
else:
    print("not in string")


string="54"
if string.isdigit():
    print("yes")

string="A"
if string.isalpha():
    print("Yes it is alpha")

string="A12B34"
if string.isalnum():
    print("Yes it is alphanumeric")
else:
    print("it is not")

value="h"
ascii_value=ord(value)
print(ascii_value)

ascii_value=65
char=chr(ascii_value)
print(char)

string="Hello!"
swaped=string.swapcase()
print(swaped)

string="Hello Worls!"
total_count=len(string.split())
print(total_count)

string="Hello Worls! is the basic program"
total_sentence_count=len(string.split())
print(total_sentence_count)

string="Hello"
text=string.split()
print(text)

list=['hey','hi',"hello"]
string=' '.join(list)
print(string)

string="cat"
padding=string.rjust(10,'*')
print(padding)

string="hat"
align_center=string.center(10,'-')
print(align_center)

string="hello world!"
print(f"basic program is {string}")

name = "Alice"
age = 30
formatted = "My name is %s and I am %d years old." % (name, age)
print(formatted) 




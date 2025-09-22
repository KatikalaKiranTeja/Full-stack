x=(1,2,3,4,5)
print(x)

x=(1,2,3,4,5)
print(x[2])

x=(1,2,3,4,5)
print(x[:-2])

x=(1,2,3,4,5)
if 3  in x:
    print("3 is exists")
else:
    print("doesnot exists")

x=(1,2,3,4,5)
y=(2,5,6,8,3)
z=x+y
print(z)

x=(1,2,3,4,5)
y=x*3
print(y)

x=(1,2,3,4,5)
print(len(x))

x=[1,2,3,4,5]
y=tuple(x)
print(y)

x=(1,2,3,4,5)
y=list(x)
print(y)

x=[1,2,3,4,5]
y=x.index(2)
print(y)

x=(1,2,3,4,5,5,7,5)
print(x.count(5))

x=(("kiran",21,"gdv"),("vimal",20,"gdv"),("vamsi",21,"gdv"))
kiran_age=x[0][1]
vimal_vil=x[1][2]
print("Kiran age is :" ,kiran_age)
print("vimal lives in :" ,vimal_vil)

my_tuple = (1, 2, 3, 4, 5)
if all(isinstance(x,int) for x in my_tuple):
    print("All are integers")
else:
    print("not integers")

x=("kiran",21,"gdv")
name,age,vil=x
print(name)
print(age)
print(vil)

x=(1,2,3)
y=(4,5,6)
x,y=y,x
print(x,y)

x=(1,5,9,11,33,45,11,2)
maximum=max(x)
print(maximum)

x=(1,2,3)
for i in x:
    print(i)

x=(1,5,9,11,33,45,11,2)
minimum=min(x)
print(minimum)

x=(1,5,9,11,33,45,11,2)
sorted_tuple=sorted(x)
print(sorted_tuple)

x=(1,2,3)
y=(4,5,6)
merge_tuple=x+y
print(merge_tuple)

for i in range(2,10,2):
    print(i)

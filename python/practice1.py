#Calculate the area of a square

def area_of_square():
    area=side*side
    print(area)
    return area
side=5
area_of_square()

#Calculate the area of a rectangle

def area_of_rectangle():
    area=(length*breadth)
    print(area)
    return area
length=25
breadth=45
area_of_rectangle()

#Calculate the area of a triangle using base and height. 

def area_of_triangle():
    area=(1/2)*length*breadth
    print(area)
    return area
length=12
breadth=25
area_of_triangle()

#Calculate the perimeter of a square

def perimeter_of_square():
    perimeter=4*side
    print(perimeter)
    return perimeter
side=24
perimeter_of_square()

#Calculate the perimeter of a rectangle. 

def perimeter_of_rectangle():
    perimeter=2*(length+breadth)
    print(perimeter)
    return perimeter
length=12
breadth=7
perimeter_of_rectangle()

#Calculate the perimeter of a triangle. 

def perimeter_of_triangle():
    perimeter=(x+y+z)
    print(perimeter)
    return perimeter
x=7
y=8
z=9
perimeter_of_triangle()

#Calculate the sum of marks in 3 subjects

def sum_of_marks(Maths, Physics, Chemistry):
    total_marks=Maths+Physics+Chemistry
    print(total_marks)
    return total_marks
sum_of_marks(55, 60, 58)

#Calculate the average of marks in 3 subjects. 

def average_of_marks():
    average=(Maths+Physics+Chemistry)/3
    print(average)
    return average
Maths = 85 
Physics = 90 
Chemistry = 88
average_of_marks()





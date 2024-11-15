class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return (self.__length * self.__width)

    def perimeter(self):
        return (2 * (self.__length + self.__width))


obj1 = Rectangle(4, 5)
print("Area is", obj1.area())
print("Perimeter is", obj1.perimeter())


################

class Student:
    __name = None
    __rollNumber = None
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


demo1 = Student()
demo1.setName("Alex")
print("Name:", demo1.getName())
demo1.setRollNumber(3789)
print("Roll Number:", demo1.getRollNumber())


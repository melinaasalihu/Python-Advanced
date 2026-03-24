class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    #getter method for name property
    @property
    def name(self):
        return self.__name

    #setter method for name property
    @name.setter
    def name(self, name):
        self.__name=name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age=age

#creating an instance of student
student1 = Student("Melina", 17)

print ("Name:", student1.name)
print("Age:", student1.age)

student1.name = "Reina"
student1.age = 16

print("updated name:", student1.name)
print("updated age:", student1.age)


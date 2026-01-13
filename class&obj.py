# class myclass():
#     x=5

# p1=myclass()
# p2=myclass()

# print(p1.x)
# print(p2.x)

#pass statement
# class person:
#     pass

#the __init__() method
#The __init__() method can have as many parameters as you need:
# class person:
#     def __init__(self,name,age,roll,gender):
#         self.name=name
#         self.age=age
#         self.roll=roll
#         self.gender=gender
    
# p1=person("avinash",21,101,"male")
# p2=person("suresh",22,102,"male")
# p3=person("radha",20,103,"female")

# print(p1.name)
# print(p1.age)
# print(p1.roll)
# print(p1.gender)

# print(p2.name,p2.age,p2.roll,p2.gender)
# print(p3.name,p3.age,p3.roll,p3.gender)

#creating a class without __init__ method
# class person:
#     pass
# p1=person()
# p1.name="avinash"
# p1.age=21
# print(p1.name,p1.age)

# default value in __init__ method
# class person:
#     def __init__(self,name,age=21):
#         self.name=name
#         self.age=age
# p1=person("avinash")
# p2=person("suresh",22)
# print(p1.name,p1.age)
# print(p2.name,p2.age)


# #self parameter

# use self to access class property
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def selffun(self):
#         print("hello my name is",self.name)

# p1=person("avinash",22)
# print(p1.age,p1.name)
# p1.selffun()

#the self parameter links the method to the specific object
#self parameter could be named anything but it should be written in the front in the parantesis
# class person:
#     def __init__(avinash,name,age):
#         avinash.name=name
#         avinash.age=age
#     def selffun(avi):
#         print(avi.name)
# p1=person("hero",22)
# p1.selffun()


#accessing properties with slef

# class person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def display(self):
#         print(f" {self.name}{self.age}{self.gender}" )

# p1=person("avinash",21,"male")
# p1.display()

#call one method from another method using self
# class person:
#     def __init__(self,name):
#         self.name=name
#     def greet(self):
#         return "hello  " +  self.name
#     def wish(self):
#         message=self.greet()
#         print(message +"! welcome to our website")
# p1=person("avinash")
# p1.wish()

# class properties

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Tobias", 25)


# del p1.age
# print(p1.name)
# print(p1.age)

# class person:
#     species="human"
#     def __init__(self,name):
#         self.name=name
# p1=person("avinash")
# p2=person("kumar")
# print(p1.name)
# print(p1.species)
# print(p2.name)
# print(p2.species)


#modifying a class property
# class person:
#     name=""
#     def __init__(self,age):
#         self.age=age
# p1=person(22)
# person.name="avinash"
# print(p1.name,p1.age)


#add a new propertyclass Person:
# class Person:
#   def __init__(self, name):
#     self.name = name

# p1 = Person("Tobias")

# p1 = Person("Tobias")
# p1.age=22
# print(p1.age)

#methods with the parameter

# class calculation:
#     def add(self,a,b):
#         return a+b
# calc=calculation()
# print("the sum is",+calc.add(5,6))class Person:
  
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def celebrate_birthday(self):
#     self.age += 1
#     print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

# p1 = Person("avinash", 21)

# p1.celebrate_birthday()

# class person:
#     def __init__(self,name,age):
#         self.name=name 
#         self.age=age
#     def __str__(self):
#         return f"{self.name} ({self.age})"

# p1=person("avi",22)
# print(p1)

# class playlist:
#     def __init__(self,name):
#         self.name=name
#         self.songs=[]
#     def add_song(self,song):
#         self.songs.append(song)
#         print(f"added:{song}")

#     def remove_song(self,song):
#         if song in self.songs:
#             self.songs.remove(song)
#             print(f"removed:{song}")
#         else:
#             print(f"{song} not found in playlist")

#     def showsong(self):
#             print(f"playlist '{self.name}' contains:")
#             for song in self.songs:
#                 print(song)
# p1=playlist("favorites")
# p1.add_song("jindagi na milegi dubara")
# p1.add_song("Stairway to Heaven")
# p1.showsong()
# p1.remove_song("Stairway to Heaven")

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)


# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year


# x = Student("Mike", "Olsen", 2024)
# print(x.graduationyear)



# 

#polymorphism
#different classes with the same method name


#inheritance class polymorphism

# class vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

#     def move(self):
#         print("move")

# class car(vehicle):
#     pass
# class boat(vehicle):
#     def move(self):
#         print("sail")
# class plane(vehicle):
#     def move(self):
#         print("fly")

# car1=car("bmw",2022)
# boat1=boat("benz",2022)
# plane1=plane("boeing",2022)

# for x in (car1,boat1,plane1):
#     print(x.brand,x.model)
#     x.move()

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age # Private property

#   def get(self):
#     return self.__age

# p1 = Person("Emil", 25)

# print(p1.get()) # This will cause an error


#set private property value
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.__age = age

#   def get_age(self):
#     return self.__age

#   def set_age(self, age):
#     if age > 0:
#       self.__age = age
#     else:
#       print("Age must be positive")

# p1 = Person("Tobias", 25)
# print(p1.get_age())

# p1.set_age(27)
# print(p1.get_age())

# class Student:
#   def __init__(self, name):
#     self.name = name
#     self.__grade = 0

#   def set_grade(self, grade):
#     if 0 <= grade <= 100:
#       self.__grade = grade
#     else:
#       print("Grade must be between 0 and 100")

#   def get_grade(self):
#     return self.__grade

#   def get_status(self):
#     if self.__grade >= 60:
#       return "Passed"
#     else:
#       return "Failed"

# student = Student("Emil")
# student.set_grade(85)
# print(student.get_grade())
# print(student.get_status())

# class Calculator:
#   def __init__(self):
#     self.result = 0

#   def __validate(self, num):
#     if not isinstance(num, (int, float)):
#       return False
#     return True

#   def add(self, num):
#     if self.__validate(num):
#       self.result += num
#     else:
#       print("Invalid number")

# calc = Calculator()
# calc.add(10)
# calc.add(5)
# print(calc.result)

# class outer:
#     def __init__(self):
#         self.name="outer class"

#     class inner:
#         def __init__(self):
#             self.name="inner class"

#         def display(self):
#             print(f"this is the {self.outer.name}")

# outer=outer()
# print(outer.name)
# inner=outer.inner(outer)
# inner.display()

#multiple inner class
# class Computer:
#   def __init__(self):
#     self.cpu = self.CPU()
#     self.ram = self.RAM()

#   class CPU:
#     def process(self):
#       print("Processing data...")

#   class RAM:
#     def store(self):
#       print("Storing data...")

# computer = Computer()
# computer.cpu.process()
# computer.ram.store()
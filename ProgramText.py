# Normal
#? Note
#* sorting
#! searching 

# U1 A6
array = [1,4,5,6,7,88,9,2,1]
# Insert 
array.append(3)
array.insert(1,99)
print("Array insert and append: ",array)
print("---")
# Delete
# remove with value
array.remove(88)
print("Remove: ", array)
array.pop()
print("Pop on the last: ", array)
del(array[3:])
print("Array delete: ",array)
array.clear()
print("Clear: ",array)
print("_ _ _ Q1 end")

#? Software Testing: the process of evaluation a software item to detect
#? differences between given input and expected output. 
#? In other words software testing is a verification and validation process.

# U1 A6
array= [1,5,8,2,10,67,20,28,11]

#! Linear search 
def linear_search(num):
    print("Linear searching Algorithm ^ v ^")
    counting = 0
    for i in range(len(array)-1):
        counting = i+1
        if array[i] == num:
            print("Found the number at: ",i+1)
            break
        print("Loading","."*counting)
linear_search(20)
print("---")

#? Verification: process=> to make sure the product behaves the way we want it to
#? Validation: process=> to make sure the product is built as per customer requirements.
#? 2 Basic of software testing=> blackbox & whitebox testing

# U1 A6
#! Binary search
array= [1,5,8,2,10,67,20,28,11]
def binary_search(num):
    print("Binary Searching Algorithm")

    for i in range(len(array)-1):
        start_num = 0
        end_num = len(array)-1
        middle_num = (start_num+end_num)/2
        if array[i] > num:
            print("Loading...",array[i])
            end_num = middle_num
        elif array[i] < num:
            print("Loading...",array[i])
            start_num = middle_num
        else:
            print("Found the number at: ",i+1)
            
binary_search(28)

#? Blackbox Testing: technique that ignores the internal mechanism of
#? the system and focus on the output
#? Whitebox Testing: technique that takes into account the internal mechanism of a system

# U1 A6
#* bubble sorting
array = [5,1,3,9,7,4,8,20,99,11,72]
def bubble_sort():
    number = 0
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            array[i],array[i+1] = array[i+1],array[i]
        else:
            array[i] = array[i]
    print(array)
bubble_sort()

#? Types of testing: Unit, Integration, Functional, System, Stress,
#? Performance, Usability, Acceptance, Regression, Beta
#? Uint=> testing  of an individual unit or group of related units
#? Integration=> testing in which a group of components are combined to produce output

# U1 A6
#* insertion sorting
array = [12,3,1,5,8]
def insertion_sort():
    print("Insertion sorting")
    print(array)
    index = 0
    temp = 0
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            
            print(array)
        print(array)
insertion_sort()

#? Functional => to ensure that the specified functionality required in the system requirements works.
#? System => to ensure that by putting the software in different environments (eg. Operating system) it still works.
#? Stress => to evaluate how system behaves under unfavorable conditions
#? Performance=> testing to assess the speed and effectiveness of the system

# U1 A6
#* selection sorting
# selection sorting
array = [12,16,11,10,14,15]
def selection_sort(lst):
    print("Selection sorting...")
    print("Before sorting:",lst)
    n = len(lst)
    for i in range(n-1):
        min = i
        print(lst)
        for j in range(i+1,n):
            if lst[j] < lst[i]:
                min = j
        lst[i],lst[min] = lst[min],lst[i]
    print("After sorting: ",lst)
selection_sort(array)

#? Usability=> to evaluate how the GUI is user-friendly? How easily can the client learn? How pleasing is it to use its design?
#? Acceptance=> to ensure that the delivered product meets the requirements
#? Regression=> testing after modification of a system, component, or a group of related units to ensure modification is working correctly
#? B3ta=> testing which is done by end users. Aim is to cover unexpected errors.

# Module import ...
from modules import addSub as sum_sub
from modules import multiDivide as multi_divide

print("Addition:",sum_sub.add(3,4))

obj = multi_divide.multi_divide()
result = obj.multiple(3,4)
print("Multiplication: ",result)

#? Encapsulation: involves bundling data and methods within a single unit, such as a class to
#? restrict direct access to variables and methods, preventing accidental modification of data.

#Encapsulation with __ to protect members
class fruit:
    def __init__(self,name,vit):
        self.name= name
        self.vit = vit
class Car:
    def __init__(self):
        self.__maxspeed = 200
        self.name = 'Lambo'
        self.updateSoftware()
        
    def drive(self):
        print("Driving at", self.__maxspeed)
    def updatedSoftware(self):
        print("Updated Software")
redCar = Car()  
redCar.drive()  # Output => Driving at 200
redCar.maxspeed = 10  # Output=> Driving at 200
redCar.drive() 
redCar.updatedSoftware() # Updated Software
print('---')        

#? Inheritance: allows to create a new class that inherits all the methods and properties from another class
#? the existing class, which serve as foundation is called parent class/ base class
#? the new class that derives from parent class is known as child class/derived class

# Inheritance
class Vehicle:
    speed = 100
    wheels = 4
    
    def start(self):
        print('Engine start')
    def drive(self):
        print('Driving')
class Car(Vehicle):  ## Inherit Vehicle(parent class)
    pass
class Bus(Vehicle):
    pass
obj1 = Car()
print(obj1.speed)
obj1.start()

obj2 = Bus()
print(obj2.wheels)
obj2.start()
print('---')

#? Method overloading: the ability to define multiple methods with the same name but different parameters in a class.
#? it offers a flexible and elegant way to handle varying parameters within a single function

# method overloading
class Calculator:
    def add(self,x=0,y=0,z=0):
        return x+y+z

cal = Calculator()
print(cal.add())   # Output=> 0
print(cal.add(2,3)) # Output => 5
print(cal.add(1,2,3)) # Output => 6
# another example
class Human:
    def sayHello(self,name= None):
        if name != None:
            print("Hello", name)
        else:
            print("Hello")
human1 = Human()
human1.sayHello("Mag Mag")
human1.sayHello()

#? Polymorphism: the ability of different object classes to share the same method name, while those
#? methods can behave differently based on which object calls them. allows us to create flexible and reusable code

# Polymorphism
class Parent:
    def show(self):
        print("inside the parent class")
class Child(Parent):
    def display(self):
        print("inside the child class")
obj = Child()
obj.display() # Output=> inside the child class
obj.show() # Output => inside the parent class



# Modular Programming:
'''
Modular programming is the process of subdividing a computer program into separate sub-programs. 
A module is a separate software component. It can often be used in a variety of applications and 
functions with other components of the system. Similar functions are grouped in the same unit of 
programming code and separate functions are developed as separate units of code so that the code 
can be reused by other applications and it is also easy to spot and fix errors. 
Example : Consider a program for a banking system. Instead of writing the entire code in a single block,
you can create modules like "Account Management," "Transaction Processing," and "User Authentication." 
Each module handles a specific aspect of the overall system.

'''

# One dimensional array:

'''
A one-dimensional array is a linear data structure that stores elements of the same data type in a contiguous block of memory. Each element in the array is identified by its index or position.
Example : 
numbers = [1, 2, 3, 4, 5]

'''
# Encapsulation: 

'''
Encapsulation in Python involves bundling data and methods within a class, and controlling access to the class's attributes.
'''

# example: encapsulation
class Car:
    def __init__(self, model, year):
        self.__model = model  # Private attribute
        self.__year = year    # Private attribute

    def start_engine(self):
        print("Engine started")
    def drive(self):
        print("Car is moving")

# Polymorphism:
'''
In object-oriented programming, polymorphism refers to a programming language's ability to process objects differently depending on their data type or class. More specifically, it is the ability to
redefine methods for derived classes. For example, given a base class shape, polymorphism enables the programmer to define different area methods for any number of derived classes, such as circles, 
rectangles and triangles. No matter what shape an object is, applying the area method to it will return the correct results. Polymorphism is considered to be a requirement of any true object-oriented programming language (OOPL).
'''
# example: polymorphism
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

# Usage
circle = Circle()
square = Square()

circle.draw()  # Outputs: Drawing a circle
square.draw()  # Outputs: Drawing a square

# Investigate the program which convert string into integer.
while True:
    # Get a string input from the user
    string_input = input("Enter a number as a string: ")

    try:
        # Convert the string to an integer
        integer_result = int(string_input)
        print("Successfully converted to an integer:", integer_result)
        break  # Exit the loop if conversion is successful
    except ValueError:
        print("Error: The input is not a valid integer.")
        try_again = input("Do you want to try again? (yes/no): ")
        if try_again.lower() != 'yes':
            break  # Exit the loop if the user does not want to try again
'''
Explanation:
1.	input("Enter a number as a string: ": This line prompts the user to enter a string, and the input is stored in the variable string_input.
2.	try:: and except ValueError: The try::block is used to attempt the conversion of the string to an integer using int(). If the conversion is successful, the code inside the try block is executed. If there's an issue (for example, if the input string is not a valid integer), a ValueError is raised, and the code inside the except block is executed.
3.	int(string_input: This is the actual conversion. The int() function attempts to convert the string to an integer.
4.	If the conversion is successful, the result is printed. If there's an error (e.g., if the user enters a string that cannot be converted to an integer), a message indicating the error is printed.
5.	I added a while True: loop to keep prompting the user until a valid integer is entered or the user chooses not to try again.
6.	Inside the except ValueError::block, after printing the error message, the program asks the user if they want to try again using input("Do you want to try again? (yes/no): ".
7.	If the user enters 'yes', the loop continues, and the user is prompted to enter a new string. If the user enters 'no' or any other response, the loop is exited.
Now, the program will keep asking the user to try again until a valid integer is entered or the user decides not to try again.

Output
Enter a number as a string: abc
Error: The input is not a valid integer.
Do you want to try again? (yes/no): yes
Enter a number as a string: 123
Successfully converted to an integer: 123

In this example:
1.	The user enters "abc," which is not a valid integer, so an error message is displayed.
2.	The program then asks, "Do you want to try again? (yes/no):" The user responds with "yes."
3.	The user is prompted to enter a new string, and this time they enter "123," which is a valid integer. The program then displays the successful conversion message and exits the loop.

'''
# Compute a program to print array in reverse order.
# Define an array
my_array = [1, 2, 3, 4, 5]

# Print the array in reverse order
reversed_array = my_array[::-1]
print("Original Array:", my_array)
print("Reversed Array:", reversed_array)
'''
In this example:
1.	The array my_array is defined with values [1, 2, 3, 4, 5].
2.	reversed_array = my_array[::-1] creates a new array that is the reverse of my_array.
3.	The program then prints both the original and reversed arrays.
When you run this program, you'll get output similar to:
Original Array: [1, 2, 3, 4, 5]
Reversed Array: [5, 4, 3, 2, 1]
This demonstrates how to print an array in reverse order in Python using slicing.

'''
# Explain with an example of method of overloading or method of overriding by using 
# modular design concept that support reusable code.

'''
Method Overloading
Method overloading refers to defining multiple methods in the same class with the same name 
but different parameters. Python does not support traditional method overloading like some other 
languages, but you can achieve similar functionality using default parameter values.
'''
class MathOperations:
    def add(self, a, b=0, c=0):
        return a + b + c

# Usage
math_ops = MathOperations()
result = math_ops.add(2, 3)
print("Result:", result)  # Output: 5

result = math_ops.add(2, 3, 4)
print("Result:", result)  # Output: 9

'''
In this example, the add method is defined with default values for parameters b and c. 
This allows you to call the method with different numbers of arguments. If only two arguments are 
provided, it defaults to treating the missing ones as zero.

Modular Design Concept for Reusable Code
Both method of overloading or method of overriding concepts support modular design by 
allowing you to encapsulate functionality into classes or modules. In method of overriding 
example, you can reuse the MathOperations class in different parts of your program without modifying the 
existing code. This promotes code reuse, maintainability, and a modular structure.

'''

# Demonstrate user defined class with an example.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! {self.name} is now {self.age} years old."

# Create an instance of the Person class
person1 = Person("Alice", 25)

# Access attributes
print(f"Name: {person1.name}")
print(f"Age: {person1.age}")

# Call methods
intro_message = person1.introduce()
print(intro_message)

birthday_message = person1.celebrate_birthday()
print(birthday_message)
'''
In this example:
•	The Person class has an __init__ method, which is the constructor. It initializes the attributes name and age when a new instance of the class is created.
•	The class has two additional methods: introduce and celebrate_birthday. The introduce method returns a string introducing the person, and the celebrate_birthday method increments the person's age and returns a birthday message.
•	An instance of the Person class, person1, is created with the name "Alice" and age 25.
•	We access the attributes (name and age) and call methods (introduce and celebrate_birthday) on the person1 object.

When this code is run, we can see output like:

...
This example demonstrates the basics of a user-defined class in Python, showing how to define attributes, methods, and create instances of the class.
'''

# Show the program to calculate the number of characters in first name of the person.
class Person:
    def __init__(self, name):
        self.name = name

    def count_characters_in_first_name(self):
        return len(self.name.split()[0])

# Create an instance of the Person class
person1 = Person("Alice Johnson")

# Call the method to count characters in the first name
character_count = person1.count_characters_in_first_name()

# Print the result
print(f"The number of characters in the first name of {person1.name} is: {character_count}")
'''
1.	Class Definition (Person)
    o	The Person class is defined with a constructor (__init__) that initializes the object with a name.
    o	The class has a method count_characters_in_first_name that calculates the number of characters in the first name.
2.	Creating an Instance (person1)
    o	An instance of the Person class is created with the name "Alice Johnson".
    o	The instance (person1) has attributes name.
3.	Calling the Method (count_characters_in_first_name)
    o	The method count_characters_in_first_name is called on the person1 instance.
    o	Inside the method, self.name.split()[0] splits the full name into words and selects the first word (the first name).
    o	len() calculates the number of characters in the first name.
4.	Printing the Result
    o	The result of the method is stored in the variable character_count.
    o	The program prints a message indicating the number of characters in the first name of the person.
When we run the program, we can see output like this.
    The number of characters in the first name of Alice Johnson is: 5

'''

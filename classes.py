# Base class 'Animal' is defined
class Animal:
    # Method for walking behavior
    def walk(self):
        print("Walking...")

# Derived class 'Dog' inherits from 'Animal'
class Dog(Animal):
    # Constructor to initialize name and age attributes
    def __init__(self, name, age):
        self.name = name  # Assign name to the Dog object
        self.age = age    # Assign age to the Dog object

    # Method specific to the Dog class
    def bark(self):
        print("woof " + self.name)  # Print a bark sound with the dog's name

# Create an instance of the Dog class with name "Roger" and age 8
roger = Dog("Roger", 8)

# Print the name of the dog
print(roger.name)  # Output: Roger

# Print the age of the dog
print(roger.age)   # Output: 8

# Call the bark method of the Dog object
roger.bark()       # Output: woof Roger

# Call the inherited walk method from the Animal class
roger.walk()       # Output: Walking...

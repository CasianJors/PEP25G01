#####################################
# ITERATORS
#####################################
# An iterator is an object that can be iterated upon (one element at a tim).
# It implements the __iter__() and __next__() methods.
# The __iter__() method returns the iterator object itself.
# The __next__() method returns the next value and raises StopIteration when there are no further items.

# Simple example with a string:
iterable_object = "Hello World"  # A string is inherently iterable

# Get the iterator from the string
iterator = iterable_object.__iter__()
# Alternatively:
iterator = iter(iterable_object)

# Using __next__() to get elements one by one
first_object = iterator.__next__()  # Should print 'H'
print(first_object)

second_object = iterator.__next__()  # Should print 'e'
print(second_object)

# Uncommenting the next lines would continue to retrieve characters:
# third_object = iterator.__next__()
# print(third_object)

# Custom iterator example using a class:
class TriangleIterator:
    """
    A custom iterator for a list of triangle sides.
    This iterator pops sides from the list until it is empty.
    """
    def __init__(self, sides: list):
        self.sides = sides

    def __iter__(self):
        # Returns the iterator object itself
        return self

    def __next__(self):
        # When no sides are left, stop iteration.
        if not self.sides:
            raise StopIteration
        # Pop a side from the list (note: this modifies the original list)
        return self.sides.pop()

class Triangle:
    """
    A Triangle class that defines a triangle by its three sides and corresponding angles.
    It implements __iter__ to allow iterating over its sides.
    """
    def __init__(self, A=1, B=1, C=1, AB=60, BC=60, CA=60):
        self.A = A
        self.B = B
        self.C = C
        self.AB = AB
        self.BC = BC
        self.CA = CA

    def __iter__(self):
        # Returns a TriangleIterator which will yield tuples containing side name and value
        return TriangleIterator([('A', self.A), ('B', self.B), ('C', self.C)])

# Create a triangle instance and iterate through its sides
t = Triangle()

for side_name, side_value in t:
    print(f'Side {side_name} has value: {side_value}')

#####################################
# GENERATORS
#####################################
# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the 'yield' statement whenever they want to return data.
# Each time next() is called on a generator, it resumes where it left off.

def my_generator(text: str):
    """
    A generator that yields each character in the input text along with its index.
    Stops iteration if it encounters an underscore ('_').
    """
    for index, data in enumerate(text):
        if data == '_':  # Stop the generator if an underscore is found
            return
        yield f"{index}: {data}"

# Example of using the generator:
result = my_generator('my_text')
print("Generator type:", type(result))
for letter in result:
    print(letter)

# Additional example: A generator for squares of numbers
def square_generator(n: int):
    """
    Yields the square of numbers from 0 up to n-1.
    """
    for i in range(n):
        yield i * i

print("Squares up to 9:")
for square in square_generator(5):
    print(square)

#####################################
# FILE OPERATIONS
#####################################
# Reading from and writing to files are essential for data storage.
# 'wt' means write text mode and 'rb' means read binary mode.

# Writing to a file using open(), write(), flush(), and close()
file = open("file.txt", 'wt')
file.write("Hello Python")
file.flush()  # Ensures that data is written to disk immediately
file.close()

# Using 'with' to automatically handle file closing.
with open("file1.txt", 'wt') as file1:
    file1.write("Hello Python with context manager!")

# Reading from a file in binary mode
with open("file1.txt", 'rb') as file2:
    result = file2.read()
    print("File read in binary mode type:", type(result))
    print("Content (in bytes):", result)

# Additional example: Appending text to a file
with open("file1.txt", 'at') as file_append:
    file_append.write("\nAppending a new line.")

#####################################
# DATETIME MODULE
#####################################
# The datetime module supplies classes for manipulating dates and times.

import datetime

# Creating specific datetime objects
date1 = datetime.datetime(2020, 10, 10)
date2 = datetime.datetime(2020, 10, 8)

# Comparison of datetime objects (later date is greater)
print(" Is date1 greater than date2?",date1 > date2)

# Get current date and time
date_now = datetime.datetime.now()
print("Current date and time:", date_now)

# Calculate the difference between two dates (result is a timedelta object)
difference = date_now - date1
print("Difference between now and date1:", difference)
print("Type of difference:", type(difference))

# Parsing a date from a string
result_date = datetime.datetime.strptime('1998-04-01', '%Y-%m-%d')
print("Parsed date from string:", result_date)

# Additional example: Formatting a datetime object as a string
formatted_date = date_now.strftime('%Y-%m-%d %H:%M:%S')
print("Formatted current date and time:", formatted_date)

#####################################
# __eq__ METHOD
#####################################
# The __eq__ method is used to define the behavior of the equality operator (==) for user-defined classes.
# By implementing __eq__, you can control when two objects of the class are considered equal.

class A:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        # Check if both name and number attributes are equal.
        return self.number == other.number and self.name == other.name

# Creating two objects of class A
a1 = A('x', 3)
a2 = A('x', 3)

# They are considered equal because their attributes are the same.
print("Are a1 and a2 equal?", a1 == a2)

# Additional example: Different objects
a3 = A('y', 4)
print("Are a1 and a3 equal?", a1 == a3)

#####################################
# LAMBDA FUNCTIONS
#####################################
# Lambda functions are small anonymous functions defined with the lambda keyword.
# They can have any number of arguments but only one expression.

# Example using a lambda function:
c = int(input("Give c (for lambda example): "))
my_sum = lambda a, b: a + b + c  # Adds a, b, and the external variable c
print("Result using lambda function:", my_sum(1, 2))

# Reassigning c to demonstrate another example using a regular function for comparison:
c = int(input("Give c (for regular function example): "))
def my_sum_regular(a, b):
    return a + b + c  # Uses the same external variable c
print("Result using regular function:", my_sum_regular(1, 2))

#####################################
# MAP FUNCTION
#####################################
# The map() function applies a given function to every item of an iterable (like a list) and returns an iterator.
# It's useful for transforming data.

c = int(input("Give c (for map example): "))

# Example using map with a lambda function:
# This lambda adds c to each element in the list.
result_map = map(lambda a: a + c, [1, 4])
print("Map result object:", result_map)
print("Mapped values as list:", list(result_map))

# Additional example: Using map with a named function to convert string numbers to integers.
def to_int(s):
    return int(s)
str_numbers = ["1", "2", "3"]
mapped_ints = map(to_int, str_numbers)
print("Converted integers using map:", list(mapped_ints))

#####################################
# FILTER FUNCTION
#####################################
# The filter() function constructs an iterator from elements of an iterable for which a function returns True.
# It’s used to filter items based on a condition.

c = int(input("Give c (for filter example): "))

# Example using filter with a lambda function:
# Here, we filter out values that, when added to c, are truthy (non-zero).
# Note: In Python, non-zero numbers are considered True.
result_filter = filter(lambda a: (a + c) != 0, [1, 4])
print("Filter result object:", result_filter)
print("Filtered values as list:", list(result_filter))

# Additional example: Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))

#####################################
# OS MODULE
#####################################
# The os module provides a way of using operating system dependent functionality.
# It allows you to interact with the underlying operating system in a portable way.

import os

# 1. Get the current working directory.
current_dir = os.getcwd()
print("Current working directory:", current_dir)

# 2. List the contents of the current directory.
# This returns a list of files and directories in the specified path.
print("Directory contents:")
print(os.listdir(current_dir))

# 3. Create a new directory.
# Check if the directory already exists before creating it.
dir_name = "example_dir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Directory '{dir_name}' created.")
else:
    print(f"Directory '{dir_name}' already exists.")

# 4. Create a file in the new directory.
# We build a file path by joining the directory name and the filename.
file_path = os.path.join(dir_name, "example.txt")
with open(file_path, "wt") as file:
    file.write("This is an example file created using the os module.")
print(f"File created at: {file_path}")

# 5. Rename the file.
# Construct a new file path and use os.rename() to rename the file.
new_file_path = os.path.join(dir_name, "renamed_example.txt")
os.rename(file_path, new_file_path)
print(f"File renamed to: {new_file_path}")

# 6. Remove the file.
os.remove(new_file_path)
print(f"File '{new_file_path}' removed.")

# 7. Remove the directory.
# The directory must be empty to be removed with os.rmdir().
os.rmdir(dir_name)
print(f"Directory '{dir_name}' removed.")

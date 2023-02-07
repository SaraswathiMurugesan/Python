#DataTypes, Variables and assisgnment

integer = 7
float = 32.5
bool = True
integer = 10

#Print Age
age = 40
print(age)

age = 50
temp = 35.8
name = 'My First project'
is_offline = False

################################################################################################################
#Finding Data Types of a variable

print('Age Data Type' ,type(age))
print('Temp Data Type' ,type(temp))
print('Name Data Type' ,type(name))
print('is_offline Data Type' ,type(is_offline))

####################################################################################################################
#DataType Conversion
#Implicit Type Conversion - Python always converts smaller data types to larger data types to avoid the loss of data.

integer_number = 123
float_number = 1.23
new_number = integer_number + float_number
# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

#Note:
# 1)We get TypeError, if we try to add str and int. For example, '12' + 23. Python is not able to use Implicit Conversion in such conditions.
# 2)Python has a solution for these types of situations which is known as Explicit Conversion.

#######################################################################################################
#Explicit Type Conversion - users convert the data type of an object to required data type.
#We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.
#This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

#Receiving Input

#birth_year = input('Enter your birth year:')
#print('Birth year:', birth_year)
#print('Data Type of num',type(birth_year))

#Convert Entered Input to integer data type
#um = int(input('Enter a number: '))
#print('Entered num:',num)

#Types of Python Operators
#Python Arithmetic Operators
a = 7
b = 2

# addition
print ('Sum: ', a + b)
# subtraction
print ('Subtraction: ', a - b)
# multiplication
print ('Multiplication: ', a * b)
# division
print ('Division: ', a / b)
# floor division
print ('Floor Division: ', a // b)
# modulo
print ('Modulo: ', a % b)
# a to the power b
print ('Power: ', a ** b)

#Python assignment operator
# assign 10 to a
a = 10
# assign 5 to b
b = 5
# assign the sum of a and b to a
a += b      # a = a + b
print(a)
# Output: 15

#Comparison Operator
a = 5
b = 2

# equal to operator
print('a == b =', a == b)
# not equal to operator
print('a != b =', a != b)
# greater than operator
print('a > b =', a > b)
# less than operator
print('a < b =', a < b)
# greater than or equal to operator
print('a >= b =', a >= b)
# less than or equal to operator
print('a <= b =', a <= b)

#Logical Operators
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

#Special operators
#Identity operators
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False

#Membership Operators
x = 'Hello world'
y = {1:'a', 2:'b'}

# check if 'H' is present in x string
print('H' in x)  # prints True
# check if 'hello' is present in x string
print('hello' not in x)  # prints True
# check if '1' key is present in y
print(1 in y)  # prints True
# check if 'a' key is present in y
print('a' in y)  # prints False

#Scope and NameSpace in Python
# global_var is in the global namespace
global_var = 10
def outer_function():
    #  outer_var is in the local namespace
    outer_var = 20
    def inner_function():
        #  inner_var is in the nested local namespace
        inner_var = 30
        print(inner_var)
    print(outer_var)
    inner_function()

# print the value of the global variable
print(global_var)

#Use of global Keyword in Python
# define global variable
global_var = 10
def my_function():
    # define local variable
    local_var = 20
    # modify global variable value
    global global_var
    global_var = 30

# print global variable value
print(global_var)
# call the function and modify the global variable
my_function()

# print the modified value of the global variable
print(global_var)

# call the outer function and print local and nested local variables
outer_function()

#Python If Statement
number = 10
# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')

#if else statement
number = 10
if number > 0:
    print('Positive number')
else:
    print('Negative number')

print('This statement is always executed')

#if...elif...else Statement
number = 10
if number > 0:
    print("Positive number")
elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')

#Nested if Statement
number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
        print('Number is 0')

    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive

#Loops
#For Loop
languages = ['Swift', 'Python', 'Go', 'JavaScript']

# access items of a list using for loop
for language in languages:
    print(language)

#for Loop with range()
# use of range() to define a range of values
values = range(4)
# iterate from i = 0 to i = 3
for i in values:
    print(i)

#In Python, we can use for loop to iterate over a range. range() is a inbuilt function

#for loop with else
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

#Here, the for loop prints all the items of the digits list. When the loop finishes, it executes the else block and prints No items left.
#Note: The else block will not execute if the for loop is stopped by a break statement

#while loop
#1)
# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i = i + 1

#2) Example
# program to calculate the sum of numbers
# until the user enters zero

total = 0
#number = int(input('Enter a number: '))
# add numbers until number is zero
while number != 0:
    number = int(input('Enter a number: '))
    total += number  # total = total + number

    # take integer input again
    #number = int(input('Enter a number: '))

print('total =', total)

#While loop with else
#Example 1)
counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

#Example 2)
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

#Notes: for Vs while loops

# this loop is iterated 4 times (0 to 3)
#for i in range(4):
   # print(i)

#while condition:
    # run code until the condition evaluates to False

#break and continue
#break Statement - The break statement is used to terminate the loop immediately when it is encountered.
for i in range(5):
    if i == 3:
        break
    print(i)

#break Statement with while Loop
i = 1

while i <= 10:
    print('6 * ', (i), '=', 6 * i)
    if i >= 5:
        break
    i = i + 1

#continue statement - The continue statement is used to skip the current iteration of the loop and the control flow of the program goes to the next iteration.

#continue Statement with for Loop
for i in range(5):
    if i == 3:
        continue
    print(i)

# continue Statement with while Loop - to print odd numbers from 1 to 10
num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)

#pass statement
#The pass statement is a null statement which can be used as a placeholder for future code.
#Suppose we have a loop or a function that is not implemented yet, but we want to implement it in the future. In such cases, we can use the pass statement.

n = 10
# use pass inside if statement
if n > 10:
    pass

print('Hello')

#Use of pass Statement inside Function or Class
def function(args):
    pass

class Example:
    pass

#Python Function

#Types -
# 1) Standard Library Functions
# 2) User defined functions

#Function syntax
#def function_name(arguments):
    # function body
#return

# 1) Example 1
#Function definition
def greet():
    print('Hello World!')
#calling the functin
greet()
print('outside function')

#Function Arguments

# 1) function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ",sum)

# function call with two values
add_numbers(5, 4)

# 2) Function return Type
# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)
print('Square:',square)

#python library functions
#In Python, standard library functions are the built-in functions that can be used directly in our program. For example,

    #1)print() - prints the string inside the quotation marks
    #2)sqrt() - returns the square root of a number
    #3)pow() - returns the power of a number
#These library functions are defined inside the module. And, to use them we must include the module inside our program.

import math
# sqrt computes the square root
square_root = math.sqrt(4)
print("Square Root of 4 is",square_root)
# pow() comptes the power
power = pow(2, 3)
print("2 to the power 3 is",power)

#) Benefits of Using Functions
#1) Code Reusable - We can use the same function multiple times in our program which makes our code reusable.

# function definition
def get_square(num):
    return num * num

for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)

#In the above example, we have created the function named get_square() to calculate the square of a number. Here, the function is used to calculate the square of numbers from 1 to 3.
#Hence, the same method is used again and again.

#Python Function Arguments: Positional, Keywords and Default

#Function Arguments
def add_numbers(a,b):
    sum = a+b
    print('Sum:',sum)

add_numbers(2, 3)

#Function Argument with Default Values
print('Function Argument with Default Values - START')
def add_numbers(a=7,b=8):
    sum = a+b
    print('Sum:',sum)

add_numbers(2,3)
add_numbers(a=2)
add_numbers()

print('Function Argument with Default Values - END')

#Keyword Argument
print('Keyword Argument - START')
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Raja', first_name = 'Dinesh')
print('Keyword Argument - END')

#Function With Arbitrary Arguments
print('Function With Arbitrary Arguments - START')
def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num
    print("Sum = ", result)
# function call with 3 arguments
find_sum(1, 2, 3)
# function call with 2 arguments
find_sum(4, 9)

#Sometimes, we do not know in advance the number of arguments that will be passed into a function.
# To handle this kind of situation, we can use arbitrary arguments in Python.
#Arbitrary arguments allow us to pass a varying number of values during a function call.
#We use an asterisk (*) before the parameter name to denote this kind of argument.
print('Function With Arbitrary Arguments - END')

#Recursive Function

print('Recursive Function - START')
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))

#Note: Our recursion ends when the number reduces to 1. This is called the base condition.
#Every recursive function must have a base condition that stops the recursion or else the function calls itself infinitely.
#Python interpreter limits the depths of recursion to help avoid infinite recursions, resulting in stack overflows.
#By default, the maximum depth of recursion is 1000. If the limit is crossed, it results in RecursionError

print('Recursive Function - END')

#Lambda Funtion - Syntax:-> lambda arguments : expression

print('Lambda Function - START')

#Add 10 to a argument
x = lambda a : a + 10
print(x(5))

#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Note: Why Use Lambda Functions?
#The power of lambda is better shown when you use them as an anonymous function inside another function.
#Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

print('Lambda Function - END')


#Variable Scope
print('variable scope - START')

#Local Variable
def greet():
    # local variable
    message = 'Hello'
    print('Local', message)
greet()

#Global variable
message = 'Hello'
def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

#nonlocal variable
#Note:nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.
#We use the nonlocal keyword to create nonlocal variables

# outside function
def outer():
    message = 'local'
    # nested function
    def inner():
        # declare nonlocal variable
        nonlocal message
        message = 'nonlocal'
        print("inner:", message)
    inner()
    print("outer:", message)
outer()

#there is a nested inner() function. We have used the nonlocal keywords to create a nonlocal variable.
#The inner() function is defined in the scope of another function outer().
#Note : If we change the value of a nonlocal variable, the changes appear in the local variable.
print('variable scope - END')

#Numbers
print('Numbers - START')
#The number data types are used to store the numeric values.
#Python supports integers, floating-point numbers and complex numbers. They are defined as int, float, and complex classes in Python.
    #int - holds signed integers of non-limited length.
    #float - holds floating decimal points and it's accurate up to 15 decimal places.
    #complex - holds complex numbers.

#Numeric Data Type

#Integers and floating points are separated by the presence or absence of a decimal point. For instance,
#5 is an integer
#5.42 is a floating-point number.
#Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.
#We can use the type() function to know which class a variable or a value belongs to.

num1 = 5
print(num1, 'is of type', type(num1))
num2 = 5.42
print(num2, 'is of type', type(num2))
num3 = 8+2j
print(num3, 'is of type', type(num3))

#Number Systems
#The numbers we deal with every day are of the decimal (base 10) number system.
#But computer programmers need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.
#In Python, we can represent these numbers by appropriately placing a prefix before that number. The following table lists these prefixes.

    #Number System   -- Prefix
        #Binary       -- 0b or 0B
        #Octal	     -- 0o or 0O
        #Hexadecimal	 -- 0x or 0X

print(0b1101011)  # prints 107
print(0xFB + 0b10)  # prints 253
print(0o15)  # prints 13

#Type conversion
num1 = int(2.3)
print(num1)  # prints 2
num2 = int(-2.8)
print(num2)  # prints -2
#num3 = float(5)
#print(num3) # prints 5.0
num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

#Random Module
import random
print(random.randrange(10, 20))
list1 = ['a', 'b', 'c', 'd', 'e']
# get random item from list1
print(random.choice(list1))
# Shuffle list1
random.shuffle(list1)
# Print the shuffled list1
print(list1)
# Print random element
print(random.random())

#Math Module
import math

print(math.pi)
print(math.cos(math.pi))
print(math.exp(10))
print(math.log10(1000))
print(math.sinh(1))
print(math.factorial(6))

#List
print('List - START')
# A list with 3 integers
numbers = [1, 2, 5]
print(numbers)

# empty list
my_list = []
# list with mixed data types
my_list = [1, "Hello", 3.4]

#Python List Elements
#Indexing
languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[0])   # Python
# access item at index 2
print(languages[2])   # C++

#Negative indexing - Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last item and so on.
#Note: If the specified index does not exist in the list, Python throws the IndexError exception.
languages = ["Python", "Swift", "C++"]
# access item at index 0
print(languages[-1])   # C++
# access item at index 2
print(languages[-3])   # Python

#Slicing of a Python List
#In Python it is possible to access a section of items from the list using the slicing operator :, not just a single item.
# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']
# items from index 2 to index 4
print(my_list[2:5])
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])

#Add Elements to a Python List

#append() - adds an item at the end of the list
numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)

#Extend - add all items of one list to another
prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)
even_numbers = [4, 6, 8]
print("List2:", even_numbers)
# join two lists
prime_numbers.extend(even_numbers)
print("List after extend:", prime_numbers)

#Change List Items
#Python lists are mutable. Meaning lists are changeable. And, we can change items of a list by assigning new values using = operator
languages = ['Python', 'Swift', 'C++']
# changing the third item to 'C'
languages[2] = 'C'
print(languages)  # ['Python', 'Swift', 'C']

#Remove an Item From a List
#del() to remove one or more items from a list - deletes a item based on index.

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the second item
del languages[1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting the last item
del languages[-1]
print(languages) # ['Python', 'C++', 'C', 'Java', 'Rust']
# delete first two items
del languages[0 : 2]  # ['C', 'Java', 'Rust']
print(languages)


#remove() - remove a item from a list based on the value in the list
# remove 'Python' from the list
languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
languages.remove('Python')
print(languages) # ['Swift', 'C++', 'C', 'Java', 'Rust', 'R']

#append() --> add an item to the end of the list
#extend() --> add items of lists and other iterables to the end of the list
#insert() --> inserts an item at the specified index
#remove() --> removes item present at the given index
#pop()	  --> returns and removes item present at the given index
#clear()  --> removes all items from the list
#index()  --> returns the index of the first matched item
#count()  --> returns the count of the specified item in the list
#sort()	  --> sort the list in ascending/descending order
#reverse()--> reverses the item of the list
#copy()	  --> returns the shallow copy of the list

#Iterating through a List
#for loop to iterate over the elements of a list.
languages = ['Python', 'Swift', 'C++']

# iterating through the list
for language in languages:
    print(language)

#Check if an Item Exists in the Python List - In Keyword
languages = ['Python', 'Swift', 'C++']

print('C' in languages)    # False
print('Python' in languages)    # True

#List Length
#len() function to find the number of elements present in a list.

languages = ['Python', 'Swift', 'C++']
print("List: ", languages)
print("Total Elements: ", len(languages))    # 3

#List Comprehension
#A list comprehension consists of an expression followed by the for statement inside square brackets.

#numbers = [number*number for number in range(1, 6)]
#print(numbers)
# Output: [1, 4, 9, 16, 25]

#numbers = [x*x for x in range(1, 6)]

#is equivalent to

#numbers = []
#for x in range(1, 6):
    #numbers.append(x * x)

print('List - END')

#TUPLES

print('TUPLE - START')

#A tuple in Python is similar to a list.
#The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

#Create Tuple with one element
#creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough.
#We will need a trailing comma to indicate that it is a tuple,

var1 = ("hello")
print(type(var1))  # <class 'str'>

# Creating a tuple having one element
var2 = ("hello",)
print(type(var2))  # <class 'tuple'>

# Parentheses is optional
var3 = "hello",
print(type(var3))  # <class 'tuple'>

#Access Python Tuple Elements

#We can use the index operator [] to access an item in a tuple, where the index starts from 0
#The index must be an integer, so we cannot use float or other types. This will result in TypeError.

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")

print(letters[0])   # prints "p"
print(letters[5])   # prints "a"

#Negative Indexing
#Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last item and so on

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

print(letters[-1])   # prints 'z'
print(letters[-3])   # prints 'm'

#Slicing
#We can access a range of items in a tuple by using the slicing operator colon :

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4])  #  prints ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7]) # prints ('p', 'r')
# elements 8th to end
print(my_tuple[7:]) # prints ('i', 'z')
# elements beginning to end
print(my_tuple[:]) # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

#When we slice lists, the start index is inclusive but the end index is exclusive.

#Tuple Methods

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3

#Iterating through a Tuple in Python
#use the for loop to iterate over the elements of a tuple

languages = ('Python', 'Swift', 'C++')
# iterating through the tuple
for language in languages:
    print(language)

#Check if an Item Exists in the Python Tuple
languages = ('Python', 'Swift', 'C++')

print('C' in languages)    # False
print('Python' in languages)    # True

print('TUPLE - END')

print('STRINGS - START')

#use single quotes or double quotes to represent a string in Python.

# create a string using double quotes
string1 = "Python programming"
# create a string using single quotes
string1 = 'Python programming'

# create string type variables
name = "Python"
print(name)
message = "I love Python."
print(message)

#Access String Characters in Python
#Indexing: One way is to treat strings as a list and use index values
greet = 'hello'
# access 1st index element
print(greet[1]) # "e"

#Negative Indexing: Similar to a list, Python allows negative indexing for its strings.
greet = 'hello'
# access 4th last element
print(greet[-4]) # "e"

#Slicing: Access a range of characters in a string by using the slicing operator colon :
greet = 'Hello'
# access character from 1st index to 3rd index
print(greet[1:4])  # "ell"

#Strings are immutable.That means the characters of a string cannot be changed.
#However, we can assign the variable name to a new string

message = 'Hola Amigos'
# assign new string to message variable
message = 'Hello Friends'
print(message); # prints "Hello Friends"
message = 'Hola Amigos'

#Multiline String
#We can also create a multiline string in Python. For this, we use triple double quotes """ or triple single quotes '''
# multiline string
message = """
Never gonna give you up
Never gonna let you down
"""
print(message)

#String Operations
#Compare Two Strings
#We use the == operator to compare two strings. If two strings are equal, the operator returns True. Otherwise, it returns False

str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

#Join Two or More Strings
#we can join (concatenate) two or more strings using the + operator.

greet = "Hello, "
name = "Jack"
# using + operator
result = greet + name
print(result)

# Output: Hello, Jack

#Iterate Through a Python String using for loop

greet = 'Hello'
# iterating through greet string
for letter in greet:
    print(letter)

#String Length - use the len() method to find the length of a string

greet = 'Hello'
# count length of greet string
print(len(greet))

# Output: 5

#Membership Test
#We can test if a substring exists within a string or not, using the keyword in

print('a' in 'program') # True
print('at' not in 'battle') #False

#Methods of Python String
#upper()	     - converts the string to uppercase
#lower()	     - converts the string to lowercase
#partition()	 - returns a tuple
#replace()       - replaces substring inside
#find()          - returns the index of first occurrence of substring
#rstrip()	     - removes trailing characters
#split()	     - splits string from left
#startswith()    - checks if string starts with the specified string
#isnumeric()	 - checks numeric characters
#index()	     - returns index of substring

#capitalize() - The capitalize() method converts the first character of a string to an uppercase letter and all other alphabets to lowercase

sentence = "i love PYTHON"
# converts first character to uppercase and others to lowercase
capitalized_string = sentence.capitalize()
print(capitalized_string)

# Output: I love python

#capitalize() Doesn't Change the Original String
sentence = "i am learning PYTHON."
# capitalize the first character
capitalized_string = sentence.capitalize()
# the sentence string is not modified
print('Before capitalize():', sentence)
print('After capitalize():', capitalized_string)

#center - The center() method returns a new centered string after padding it with the specified character

#The center() method takes two parameters:
#width - length of the string with padded characters
#fillchar (optional) - padding character
#Note: If fillchar is not provided, whitespace is taken as the default argument.

sentence = "Python is awesome"
# returns the centered padded string of length 20
new_string = sentence.center(20, '$')
print(new_string)

#Output : $Python is awesome$$

#center() with Default Argument

text = "Python is awesome"
# returns padded string by adding whitespace up to length 24
new_text = text.center(24)
print("Centered String: ", new_text)

#Output :Centered String:     Python is awesome

#casefold()
text = "PYTHON IS FUN"
# converts text to lowercase
print(text.casefold())

#Output :python is fun

#casefold() as an Aggressive lower() Method
#The casefold() method is similar to the lower() method but it is more aggressive.
#This means the casefold() method converts more characters into lower case compared to lower() .
#For example, the German letter ß is already lowercase so, the lower() method doesn't make the conversion.
#But the casefold() method will convert ß to its equivalent character ss

text = 'groß'
# convert text to lowercase using casefold()
print('Using casefold():', text.casefold())
# convert text to lowercase using lower()
print('Using lower():', text.lower())

#Output :
#Using casefold(): gross
#Using lower(): groß

#count() - The count() method returns the number of occurrences of a substring in the given string.

# define string
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
# print count
print("The count is:", count)

#output : The count is: 2

#Count number of occurrences of a given substring using start and end

# define string
string = "Python is awesome, isn't it?"
substring = "i"
# count after first 'i' and before the last 'i'
count = string.count(substring, 8, 25)
# print count
print("The count is:", count)

#output: The count is: 1

#endswith() - returns True if a string ends with the specified suffix. If not, it returns False

#endswith() Without start and end Parameters

text = "Python is easy to learn."
result = text.endswith('to learn')
# returns False
print(result)
result = text.endswith('to learn.')
# returns True
print(result)
result = text.endswith('Python is easy to learn.')
# returns True
print(result)

#endswith() With start and end Parameters

text = "Python programming is easy to learn."
# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 7)
print(result)
# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 7, 26)
# Returns False
print(result)
result = text.endswith('easy', 7, 26)
# returns True
print(result)

#endswith() With start and end Parameters

text = "Python programming is easy to learn."
# start parameter: 7
# "programming is easy to learn." string is searched
result = text.endswith('learn.', 1)
print(result)
# Both start and end is provided
# start: 7, end: 26
# "programming is easy" string is searched

result = text.endswith('is', 1, 21)
# Returns False
print(result)

result = text.endswith('easy', 7, 26)
# returns True
print(result)

#endswith() With Tuple Suffix - If the string ends with any item of the tuple, endswith() returns True. If not, it returns False

text = "programming is easy"
result = text.endswith(('programming', 'python'))
# prints False
print(result)
result = text.endswith(('python', 'easy', 'java'))
#prints True
print(result)
# With start and end parameter
# 'programming is' string is checked
result = text.endswith(('is', 'an'), 0, 14)
# prints True
print(result)





print('STRINGS - END')

#SETS

print('SET - START')

#we create sets by placing all the elements inside curly braces {}, separated by comma.
#A set can have any number of items and they may be of different types (integer, float, tuple, string etc.).
#But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'i', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)

#Create an Empty Set in Python

# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = { }
# check data type of empty_set
print('Data type of empty_set:', type(empty_set))
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

#Duplicate Items in a Set

numbers = {2, 4, 6, 6, 2, 8}
print(numbers)   # {8, 2, 4, 6}

#Add and Update Set Items in Python

#Sets are mutable. However, since they are unordered, indexing has no meaning.
#We cannot access or change an element of a set using indexing or slicing. Set data type does not support it.

#Add Items to a Set in Python

numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)

#Output
#Initial Set: {34, 12, 21, 54}
#Updated Set: {32, 34, 12, 21, 54}

#update() method is used to update the set with items other collection types (lists, tuples, sets, etc). For example,

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

#Remove an Element from a Set - discard() method to remove the specified element from a set.

languages = {'Swift', 'Java', 'Python'}
print('Initial Set:',languages)
# remove 'Java' from a set
removedValue = languages.discard('Java')
print('Set after remove():', languages)

#Output
#Initial Set: {'Python', 'Swift', 'Java'}
#Set after remove(): {'Python', 'Swift'}

#Built in functions in Set
#all()	      -- Returns True if all elements of the set are true (or if the set is empty).
#any()	      -- Returns True if any element of the set is true. If the set is empty, returns False.
#enumerate()  -- Returns an enumerate object. It contains the index and value for all the items of the set as a pair.
#len()	      -- Returns the length (the number of items) in the set.
#max()	      -- Returns the largest item in the set.
#min()	      -- Returns the smallest item in the set.
#sorted()	  -- Returns a new sorted list from elements in the set(does not sort the set itself).
#sum()	      -- Returns the sum of all elements in the set.


#Iterate Over a Set in Python - Use for loop

fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
    print(fruit)

#Find Number of Set Elements

even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))

#Set Operations

#Union of Two Sets
# first set
A = {1, 3, 5}
# second set
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))

#Output
#Union using |: {0, 1, 2, 3, 4, 5}
#Union using union(): {0, 1, 2, 3, 4, 5}

#Set Intersection
# first set
A = {1, 3, 5}
# second set
B = {1, 2, 3}

# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

#output
#Intersection using &: {1, 3}
#Intersection using intersection(): {1, 3}

#Difference between two sets - The difference between two sets A and B include elements of set A that are not present on set B.

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

#Symmteric difference - The symmetric difference between two sets A and B includes all elements of A and B without the common elements.

# first set
A = {2, 3, 5}

# second set
B = {1, 2, 6}

# perform difference operation using &
print('using ^:', A ^ B)

# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

#output
#using ^: {1, 3, 5, 6}
#using symmetric_difference(): {1, 3, 5, 6}

#Check if two sets are equal
# first set
A = {1, 3, 5}

# second set
B = {3, 5, 1}

# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')

#output : Set A and Set B are equal

#Set Methods

#add()	Adds an element to the set
#clear()	Removes all elements from the set
#copy()	Returns a copy of the set
#difference()	Returns the difference of two or more sets as a new set
#difference_update()	Removes all elements of another set from this set
#discard()	Removes an element from the set if it is a member. (Do nothing if the element is not in set)
#intersection()	Returns the intersection of two sets as a new set
#intersection_update()	Updates the set with the intersection of itself and another
#isdisjoint()	Returns True if two sets have a null intersection
#issubset()	Returns True if another set contains this set
#issuperset()	Returns True if this set contains another set
#pop()	Removes and returns an arbitrary set element. Raises KeyError if the set is empty
#remove()	Removes an element from the set. If the element is not a member, raises a KeyError
#symmetric_difference()	Returns the symmetric difference of two sets as a new set
#symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
#union()	Returns the union of sets in a new set
#update()	Updates the set with the union of itself and others

#Add - an element to a set
# set of vowels
vowels = {'a', 'e', 'i', 'u'}
# adding 'o'
vowels.add('o')
print('Vowels are:', vowels)
# adding 'a' again
vowels.add('a')
print('Vowels are:', vowels)

#output
#Vowels are: {'a', 'i', 'o', 'u', 'e'}
#Vowels are: {'a', 'i', 'o', 'u', 'e'}

#Add tuple to a set
# set of vowels
vowels = {'a', 'e', 'u'}
# a tuple ('i', 'o')
tup = ('i', 'o')
# adding tuple
vowels.add(tup)
print('Vowels are:', vowels)
# adding same tuple again
vowels.add(tup)
print('Vowels are:', vowels)

#output
#Vowels are: {('i', 'o'), 'e', 'u', 'a'}
#Vowels are: {('i', 'o'), 'e', 'u', 'a'}

#output
#

#copy() - returns a copy of the set.

names = {"John", "Charlie", "Marie"}
# items of names are copied to new_names
new_names = names.copy()
print('Original Names: ', names)
print('Copied Names: ', new_names)

#output
#Original Names:  {'Marie', 'John', 'Charlie'}
#Copied Names:  {'Marie', 'John', 'Charlie'}


#Copy Set using = operator
names = {"John", "Charlie", "Marie"}
# copy set using = operator
new_names = names
print('Original Names: ', names)
print('Copied Names: ', new_names)

#output
#Original Names:  {'John', 'Marie', 'Charlie'}
#Copied Names:  {'John', 'Marie', 'Charlie'}

#Add items to the set after copy()
numbers = {1, 2, 3, 4}
new_numbers = numbers
print('numbers: ', numbers)
# add 5 to the copied set
new_numbers.add(5)
print('new_numbers: ', new_numbers)

#output
#numbers:  {1, 2, 3, 4}
#new_numbers:  {1, 2, 3, 4, 5}

#clear() -removes all items from the set

# set of vowels
vowels = {'a', 'e', 'i', 'o', 'u'}
print('Vowels (before clear):', vowels)
# clear vowels
vowels.clear()
print('Vowels (after clear):', vowels)

#output
#Vowels (before clear): {'e', 'a', 'o', 'u', 'i'}
#Vowels (after clear): set()

#The difference_update() method computes the difference between two sets (A - B) and updates set A with the resulting set.

A = {'a', 'c', 'g', 'd'}
B = {'c', 'f', 'g'}
print('A before (A - B) =', A)
A.difference_update(B)
print('A after (A - B) = ', A)

#output
#Original Set = {'a', 'g', 'c', 'd'}
#A after (A - B) =  {'a', 'd'}

#discard - The discard() method doesn't return any value.
numbers = {2, 3, 4, 5}
# discards 3 from the set
numbers.discard(3)
print('Set after discard:', numbers)

#output: Set after discard: {2, 4, 5}

#discard with a non-existent item()
numbers = {2, 3, 5, 4}
print('Set before discard:', numbers)
# discard the item that doesn't exist in set
numbers.discard(10)
print('Set after discard:', numbers)

#output
#Set before discard: {2, 3, 4, 5}
#Set after discard: {2, 3, 4, 5}

#intersection_update()
A = {1, 2, 3, 4}
B = {2, 3, 4, 5, 6}
C = {4, 5, 6, 9, 10}

# performs intersection between A, B and C and updates the result to set A
A.intersection_update(B, C)
print('A =', A)
print('B =', B)
print('C =', C)

#output
#A = {4}
#B = {2, 3, 4, 5, 6}
#C = {4, 5, 6, 9, 10}

#isdisjoint() method returns True if two sets don't have any common items between them, i.e. they are disjoint. Else the returns False

A = {1, 2, 3}
B = {4, 5, 6}
C = {6, 7, 8}

print('A and B are disjoint:', A.isdisjoint(B))
print('B and C are disjoint:', B.isdisjoint(C))

#Output
#A and B are disjoint: True
#B and C are disjoint: False

# isdisjoint() with Other Iterables as Arguments

# create a set A
A = {'a', 'e', 'i', 'o', 'u'}

# create a list B
B = ['d', 'e', 'f']

# create two dictionaries C and D
C = {1 : 'a', 2 : 'b'}
D = {'a' : 1, 'b' : 2}
# isdisjoint() with set and list
print('A and B are disjoint:', A.isdisjoint(B))

# isdisjoint() with set and dictionaries
print('A and C are disjoint:', A.isdisjoint(C))
print('A and D are disjoint:', A.isdisjoint(D))

#A and B are disjoint: False
#A and C are disjoint: True
#A and D are disjoint: False

print('SET- END')


#Dictionary

#print('Dictionary - START')

#Create a dictionary in Python

capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "England": "London"}
print(capital_city)

# dictionary with keys and values of different data types
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

#output: [3: "Three", 1: "One", 2: "Two"]

#Add Elements to a Python Dictionary

capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)

#output:
#Initial Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London'}
#Updated Dictionary:  {'Nepal': 'Kathmandu', 'England': 'London', 'Japan': 'Tokyo'}

#Change Value of Dictionary - We can also use [] to change the value associated with a particular key

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
student_id[112] = "Stan"
print("Updated Dictionary: ", student_id)

#output
#Initial Dictionary:  {111: 'Eric', 112: 'Kyle', 113: 'Butters'}
#Updated Dictionary:  {111: 'Eric', 112: 'Stan', 113: 'Butters'}

#Accessing Elements from Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print(student_id[111])  # prints Eric
print(student_id[113])  # prints Butters

#Remove element from dictionary - del statement to remove an element from the dictionary.

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)

#output
#Initial Dictionary:  {111: 'Eric', 112: 'Kyle', 113: 'Butters'}
#Updated Dictionary  {112: 'Kyle', 113: 'Butters'}

#Dictionary Membership Test

#key is in a dictionary or not using the keyword in.
# Notice that the membership test is only for the keys and not for the values

# Membership Test for Dictionary Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# Output: True
print(1 in squares) # prints True
print(2 not in squares) # prints True
# membership tests for key only not value
print(49 in squares) # prints false

#Iterating Through a Dictionary
# Iterating through a Dictionary
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])

#built functions
#all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
#any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
#len()	Return the length (the number of items) in the dictionary.
#sorted()	Return a new sorted list of keys in the dictionary.
#clear()	Removes all items from the dictionary.
#keys()	Returns a new object of the dictionary's keys.
#values()	Returns a new object of the dictionary's values

#File I/OPython File Operation

#Opening Files in Python

# open file in current directory
file1 = open("test.txt")

#By default, the files are open in read mode (cannot be modified). The code above is equivalent to

file1 = open("test.txt", "r")

#Different Modes to Open a File in Python
#Mode	Description
#r	    Open a file for reading. (default)
#w	    Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
#x	    Open a file for exclusive creation. If the file already exists, the operation fails.
#a	    Open a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
#t	    Open in text mode. (default)
#b	    Open in binary mode.
#+	    Open a file for updating (reading and writing)

#few simple examples of how to open a file in different modes

file1 = open("test.txt")  # equivalent to 'r' or 'rt'
file1 = open("test.txt", 'w')  # write in text mode
file1 = open("img.bmp", 'r+b')  # read and write in binary mode


#Reading Files in Python - After we open a file, we use the read() method to read its contents

# open a file
file1 = open("test.txt", "r")
# read the file
read_content = file1.read()
print(read_content)

#output
#This is a test file.
#Hello from the test file.

#we have read the test.txt file that is available in our current directory. Notice the code,

#read_content = file1.read
#Here, file1.read() reads the test.txt file and is stored in the read_content variable.

#Closing Files in Python

#When we are done with performing operations on the file, we need to properly close the file.
#Closing a file will free up the resources that were tied with the file. It is done using the close() method in Python

# open a file
file1 = open("test.txt", "r")
# read the file
read_content = file1.read()
print(read_content)
# close the file
file1.close()

#output
#This is a test file.
#Hello from the test file.

#Exception Handling in Files


#print('Dictionary - END')

try:
    file1 = open("test.txt", "r")
    read_content = file1.read()
    print(read_content)
finally:
    # close the file
    file1.close()

#Use of with...open Syntax
#we can use the with...open syntax to automatically close the file
with open("test.txt", "r") as file1:
    read_content = file1.read()
    print(read_content)

#Note: Since we don't have to worry about closing the file, make a habit of using the with...open syntax.

#Writing to Files in Python
with open(test2.txt', 'w') as file2:
    # write contents to the test2.txt file
    file2.write('Programming is Fun.')
    fil2.write('Programiz for beginners')


#Python Directory and Files Management
#A directory is a collection of files and subdirectories. A directory inside a directory is known as a subdirectory.
#Python has the os module that provides us with many useful methods to work with directories (and files as well).

#Get Current Directory in Python
#We can get the present working directory using the getcwd() method of the os module.
#This method returns the current working directory in the form of a string

import os
print(os.getcwd())

# Output: C:\Program Files\PyScripter

#Changing Directory in Python
#In Python, we can change the current working directory by using the chdir() method.
#The new path that we want to change into must be supplied as a string to this method.
#And we can use both the forward-slash / or the backward-slash \ to separate the path elements.

import os
# change directory
os.chdir('C:\\Python33')
print(os.getcwd())

#Output: C:\Python33


# comments and Math Operator
summed = 2+3
difference = 7 - 4
divided = 1000/10
product = 7*5
exponent = 3**3
floored = 10 // 3
mod = 17 % 15


#Strings
ex_10 = "apricots"
#print(ex_10[:3])
#print(ex_10[2:5])
#print(ex_10[4:])


Penne = 16.68 * 100
ArrabittaPasta = 6.98 * 100
SubTotal = (Penne+ArrabittaPasta)/100
#print(SubTotal)

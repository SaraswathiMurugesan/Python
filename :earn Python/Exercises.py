
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

birth_year = input('Enter your birth year:')
print('Birth year:', birth_year)
print('Data Type of num',type(birth_year))

#Convert Entered Input to integer data type
num = int(input('Enter a number: '))

print('Entered num:',num)



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
print(ex_10[:3])
print(ex_10[2:5])
print(ex_10[4:])


Penne = 16.68 * 100
ArrabittaPasta = 6.98 * 100
SubTotal = (Penne+ArrabittaPasta)/100
print(SubTotal)

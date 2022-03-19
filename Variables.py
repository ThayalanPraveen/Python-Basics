# Types of variables : Integers, Strings, boolean & float
# Variable names cannot start with a number and are case sensitive

name = 'Praveen'  # string var
age = 18  # Integer var

# User input
x = input('prompt ')

# Operators

print(64/10)  # Full division
print(64//10)  # Whole number division

# Modulus operator is the % sign : returns the remainder after division
print(5 % 2)  # Should return 1 as 1 is the remainder

# Exponent operator is **
print(5 ** 2)  # should return 25 as 5 * 5 = 25

# Some convert functions
# int() converts numbers in string form to integer values
# sum() calculates sum of variables
# str() converts integers to string values

num1 = 10
num2 = 20
num3 = '30'

num3int = int(num3)
print(num3int + num1)  # This returns 40 as '30' is converted to 30 and added to 10

# Sum : adds numbers of an iterable

numlist = input('Enter numbers to add with a space after every number : ')
numlist = numlist.strip()  # Removes spaces in the end
numlist = numlist.split(" ")  # Creates a list from input values
print(numlist)

numlist = list(map(int, numlist))  # Converts all string values in list to integers

sum1 = sum(numlist)  # Calculates the sum of the integers in the list
print(sum1)

# str()
print(str(sum1))  # converts integers to string



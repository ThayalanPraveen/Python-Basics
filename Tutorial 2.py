# Question 2
'''
Read Num1, Num2
Set Num3 to Num1 * Num2
Write Num3
'''

# Question 3
'''
Input Num1
If (0< Num1 <10) 
    Write "blue"
Else if (10< Num1 <20) 
    Write "red"
Else if (20< Num1 <30) 
    Write "green"
Else
    Write " not a color option"
'''
# Question 4
print('Question 4')
total = 0
num_1 = int(input('input num1 : '))
num_2 = int(input('input num2 : '))
total = num_1 + num_2
print('the total is : ', total)
print('--------------')

# Question 5
print('Question 5')
'''
Read Celsius
Set Farenheit to (9/5)*Celsius + 32
Write Farenheit
'''
Celsius = int(input('Input Celsius : '))
Farenheit = (9/5)*Celsius + 32
print('the farenheit value is : ', Farenheit)
print('--------------')

print('Question 6')
value =  12.4
print(value)
print(type(value))

value=12
print(value)
print(type(value))
print('--------------')

print('Question 7')

value = 20
print('The value is ' + str(value))
print('Converted integer to string')
print('--------------')

print('Question 8')
num1 = "20"
num2 = "10"
print(num1 +num2)
print(int(num1) + int(num2))

print('first print statement returns just the strings added \nbut the second print statement converts the numbers to integers therefore adding them together mathematically')
print('--------------')

print('Question 9')

value=100
#print - version 1
print('value is')
print(value)
#print - version 2
print('value is ', value)
#print - version 3 - To suppress printing of a new line, use end=' '
print('value is ', end=' ')
print(value)
print('--------------')

print('Question 10')

print('I\'m a student ………………')
print('This is a \"great\" website')
print('\\n is the character to enter a new line')
print('This is a \"great\" website')
print('test\\test2\\answers.txt')
print('\\is called a Backslash')

print('--------------')

print('Question 11')
'''
Read BoardIndex
Read Rowcount
Read Columncount
set bombcount to 0
set x to 0
set y to 0
While (x<= Rowcount)
    While(y<= Columncount)
        If (BoardIndex(x,y) = 1)
            set bombcount to bombcount+1
Write bombcount
'''
print('--------------')

print('Question 12')

string = input('enter string : ')
string = string[::-1]
print('reversed string is : ', string)











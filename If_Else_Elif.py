'''
= this is used to assign a value
== this is used to compare with a value
=! this means not equal t0

> Greater than
< Less than
>= Greater than or equal to
<= Less than or equal to

'''

name = input('Input name: ')
num = 5

if name =='Praveen' :
    print('name is Praveen')
elif name == 'Python':
    print('name is python')
else :
    print('End of if statement')

# Chained Conditions

if name == 'Praveen' and num == 5 :
    print('name is Praveen and num is 5')
elif name == 'Python' and num ==5 :
    print('name is Python and num is 5 ')
else:
    print('Enter Praveen or Python')

# Nested if statements
if name == 'Praveen':
    if num == 5:
        print('name is Praveen and num is 5')
    else:
        print('name is Praveen but num not 5')
else:
    if num == 5:
        print('name is Python and num is 5')
    else:
        print('name is Python but num not 5')



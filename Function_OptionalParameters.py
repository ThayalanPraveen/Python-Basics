# by default test will be assigned the value of 2
def func(x, test=2):
    print(x)
    if test == 2:
        print('test is 2')
    else:
        print('test is not 2')


# This should return 'test is 2' because the value for text wasn't passed in the function, x becomes 3
func(3)

# if multiple parameters in the function have default values, it's not possible to adjust variables if we try to keep
# any variable with it's default value.



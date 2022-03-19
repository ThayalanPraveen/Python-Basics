# For loop iterates for a given range
num = 1

for x in range(10):  # range is (start:stop:step) default start is 0 and step is 1
    print(num)
    num = num+1

# Note that x stops when x becomes 10, which means the loop doesn't run for the value for x = 10

# While loop iterates until a given condition is met

num = 1

while num <= 10:  # Returns the same output as the for loop as it iterates from num=1 to num=1
    print(num)
    num = num+1
# Break functions can break the loops before the final condition is met

num = 1
for x in range(10):  # range is (start:stop:step) default start is 0 and step is 1
    print(num)
    num = num+1
    if num == 5:
        break

print('for loop stopped at num =', num)

num = 1

while num <= 10:  # Returns the same output as the for loop as it iterates from num=1 to num=1
    print(num)
    num = num+1
    if num == 5:
        break

print('while loop stopped at num =', num)


text = "String methods in python  "

# Length function len(text)
print("length of string is:", len(text))

# Strip function text.strip()
text = text.strip()
print('length of string after strip is:', len(text))


# Uppercase function text.upper
print('after Uppercase function:', text.upper())

# Split creates a list with a specified separator
print("List after split:")
list1 = text.split(' ')
print(list1)

# Slice operator  [start:stop:step] if stop is not specified it will go till end of file
print('Using the slice operator')
print(text[0:5])

#Slice with lists
list1[2:2] = "Replace"
print(list1)


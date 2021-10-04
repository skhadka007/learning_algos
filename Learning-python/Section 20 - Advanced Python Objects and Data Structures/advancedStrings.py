# Santosh Khadka

''' Capitalize, upper, lower '''
s1 = "hellO world"
s2 = "this is a full sentence"
# print(s1.capitalize())  # 1st word of string.   -> Hello world
# print(s1.upper())
# print(s1.lower())

''' Count '''
# print(s1.count('o'))    # 1
# print(s1.lower().count('o'))    # 2

''' Find '''
# print(s2.find('full'))  # 10    -> Word starts at index 10, index count starts at 0
# print(s2[10])

''' Center '''
# print(s1.center(25, 'x'))   # Want s1 to be in the center of a bunch of 'x' chars and the total length to be 25
    # Output: xxxxxxxhellO worldxxxxxxx
    
''' Tabs and New line '''
# print('hello\thi')                  # hello   hi
# print('hello\thi'.expandtabs())     # hello   hi
# print('hello\nhi')                  # line 1)hello line2)hi

''' is Alpha numeric'''
# print(s1.isalnum())         # False because of the space: ' '
# print('hello'.isalnum())    # True

''' isAplha isLower'''
# print(s1.isalpha())         # False because not all capital
# print("HELLO".isalpha())    # True
# print(s1.islower())         # False because not all lower
# print("hello".islower())    # True

''' all Space/blank '''
# print("   ".isspace())  # True
# print(s1.isspace())     # False

''' Title Case '''
# print(s1.istitle())             # False
# print("Hello World".istitle())  # True
# print(s1.title())               # 'Hello World'

''' Ends With '''
# print(s1.endswith('d'))         # True
# print('hello'.endswith('d'))    # False

''' Get first and last characters '''
# print(s1[0])    # h
# print(s1[-1])   # d

''' Split '''
# print(s1.split('o'))    # ['hellO w', 'rld']
# print(s1.split('l'))    # ['he', '', 'O wor', 'd']    # splits at every occurence
# print(s1.split('e'))    # ['h', 'llO world']

''' Partition '''
# print(s1.partition('l'))   # Will give the: head, partitioner, and tail. Will only do the first instance of the partitioner
    # ('he', 'l', 'lO world')
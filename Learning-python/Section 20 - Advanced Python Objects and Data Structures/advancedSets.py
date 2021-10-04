# Santosh Khadka

''' 
Python Set
- Wont take any duplicate items
'''

s1 = set()

s1.add(4)   # Takes only one argument
s1.add(5)
s1.add(4)  
# print(s1)   # {4, 5}  ; Did not add the duplicate 4

s1.add(1)
s1.add(3)
s1.add(10)
# print(s1)   # {1, 3, 4, 5, 10}  ; Prints in order

''' Clear '''
s1.clear()  # Makes empty set
# print(s1)

''' Copy '''
s1 = {1, 4, 5, 6, 7, 0}
# print(s1)   # {0, 1, 4, 5, 6, 7}

s2 = s1.copy()
# print(s2)   # {0, 1, 4, 5, 6, 7}

''' Difference '''
s2 = {12, 4, 5, 7, 12, 11}
# print(s1.difference(s2))    # {0, 1, 6} ; Prints what s1 has that s2 doesnt
# print(s2.difference(s1))    # {11, 12}

s1 = {1, 2, 3}
s2 = {1, 4, 5}
s1.difference_update(s2)    # No return. Done in place.
# print(s1)       # {2, 3} ; Returned all the elements that did not match with s2

''' Discard '''
s1 = {1, 2, 3, 4}
s1.discard(3)       # No error if value was not in the set.
# print(s1)   #   {1, 3, 4} 

''' Intersection : Elements that are common to all the sets '''
s1 = {1, 2, 3}
s2 = {1, 2, 4}
print(s1.intersection(s2))  # {1, 2}
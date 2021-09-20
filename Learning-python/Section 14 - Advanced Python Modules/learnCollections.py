# Santosh Khadka
# Python collections module
# Specialized container types

from collections import Counter # NOTE: make sure the file you're working on is not called "collections" !!!
from collections import defaultdict # Assigns default value in the instance a KeyError would've occured. - Prevents KEY ERROR
from collections import namedtuple  # Useful for very large tuples or when you cant remember what values are at what index. 

mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 5, 6, 7, 8, 8, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0]

# Counter is a dictionary subclass that helps count hashable objects
# Key is the object, value is the count

counted = Counter(mylist)

# print(counted.keys())
# print(counted.values())

sentence = "How many times does each word show up in this sentence with a word"
countSentece = Counter(sentence.split())    # Can also: Counter(sentence.lower().split())
# print(countSentece) # Prints from highest to lowest count: Counter({'word': 2, 'How': 1, 'many': 1, 'times': 1, 'does': 1, 'each': 1, 'show': 1, 'up': 1, 'in': 1, 'this': 1, 'sentence': 1, 'with': 1, 'a': 1})

letters = 'aaaaaaabbbbcccccdddddeeeeeeeeeee'
countLetters = Counter(letters)
# print(countLetters) # Doesnt keep original order: Counter({'e': 11, 'a': 7, 'c': 5, 'd': 5, 'b': 4})

# for key, value in countLetters.items():
#      print(key, value)
#      print(key)
#      print(value)

# key = "a"
# print("Key:", key, "Value:", countLetters[key])        # 7

# print(countLetters.keys())      # odict_keys(['a', 'b', 'c', 'd', 'e'])
# print(list(countLetters.keys()))

'''
Common patterns when using the Counter() object:

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
c += Counter()                  # remove zero and negative counts
'''
# for key in countLetters.items():
#     print(key)

# print(countLetters.values())    # odict_values([7, 4, 5, 5, 11])
# print(list(countLetters.values()))

# print(countLetters.items())     # odict_items([('a', 7), ('b', 4), ('c', 5), ('d', 5), ('e', 11)])
# print(list(countLetters.items()))

# print(list(countLetters))       # ['a', 'b', 'c', 'd', 'e']
# print(list(countLetters))

## Most Common
# print(countLetters.most_common(3))  # [('e', 11), ('a', 7), ('c', 5)]

dict1 = {'a':10}
# print(dict1)
# print(dict1['a'])
# print(dict1['z'])   # KeyError - key not in dict

def_dict = defaultdict(lambda:0)    # all default values are 0
def_dict['a'] = 1
# print(dict(def_dict))
def_dict['b']
# print(dict(def_dict))

myTuple = (10, 20, 30)
print(myTuple[0])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
husk = Dog(age=5, breed="Husky", name="Husk")
print(type(husk))
print(husk.age)
print(husk.breed)
print(husk.name)
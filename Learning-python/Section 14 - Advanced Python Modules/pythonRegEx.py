# Santosh Khadka
# Python Regular Expressions: RegEx Part 1

# if "dig" in "lets dig":
#     print(True)
# Issue here is that we need to know specifics of what we're looking for. 


'''
Regular Expressions 
RegEx allows us to search for general patterns in text data.
Ex)
    an email format: user@gmail.com
        Know to look for: "text" + "@" + "text" + ".com"
        
Python comes with built in "re" library.
    Create specialized pattern strings and then search for matches within text.
    
Goal is to understand how to look for what you need.
'''

'''
Phone number example:
(555)-555-5555

Regex pattern:
r"(\d\d\d)-\d\d\d-\d\d\d\d"
'''

# Sample Texts
text1 = "The agent's phone number is 408-555-5555. Call us back soon!"
text2 = "Here is phone 1, here is phone 2, here is phone 3."
# print('phone' in text1)   # output: True

from pdb import find_function
import re
pattern1 = 'phone'
pattern2 = 'NOT IN TEXT'
# print(re.search(pattern1, text1))       # output: '<re.Match object; span=(12, 17), match='phone'>'
# print(re.search(pattern1, text1).group()) # output: 'phone' ; To get actual result from match
# print(re.search(pattern2, text1))       # output: 'None'
match = re.search(pattern1, text1)
# print(match.span())     # output: '(12, 17)'    - location of match
# print(match.start())    # Will only get the start location of the first match (issues if more than 1 match in string)
# print(match.end())      # Will only get the end location of the first match (issues if more than 1 match in string)

matches = re.findall('phone', text2)
# print(matches)      # '['phone', 'phone', 'phone']' ; type = list
# print(len(matches)) # getting total number of matches

# for match in re.finditer('phone', text2):
#     print(match)
#     print(match.span())
#     print(match.group(), '\n')  # to get the actual text that matched

'''
                        ~~Quantifiers~~
Character 	Description 	    Example Pattern Code 	Example Match
\d 	        A digit 	        file_\d\d               file_25
\w 	        Alphanumeric 	    \w-\w\w\w 	            A-b_1           # Alphanumeric also includers special characters like: _
\s 	        White space 	    a\sb\sc 	            a b c
\D 	        A non digit 	    \D\D\D 	                ABC
\W 	        Non-alphanumeric 	\W\W\W\W\W 	            *-+=)
\S 	        Non-whitespace 	    \S\S\S\S 	            Yoyo

                        ~~Quantity~~
Character 	Description 	            Example Pattern Code 	Example Match
+ 	        Occurs one or more times 	Version \w-\w+ 	        Version A-b1_1
{3} 	    Occurs exactly 3 times 	    \D{3} 	                abc
{2,4} 	    Occurs 2 to 4 times 	    \d{2,4} 	            123
{3,} 	    Occurs 3 or more 	        \w{3,} 	                anycharacters
\* 	        Occurs zero or more times 	A\*B\*C* 	            AAACC
? 	        Once or none 	            plurals? 	            plural
'''

text1 = "The agent's phone number is 408-555-5555. Call us back soon!"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text1)
# print(phone)
# print(phone.group())

phone1 = re.search(r'\d{3}-\d{3}-\d{4}', text1)     # Easier/better to use {3} style because if youre looking for long comparisons this is much easier.
# print(phone1)
# print(phone1.group())       # If there was nothing found in search i.e 'None', then this will cause an AtrributeError

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')        # Compiles together multiple pattern codes. Used when we want to grab subgroups of our returned patterns
results = re.search(phone_pattern, text1)
# print(results.group())      # type: string
# print(results.group(1))     # Indexing starts at 1 for group
# print(results.group(2))
# print(results.group(3))
# print(results.group(4))     # results in error - IndexError

''' | = pipe operator. Or statement. '''
# print(re.search(r'cat|dog', 'The dog is here'))     # Searched for cat OR dog

''' Wildcard operator'''
# print(re.findall(r'.at', 'The cat in the hat sat there.'))      # Wildcard. Ex) '.at" Meaning a word with 1 character attached to the left of 'at'. So 3 letter words ending with 'at'
#     # Output: '['cat', 'hat', 'sat']'                           # NOTE: Also will catch spaces and other characters
# print(re.findall(r'..at', 'The cat in the hat sat there. It also went splat.'))
#     # Output: '[' cat', ' hat', ' sat', 'plat']'
# print(re.findall(r'...at', 'The cat in the hat sat there. It also went splat.'))
    # Output: '['e cat', 'e hat', 'splat']'     - Doesn't get 't sat' because it runs into 'e hat'

''' Starts and Ends with: ^ and $'''
# print(re.findall(r'^\d', 'The 2 is a number'))      # ^ means it starts with. So here it would find if starts with a number. Output: [] because it starts with 'T'
# print(re.findall(r'^\d', '2 is a number'))          # Output: ['2'] ; Type: list

# print(re.findall(r'\d$', 'The 2 is a number'))      # []
# print(re.findall(r'\d$', 'The 2 is a number. 2'))   # ['2']

''' Excluding: [] '''
phrase = "There are 3 numbers inside 34 this sentence 6."

pattern3 = r'[^\d]'
# print(re.findall(pattern3, phrase))     # Will return everything that was not a number. See output bellow
# ['T', 'h', 'e', 'r', 'e', ' ', 'a', 'r', 'e', ' ', ' ', 'n', 'u', 'm', 'b', 'e', 'r', 's', ' ', 'i', 'n', 's', 'i', 'd', 'e', ' ', ' ', 't', 'h', 'i', 's', 
#' ', 's', 'e', 'n', 't', 'e', 'n', 'c', 'e', ' ', '.']

pattern3 = r'[^\d]+'                # Use '+' to put it back together. 
# print(re.findall(pattern3, phrase))     # Output:  ['There are ', ' numbers inside ', ' this sentence ', '.'] 

phrase2 = "This is a string! But it has punctuation. How can we remove it?"
# print(re.findall(r'[^!.? ]+', phrase2))     # Removes: ! . ? ' '
    # Output: ['This', 'is', 'a', 'string', 'But', 'it', 'has', 'punctuation', 'How', 'can', 'we', 'remove', 'it']
# print(' '.join(re.findall(r'[^!.? ]+', phrase2)))   # Joining the list back together
    # Output: This is a string But it has punctuation How can we remove it
    

''' Inclusive '''
phrase_inclusive = "Only find the hyphen-words in this sentence. Like super-long if that even makes sense."
pattern_inc = r'[\w]+-[\w]+'        # lower case w.
find_hyphen = re.findall(pattern_inc, phrase_inclusive)
# print(find_hyphen)

''' Multiples '''
m1 = "Would you like some catfish?"
m2 = "Would you like some catcorn?"
m3 = "Would you like some caterpillar?"
pattern_m = r'cat(fish|corn|erpillar)'      # Find words that start with 'cat' and end with the given choices
print(re.search(pattern_m, m1).group())
print(re.search(pattern_m, m2).group())
print(re.search(pattern_m, m3).group())
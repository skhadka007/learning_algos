import unittest
import cap	# imports cap.py - the file we want to test

## Generally someone in the QA department will be writing these scripts. 

class TestCap(unittest.TestCase):	# inherit TestCase class from unittest
	"""
	Test Class for cap.py
	General structure of a test
	"""
	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)	# importing cap and running cap_text function
		self.assertEqual(result, 'Python')	# Saying that you NEED var result to always return "Python"

	def test_mult_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
	unittest.main()

###########################
## COMMAND LINE RESULTS for: return text.capitalize()

# $ python test_cap.py
# F.
# ======================================================================
# FAIL: test_mult_words (__main__.TestCap)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\PC-SK\Desktop\uDemy Python\_MY WORK\Section 10 - Errors and Exception Handling\pylint\test_cap.py", line 19, in test_mult_words
#     self.assertEqual(result, 'Monty Python')
# AssertionError: 'Monty python' != 'Monty Python'
# - Monty python
# ?       ^
# + Monty Python
# ?       ^


# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# FAILED (failures=1)
###########################

###########################
## COMMAND LINE RESULTS for: return text.title()
# $ python test_cap.py
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
###########################
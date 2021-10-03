# Santosh Khadka
import pdb  # Python DeBugger - python debugging library

x = [1, 2, 3]
y = 2
z = 3

result_1 = y + z

pdb.set_trace()     # trace should be set right before error -> Can then use terminal to debug. Use 'q' to exit. See more at: https://docs.python.org/3/
result_2 = y + x


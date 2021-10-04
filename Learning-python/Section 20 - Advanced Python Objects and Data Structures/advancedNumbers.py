# Santosh Khadka

''' Hex and Binary '''
# print(bin(33))      # 0b100001
# print(hex(33))      # 0x21
# print(hex(512))     # 0x200
# print(bin(512))     # 0b1000000000
# print(bin(512)[2:]) # 1000000000    - Removes the first 2 characters -> '0b'
# print(hex(33)[2:])      # 0x21

''' Power '''
# print(2**4)         # 16
# print(pow(2, 4))    # 16
# print(pow(2, 4, 3)) # Means: pow(x, y, z) -> (x**y) % z . Used for some efficiency cases. % means mod.

''' Odd or even '''
# print(3%2)  # 1 -> Odd ;    % means mod.
# print(4%2)  # 0 -> Even

''' Abs '''
# print(abs(-3))  # 3
# print(abs(-22)) # 22

''' Round '''
# print(round(3.1))   # 3
# print(round(3.5))   # 4
# print(round(3.9))   # 4
print(round(3.46553, 3))    # 3.466
print(int(3.9))     # 3
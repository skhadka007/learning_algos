from collections import deque

def rotLeft(a, d):
    # Write your code here
    rotated = deque(a);
    
    rotated.rotate(4)
        
    return rotated

def test(case):
    if case == 1:
        a = [1, 2, 3, 4, 5]
        d = 4
    print(rotLeft(a, d))
    
test(1)
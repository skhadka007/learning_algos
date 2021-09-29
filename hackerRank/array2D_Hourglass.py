arr = [[-1, -1, 0, -9, -2, -2],
       [-2, -1, -6, -8, -2, -5],
       [-1, -1, -1, -2, -3, -4],
       [-1, -9, -2, -4, -4, -5],
       [-7, -3, -3, -2, -9, -9],
       [-1, -3, -1, -2, -4, -5]]

# arr2=[[1, 1, 1, 0, 0, 0],
#       [0, 1, 0, 0, 0, 0],
#       [1, 1, 1, 0, 0, 0],
#       [0, 0, 2, 4, 4, 0],
#       [0, 0, 0, 2, 0, 0],
#       [0, 0, 1, 2, 4, 0]]

max = -9999999  # Because array can end up having negative numbers - always check constraints

# print(arr[0][0], arr[0][1], arr[0][2])
# print(arr[1][1])
# print(arr[2][0], arr[2][1], arr[2][2])
for x in range(4):
    for y in range(4):
        # print("x, y:", x,y)
        t1 = arr[x][y]
        t2 = arr[x][y+1]
        t3 = arr[x][y+2]
        mid = arr[x+1][y+1]
        b1 = arr[x+2][y]
        b2 = arr[x+2][y+1]
        b3 = arr[x+2][y+2]
        sum = t1+t2+t3+mid+b1+b2+b3
        print(sum);
        if (sum > max):
            max = sum

print(max)
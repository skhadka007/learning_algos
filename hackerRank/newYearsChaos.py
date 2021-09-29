def minimumBribes(q):
    # Write your code here
    # print(q)
    bribes = 0
    check = 1
    for x in range(len(q)-1, 0, -1):
        # print(x)
        if q[x] != x+1:
            if q[x-1] == x+1:
                bribes += 1
                q[x-1], q[x] = q[x], q[x-1]
            elif q[x-2]==x+1:
                bribes += 2
                q[x-2], q[x-1], q[x] = q[x-1], q[x], q[x-2]
            else:
                print("Too chaotic")
                return
    
    print(bribes)
    return bribes

'''
2 1 5 3 4
2 5 1 3 4

5 1 2 3 7 8 6 4
1 2 5 3 7 8 6 4
'''


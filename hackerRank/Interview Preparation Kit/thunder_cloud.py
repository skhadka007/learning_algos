'''
There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus or

. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered
if they are safe or if they must be avoided. 

7, 0 0 1 0 0 1 0    : 4
6, 0 0 0 1 0 0     : 3
'''

def jumpingOnClouds(c):
    jumps = 0
    step = 0
    n = len(c)
    # print("Length:", n)
    if n < 2:
        return 0
    for x in range(n):
        x = step
        # print("X:", x)
        if x+2 < n and c[x+2] == 0:
            jumps += 1
            step += 2
        elif x+1 < n and c[x+1] == 0:
            jumps += 1
            step += 1
        if step == n-1:
            break

    print(jumps)
    return jumps
       
   
jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]) 
jumpingOnClouds([0,0,0,1,0,0]) 
'''
There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is

.

Function Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

    int n: the number of socks in the pile
    int ar[n]: the colors of each sock

Returns

    int: the number of pairs

Input Format

The first line contains an integer
, the number of socks represented in .
The second line contains space-separated integers, , the colors of the socks in the pile.
'''

def sockMerchant2(n, ar):
    ar.sort()
    count = 0
    total_pairs = 0
    for x in range(n):
        if count == 0:
            count += 1
            continue
        if ar[x] == ar[x-1]:
            total_pairs += 1
            count = 0
   
    print(total_pairs)
    print(ar)

sockMerchant2(15, [6,5,2,3,5,2,2,1,1,5,1,3,3,3,5])
sockMerchant2(7, [1, 2, 1, 2, 1, 3, 2])
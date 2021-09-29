def repeatedString(s, n):
    # Write your code here
    # max = 0
    count = s.count('a')
    
    if count == 0:
        return 0
    
    len_s = len(s)
    
    if (len(s) == 1) and ('a' in s):
        return n
 
    # print(count)

    div1 = n//len_s
    count = count*div1
    # print(count)

    minus = n-(div1*len_s)
    count += (s[:minus].count('a'))
    # print(count)
    return count

def test(case):
    if case == 1:
        s = "aba"
        n = 10
    if case == 2:
        s = "x"
        n = 970770
    if case == 3:
        s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"
        n = 736778906400
        # expected output: 51574523448
    if case == 4:
        s = "a"
        n = 1000000000000
    print(repeatedString(s, n))

test(3) 
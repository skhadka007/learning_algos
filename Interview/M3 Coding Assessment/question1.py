x = 1
l = 10


def test(x, l):
    count = 0
    for a in range(x, l+1):
        if ('6' in str(a) and '8' in str(a)):
            continue
        elif ('8' in str(a)):
            count +=1
        elif ('6' in str(a)):
            count +=1   
    print(count)
    
# test(1, 10) # 2 good
# test (58, 72) # 10 good
# test(3268,3268) # 0 good
# test(361087, 773904) # 224197 good
test(92871036442, 3363728910382456)             
    # print(a%6)

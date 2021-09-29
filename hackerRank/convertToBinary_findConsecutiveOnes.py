n = 439
binary = (bin(n)[2:])
print(binary)

max = 0
count = 0
for one in binary:
    if int(one) == 1:
        count += 1
    else:
        if count > max:
            max = count
        count = 0
    if count>max:
        max = count;    
print(max)
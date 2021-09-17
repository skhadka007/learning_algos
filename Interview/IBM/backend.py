def compressedString(message):
    # Write your code here
    skip = 0
    count = 1
    output = ""
    for x in range(len(message)):
        if skip == 0:
            output += message[x]
            skip = 1
            continue
        if message[x-1] == message[x]:
            count += 1
            continue
        if message[x-1] != message[x]:
            if count != 1:
                output += str(count)
                count = 1
            output += message[x]
            continue
    if count != 1:
        output += str(count)
            
        
    print(output)
    return output

# compressedString("abaabbbc") # aba2b3c
# compressedString("wwww")

def circularArray(n, endNode):
    # Write your code here
    # n = max value
    # endNode = last node
    print(n, ", ", endNode)
    
    values = dict.fromkeys(range(1, n+1), 0)
    print(values)
    
    for index in range(len(endNode)):
        if index + 1 < len(endNode):
            start = endNode[index]
            end = endNode[index+1]
            if start <= end:
                for node in range(start, end + 1):
                    values[node] += 1
                    # print(values) 
            else:
                for node in (list(range(start, n)) + list(range(1, end+1))):
                    values[node] += 1
    print(values)
    max_value = max(values, key=values.get) # Gets max value
    print(max_value)
    return max_value

# n = 10, [1, 5, 10, 5]

def circularArray2(n, endNode):
    values = dict.fromkeys(range(1, n+1), 0)
    nodes = [];

    for index in range(endNode[0], endNode[len(endNode) - 1] + 1):
        values[index] += 1

    for index in endNode[1:len(endNode) - 1]:
        values[index] += 1

    max_value = max(values, key=values.get) # Gets max value

    return max_value

print(circularArray2(10, [1, 5, 10, 5]))
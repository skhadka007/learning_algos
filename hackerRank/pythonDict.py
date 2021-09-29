# Enter your code here. Read input from STDIN. Print output to STDOUT
# n1 = int(input())
# print(n1)
n1 = 3

from sys import stdin
phoneBook = {}
for nums in range(n1):
    data = input()
    name, number = data.split()
    # print(data, name, number)
    phoneBook[name] = number
    # print(phoneBook)

# print(phoneBook) # phoneBook = {'sam': '99912222', 'tom': '11122222', 'harry': '12299933'}

for line in stdin:
    if line == '':
        break
    else:
        line = line.strip()
        try:
            print(str(line)+"="+str(phoneBook[line]))
        except KeyError:
            print("Not found")
            
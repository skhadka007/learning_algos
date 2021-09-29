# n = int(input())
n = "Hacker Rank"
n = n.split()
odds = ""
evens = ""

text = []

for x in range(len(n)):
    text.append(n[x])

for x in range(len(text)):
    odds = ""
    evens = ""
    for y in range(len(text[x])):
        if y == 0:
            evens += text[x][y]
            continue
        if y % 2 == 0:
            # print("even:", y)
            evens += text[x][y]
        else:
            # print("odd:", y)
            odds += text[x][y]
    print(evens, odds)    

# print(splitText)
def myfunc(string1):
    newString = ''
    for num in range(0, len(string1)):  # because 2nd number will count as odd due to 0 indexing
        if num % 2 == 1:
            newString += string1[num].upper()
        else:
            newString += string1[num].lower()
    return newString

#print(myfunc("HelloWorld"))

list1 = [Australia, Singapore, Sweden, China, Netherlands, Israel, Russia, Nepal, Hong Kong, Taiwan, Norway, South Korea, Canada, India, Mexico]

print(list1)
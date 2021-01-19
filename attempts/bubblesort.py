### Bubble sort implementation in python. 

## Read from file
fileName = "pre_sort.txt"
#fileRead = open(fileName, "r+") # read and write

def read_and_append(fileName):
    file_elements = []
    
    with open(fileName) as fileRead:
        for line in fileRead:
            file_elements.append(line.rstrip('\n')) # only removes '\n'
    return file_elements

def main():
    elements = read_and_append(fileName)
    print(elements[len(elements)-1])    
    #print(len(elements))
    #print(elements[10000-1])

if __name__ == '__main__':
    main()




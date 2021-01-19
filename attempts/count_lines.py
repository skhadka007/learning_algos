## Count the number of lines in the text file - similar to counting the elements

#!! TO DO - Make this into a GUI where user can pick the file manually & output is on a result window

## File read
fileName = "pre_sort.txt"
fileRead = open(fileName, "r") # read only 

line_count = 0  # total lines
char_count = 0  # total characters
word_count = 0  # total words
elements_count = 0  # total elements. E.g) "1313 1231 3131" => 3 elements

## Line counter
def lineCounter(fileName):
    fileRead = open(fileName, "r") # read only 
    line_count = 0
    
    for lines in fileRead:
        line_count += 1
    
    fileRead.close()
    return line_count
    
## Character counter

## Word counter

## Elements counter

## Print Out
def main():
    print("Line Count: ", lineCounter(fileName))
    #print("Char Count: ", char_count)
    #print("Word Count: ", word_count)
    #print("Elements Count: ", elements_count)
    
if __name__ == "__main__":  # Will only run the stuff in function main if this file/module is being directly run. Will NOT print when being called in another module
    main()

## File Close
fileRead.close()
## SANTOSH KHADKA
## Complete-Python-3-Bootcamp/03-Methods and Functions/03-Function Practice Exercises
## Challenging Problems:

def spy_game(nums):
    '''
    SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
    '''
    check1 = False
    check2 = False
    for x in range(len(nums)):
        if nums[x] == 0 and check1 == False:
            check1 = True
            continue
        if nums[x] == 0 and check1 == True:
            check2 = True
            continue
        if nums[x] == 7 and (check1 == False or check2 == False):
            check1 = False
            check2 = False
            continue
        if nums[x] == 7 and check1 == True and check2 == True:
            return True
    return False

def count_primes(num):
    '''
    COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number.
    '''
    #count = 0
    primes = [2]
    if (num <= 1):
        return 0
    else:
        count = 3
        while count <= num:
            for y in range(3, count, 2):
                if count%y == 0:
                    count += 2
                    break
            else:
                primes.append(count)
                count += 2
        return len(primes)

def function_test(func_name):
    if "spy_game" in str(func_name):
        print(spy_game([1,2,4,0,0,7,5]))    #--> True
        print(spy_game([1,0,2,4,0,5,7]))    #--> True
        print(spy_game([1,0,2,4,0,0,5,7]))  #--> True
        print(spy_game([1,0,2,4,0,7,5,7]))  #--> True
        print(spy_game([1,7,2,0,4,5,0]))    #--> False
        print(spy_game([1,0,7,2,0,4,5,0]))  #--> False
        
    if "count_primes" in str(func_name):
        print(count_primes(100))

def main():
    #function_test("spy_game")
    function_test("count_primes")

if __name__ == "__main__":
    main()
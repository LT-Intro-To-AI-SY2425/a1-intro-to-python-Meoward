# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"
'''
Absolutely! Here are some beginner to intermediate-level Python programming challenges for you to practice:

### 1. **Fibonacci Sequence**
Write a function that returns the first `n` numbers of the Fibonacci sequence. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.

### 2. **Palindrome Checker**
Create a function that checks if a given string is a palindrome (reads the same forwards and backwards). Ignore spaces, punctuation, and capitalization.

### 3. **Prime Number Finder**
Write a function that takes a number `n` and returns a list of all prime numbers up to `n`. A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.

### 4. **Character Count**
Create a function that takes a string and returns a dictionary with the count of each character (case-insensitive). 

### 5. **Sorting a List**
Implement a function that sorts a list of numbers in ascending order without using built-in sorting functions (like `sort()` or `sorted()`). You can use any sorting algorithm you prefer (e.g., bubble sort, selection sort).

### 6. **Anagram Checker**
Write a function that checks if two given strings are anagrams (they contain the same characters in a different order). Ignore spaces and capitalization.

### 7. **Simple Calculator**
Create a simple calculator that takes two numbers and an operator (+, -, *, /) and returns the result. Handle division by zero gracefully.

### 8. **Guess the Number Game**
Implement a guessing game where the program randomly selects a number between 1 and 100, and the user has to guess it. Provide feedback if the guess is too high or too low. Count the number of attempts the user takes.

### 9. **Text Reversal**
Write a function that reverses the words in a given sentence while maintaining the original order of the words.

### 10. **Remove Duplicates**
Create a function that takes a list and returns a new list with all duplicates removed, while preserving the order of the first occurrences.

Feel free to tackle these challenges one at a time, and if you need help or hints, just ask! Happy coding!
'''
# 3 ai problems

#im going to do fibonochi (nxt number is the sum f last)
#0 1, 1, 2, 3, 5, 8, 13, 21

fib = [0,1]

for i in range(10):
    first = len(fib) -2
    second = len(fib) -1
    sum = fib[first] + fib[second]
    fib.append(sum)
print(fib)



#sort list
def theSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
   


assert theSort([3,25,3,52]) == [3,3,25,52]
print(theSort([4,3,2,1]))


#remove duplicates
def remove_duplicates(input_list):
    seen = set()
    output_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            output_list.append(item)
    return output_list


assert remove_duplicates([1, 2, 2, 3, 4, 4, 5, 1, 6]) == [1, 2, 3, 4, 5, 6]
assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
assert remove_duplicates([]) == []
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

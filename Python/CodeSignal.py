
# Exercise 1

""" xs = [()]

res = [False]*2

if xs:
    res[0] = True
    
if xs[0]:
    res[1] = True

print(res) # [True, False] """ 



# Excercise 2

""" 
import time

x = 2

y = 4

L = 5

R = 25

start_time = time.time()

if L < x**y <= R: # Winner
    print("---Time 1:  %s seconds ---" % (time.time() - start_time))



start_time = time.time()

if x**y > L and x ** y <= R:
    print("---Time 2:  %s seconds ---" % (time.time() - start_time))


start_time = time.time()

if x**y in range(L + 1, R + 1):
    print("---Time 3:  %s seconds ---" % (time.time() - start_time)) """



# Excercise 3

""" a = True

b = False

print( a == (not b))

 print( a == not b) # Correct, it doesn't work

print( not (a == b) )

print( not a == b ) """


# Excercise 4

""" 
def division(x, y):
    return x // y


print(division(17, 13))

print(division(-8,2))

print(division(5,10))

print(division(-10, -3))

print(division(15, -4)) # Correct, javascript does not rounds """



##################################

# EXCERCISE 5


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Implement a function that, given an integer n, uses a specific method on it and returns the number of bits in its binary representation.

# Note: in this task and most of the following tasks you will be given a code snippet with some part of it replaced by the ellipsis (...). Only this part is allowed to be changed.

# Example

# For n = 50, the output should be
# solution(n) = 6.

# 50_10 = 110010_2, a number that consists of 6 digits. Thus, the output should be 6.

# Input/Output

# [execution time limit] 4 seconds (py)

# [input] integer n

# A positive integer.

# Guaranteed constraints:
# 1 ≤ n ≤ 10**9.

# [output] integer

# The number of bits in binary representation of n.

# [Python 2] Syntax Tips

# # Prints help message to the console
# # Returns a string
# def helloWorld(name):
#     print "This prints to the console when you Run Tests"
#     return "Hello, " + name

##################################


""" # Solution A: own method
def solution(n):
    return len("{0:b}".format(int(n)))
    
    

# Solution B: built in method
def solution(n):
    return n.bit_length()
    

print(solution(50)) """



##################################

# EXCERCISE 6


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# It frustrates you more than you'd like to admit that the solution operator in Python can be applied to non-integer values. When you write code, you expect the result of the solution operator to always be an integer, but thanks to Python this isn't always the case.

# To fix this, you've decided to write your own solution operator as a function. Your task is to implement a function that, given a number n, returns -1 if this number is not an integer and n % 2 otherwise. It is guaranteed that if the number represents an integer, it will be written without a decimal point.

# Example

# For n = 15, the output should be
# solution(n) = 1;

# For n = 23.12, the output should be
# solution(n) = -1.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] numeric n

# A non-negative number that can be an int, a float, or a long.

# Guaranteed constraints:
# 0 ≤ n ≤ 1000.

# [output] integer

# Return n % 2 if n is an integer, otherwise return -1.

##################################


""" def solution(n):
    if type(n) == int:
        return n % 2
    else:
        return -1
    

print(solution(15)) """



##################################

# EXCERCISE 7


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# To understand how efficient the built-in Python sorting function is, you decided to implement your own simple sorting algorithm and compare its speed to the speed of the Python sorting. Write a function that, given an array of integers arr, sorts its elements in ascending order.

# Hint: with Python it's possible to swap several elements in a single line. To solve the task, use this knowledge to fill in both of the blanks (...).

# Example

# For arr = [2, 4, 1, 5], the output should be
# solution(arr) = [1, 2, 4, 5].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer arr

# Guaranteed constraints:
# 1 ≤ arr.length ≤ 500,
# -105 ≤ arr[i] ≤ 105.

# [output] array.integer

# The given array with elements sorted in ascending order.

##################################

""" def solution(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1] ,  arr [j]
            j += 1
    return arr


print(solution([2, 4, 1, 5])) """




##################################

# EXCERCISE 8


# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# Your university professor decided to have a little fun and asked the class to implement a function that, given a number n and a base x, converts the number from base x to base 16. To make things more interesting, he announced that the first student to write the solution will have to answer fewer question than the rest of the class during the final exam.

# Laughing devilishly, you asked if it was okay to use a language of your choice, and the unsuspecting professor answered "yes". It's settled then: Python is your language of choice!

# Now you're bound to win. Implement a function that, given an integer number n and a base x, converts n from base x to base 16.

# Example

# For n = "1302" and x = 5, the output should be
# solution(n, x) = "ca".

# Here's why:
# 1302_5 = 202_10 = ca_16.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string n

# A valid non-negative integer in base x. The string is guaranteed to consist of digits and lowercase English letters.

# Guaranteed constraints:
# 1 < n.length ≤ 10.

# [input] integer x

# The base of n.

# Guaranteed constraints:
# 2 ≤ x ≤ 36.

# [output] string

# The value of n in base 16. The string should contain only digits and lowercase English letters 'a' - 'f'.

##################################

""" def solution(n, x):
    return "0" if hex(int(str(n),x)).strip("0x") == "" else hex(int(str(n),x)).strip("0x")


print(solution("z",36)) """






##################################

# EXCERCISE 9

# Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
# You've just started to study impartial games, and came across an interesting theory. The theory is quite complicated, but it can be narrowed down to the following statements: solutions to all such games can be found with the mex function. Mex is an abbreviation of minimum excludant: for the given set s it finds the minimum non-negative integer that is not present in s.

# You don't yet know how to implement such a function efficiently, so would like to create a simplified version. For the given set s and given an upperBound, implement a function that will find its mex if it's smaller than upperBound or return upperBound instead.

# Hint: for loops also have an else clause which executes when the loop completes normally, i.e. without encountering any breaks

# Example

# For s = [0, 4, 2, 3, 1, 7] and upperBound = 10,
# the output should be
# solution(s, upperBound) = 5.

# 5 is the smallest non-negative integer that is not present in s, and it is smaller than upperBound.

# For s = [0, 4, 2, 3, 1, 7] and upperBound = 3,
# the output should be
# solution(s, upperBound) = 3.

# The minimum excludant for the given set is 5, but it's greater than upperBound, so the output should be 3.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer s

# Array of distinct non-negative integers.

# Guaranteed constraints:
# 0 ≤ s.length ≤ 100,
# 0 ≤ s[i] ≤ 100.

# [input] integer upperBound

# A positive integer.

# Guaranteed constraints:
# 1 ≤ upperBound ≤ 100.

# [output] integer

# Mex of s if it's smaller than upperBound, or upperBound instead.


##################################


""" def solution(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found


print(solution([0, 4, 2, 3, 1, 7],3)) """



##################################

# EXCERCISE 10

# Let's call a list beautiful if its first element is equal to its last element, or if a list is empty. Given a list a, your task is to chop off its first and its last element until it becomes beautiful. Implement a function that will make the given a beautiful as described, and return the resulting list as an answer.

# Hint: one of the features introduced in Python 3 called extended unpacking could help here.

# Example

# For a = [3, 4, 2, 4, 38, 4, 5, 3, 2], the output should be
# solution(a) = [4, 38, 4].

# Here's how the answer is obtained:
# [3, 4, 2, 4, 38, 4, 5, 3, 2] => [4, 2, 4, 38, 4, 5, 3] => [2, 4, 38, 4, 5] => [4, 38, 4].

# For a = [1, 4, -5], the output should be
# solution(a) = [4].

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.integer a

# A list of integers.

# Guaranteed constraints:
# 0 ≤ a.length ≤ 50,
# 1 ≤ a[i] ≤ 100.

# [output] array.integer

# A beautiful list obtained as described above.

##################################


def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res,*res = res
    return res


print(solution([3, 4, 2, 4, 38, 4, 5, 3, 2]))


#########################################################
#                      MEET PYTHON                      #
#########################################################




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


# Info from https://stackoverflow.com/questions/6967632/unpacking-extended-unpacking-and-nested-extended-unpacking


""" def solution(a):
    res = a[:]
    while res and res[0] != res[-1]:
        *(a,*res),c = res
    return res


print(solution([3, 4, 2, 4, 38, 4, 5, 3, 2])) """







#########################################################
#               SLITHERING IN STRINGS                   #
#########################################################

# Excercise 11



# s = 'abacaba'

# s = "abacaba"

# s = ''abacaba'' # Incorrect

# s = ""abacaba"" # Incorrect

# s = '''abacaba'''

# s = """abacaba"""




##################################

# EXCERCISE 12



# One of your friends has an awful writing style: he almost never starts a message with a capital letter, but adds uppercase letters in random places throughout the message. It makes chatting with him very difficult for you, so you decided to write a plugin that will change each message received from your friend into a more readable form.

# Implement a function that will change the very first symbol of the given message to uppercase, and make all the other letters lowercase.

# Example

# For message = "you'll NEVER believe what that 'FrIeNd' of mine did!!1",
# the output should be
# solution(message) = "You'll never believe what that 'friend' of mine did!!1".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string message

# A string consisting of English letters, whitespace characters, digits and punctuation marks.

# Guaranteed constraints:
# 1 ≤ message.length ≤ 65.

# [output] string

# Fixed message with its first letter capitalized, and all other letters converted to lowercase.

##################################


""" def solution(message):
    return message.capitalize()


print(solution("you'll NEVER believe what that 'FrIeNd' of mine did!!1")) """







##################################

# EXCERCISE 13


# You've been working on a particularly difficult algorithm all day, and finally decided to take a break and drink some coffee. To your horror, when you returned you found out that your cat decided to take a walk on the keyboard in your absence, and pressed a key or two. Your computer doesn't react to letters being pressed when an unauthorized action appears, but allows typing whitespace characters and moving the arrow keys, so now your masterpiece contains way too many whitespace characters.

# To repair the damage, you need to start with implementing a function that will replace all multiple space characters in the given line of your code with single ones. In addition, all leading and trailing whitespaces should be removed.

# Example

# For

# line = "def      m   e  gaDifficu     ltFun        ction(x):"
# the output should be
# solution(line) = "def m e gaDifficu ltFun ction(x):".

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string line

# One line from your code containing way too many whitespace characters.

# Guaranteed constraints:
# 5 ≤ line.length ≤ 125.

# [output] string

# line with unnecessary whitespace characters removed.

##################################

""" def solution(code):
    return ' '.join(code.split())


print(solution("def      m   e  gaDifficu     ltFun        ction(x):")) """





##################################

# EXCERCISE 14


# You found an awesome customizable Python IDE that has almost everything you'd like to see in your working environment. However, after a couple days of coding you discover that there is one important feature that this IDE lacks: it cannot convert tabs to spaces. Luckily, the IDE is easily customizable, so you decide to write a plugin that would convert all tabs in the code into the given number of whitespace characters.

# Implement a function that, given a piece of code and a positive integer x will turn each tabulation character in code into x whitespace characters.

# Example

# For code = "\treturn False" and x = 4, the output should be

# solution(code, x) = "    return False"
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string code

# Your piece of code.

# Guaranteed constraints:
# 0 ≤ code.length ≤ 1500.

# [input] integer x

# The number of whitespace characters (' ') that should replace each occurrence of the tabulation character ('\t').

# Guaranteed constraints:
# 1 ≤ x ≤ 16.

# [output] string

# The given code with tabulation characters expanded according to x.

##################################


""" def solution(code, x):
    return code.replace('\t', ' ' * x) 


print(solution("\treturn False", 4)) """





##################################

# EXCERCISE 15

# You've launched a revolutionary service not long ago, and were busy improving it for the last couple of months. When you finally decided that the service is perfect, you remembered that you created a feedbacks page long time ago, which you never checked out since then. Now that you have nothing left to do, you would like to have a look at what the community thinks of your service.

# Unfortunately it looks like the feedbacks page is far from perfect: each feedback is displayed as a one-line string, and if it's too long there's no way to see what it is about. Naturally, this horrible bug should be fixed. Implement a function that, given a feedback and the size of the screen, splits the feedback into lines so that:

# each token (i.e. sequence of non-whitespace characters) belongs to one of the lines entirely;
# each line is at most size characters long;
# no line has trailing or leading spaces;
# each line should have the maximum possible length, assuming that all lines before it were also the longest possible.
# Example

# For feedback = "This is an example feedback" and size = 8,
# the output should be

# solution(feedback, size) = ["This is", 
#                                   "an", 
#                                   "example", 
#                                   "feedback"]

##################################


""" import textwrap

def solution(feedback, size):
    return textwrap.wrap(feedback, size)

print(solution("This is an example feedback", 8)) """



##################################

# EXCERCISE 16

# Given a word, check whether it is a palindrome or not. A string is considered to be a palindrome if it reads the same in both directions.

# Example

# For word = "aibohphobia", the output should be
# solution(word) = true;

# For word = "hehehehehe", the output should be
# solution(word) = false.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string word

# A string containing lowercase English letters.

# Guaranteed constraints:
# 1 ≤ word.length ≤ 20.

# [output] boolean

# true if the given word is a palindrome, false otherwise.

##################################

""" def solution(word):
    return word == word[::-1]



print(solution("hehehehehe")) """



##################################

# EXCERCISE 17

# You found your very first laptop in the attic, and decided to give in to nostalgia and turn it on. The laptop turned out to be password protected, but you know how to crack it: you have always used the same password, but encrypt it using permutation ciphers with various keys. The key to the cipher used to protect your old laptop very conveniently happened to be written on the laptop lid.

# Here's how permutation cipher works: the key to it consists of all the letters of the alphabet written up in some order. All occurrences of letter 'a' in the encrypted text are substituted with the first letter of the key, all occurrences of letter 'b' are replaced with the second letter from the key, and so on, up to letter 'z' replaced with the last symbol of the key.

# Given the password you always use, your task is to encrypt it using the permutation cipher with the given key.

# Example

# For password = "iamthebest" and
# key = "zabcdefghijklmnopqrstuvwxy", the output should be
# solution(password, key) = "hzlsgdadrs".

# Here's a table that can be used to encrypt the text:

# abcdefghijklmnopqrstuvwxyz
# ||  |  ||   |     || 
# vv  v  vv   v     vv
# zabcdefghijklmnopqrstuvwxy
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string password

# The password you always use. It is guaranteed to consist only of lowercase English letters.
# If you're using Python 2, note that the string is given as a unicode.

# Guaranteed constraints:
# 1 ≤ password.length ≤ 26.

# [input] string key

# The key to the permutation cipher. It is guaranteed to be a permutation of the plaintext alphabet.
# If you're using Python 2, note that the string is given as a unicode.

# Guaranteed constraints:
# key.length = 26.

# [output] string

# Your password encrypted by the permutations cipher with the given key.

##################################


""" def solution(password, key):
    table = password.maketrans('abcdefghijklmnopqrstuvwxyz', key)
    return password.translate(table)


password = "iamthebest"

key = "zabcdefghijklmnopqrstuvwxy"


print(solution(password, key)) """



##################################

# EXCERCISE 18


# The World Wide Competitive Eating tournament is going to be held in your town, and you're the one who is responsible for keeping track of time. For the great finale, a large billboard of the given width will be installed on the main square, where the time of possibly new world record will be shown.

# The track of time will be kept by a float number. It will be displayed on the board with the set precision precision with center alignment, and it is guaranteed that it will fit in the screen. Your task is to test the billboard. Given the time t, the width of the screen and the precision with which the time should be displayed, return a string that should be shown on the billboard.

# Example

# For t = 3.1415, width = 10, and precision = 2,
# the output should be

# solution(t, width, precision) = "   3.14   "
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] float t

# The time to be displayed on the billboard. It is guaranteed that t has at most 5 digits after the decimal point.

# Guaranteed constraints:
# 0 ≤ t < 1000.

# [input] integer width

# The width of the billboard. It is guaranteed that it's big enough to display the time t with the desired precision.

# In case it's impossible to align the time perfectly in the center, left padding should be 1 whitespace character shorter than right padding.

# Guaranteed constraints:
# 3 ≤ width ≤ 20.

# [input] integer precision

# Precision with which the number should be displayed.

# Guaranteed constraints:
# 0 ≤ precision ≤ 10.

# [output] string

# A string of length width representing the time t as it will be displayed on the billboard.


##################################


def solution(t, width, precision):
    return "{:.{precision}f}".format(str(round(t,precision))).center(width,' ')
    
    # return f"{:{precision}f}".format(round(t,precision)).center(width,' ')


t = 3.1415
width = 10
precision = 2

print(solution(t, width, precision))
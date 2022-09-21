
###### This file includes all the excercises solved in CodeWars website. To run any of the cases uncomment the codes between ''' ''' ######

#------------------------------------------------

# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:

# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


#------------------------------------------------

"""  def unique_in_order(iterable):
    
    listnorep = list()
    for i in range(len(iterable)):
        if i==0:
            listnorep.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            listnorep.append(iterable[i])
    

    return print(listnorep)


unique_in_order('A') """


# Best Practices 

""" def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k """ 



#------------------------------------------------


# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

#------------------------------------------------

""" def get_count(sentence):
    count = 0
    for i in sentence:
        if i=='a' or i=='e' or i == 'i' or i == 'o' or i=='u':
            count += 1

    return count



print(get_count('asdfsasw'))
 """

#------------------------------------------------

# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.

#------------------------------------------------

"""  def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    x = numbers[0] + numbers[1]
    
    return x """

# Best Practices 

""" def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    return sum(numbers[:2])


print(sum_two_smallest_numbers([10, 32423423, 20, 23423234, 30])) """
     
    
    

#------------------------------------------------

# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.

#------------------------------------------------


""" def accum(s):
    result=""
    for i in range(len(s)):
        if result == "":
            result+=s[i].upper()
            result+='-'
    
        else:
            for c in range(i+1):
                if c == 0:
                    result+=s[i].upper()
                elif c < i + 1  :
                    result+=s[i].lower()
                    if c == i and i < len(s) - 1:
                        result += '-'


            
    return result """

 # Best Practices 

""" def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]
                          
print(accum('addas')) """ 



#------------------------------------------------


# Find the average of a list of numbers. If the list
# is empty it should return 0.


#------------------------------------------------

""" def find_average(numbers):
    
    suma = 0
    if numbers == []:
        return 0
    else:
        for i in numbers:
            suma = suma + i

        return suma/len(numbers)

print(find_average([])) """


# Best practices

""" def find_average(array):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0  """
        
        
#------------------------------------------------

# Write a function that finds the sum of all its arguments.

# eg:

# sum_args(1, 2, 3) # => 6
# sum_args(8, 2) # => 10
# sum_args(1, 2, 3, 4, 5) # => 15

#------------------------------------------------


# With the * symbol, an arbitrary number of arguments can be passed into a function.

""" def sum_args(*lista):
    
    suma = 0
    for i in lista:
        suma += i
    return suma


print(sum_args(3, 2, 4, 2, 2, 2)) """




#------------------------------------------------

# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.

# Don't forget the space after the closing parentheses!

#------------------------------------------------


""" def create_phone_number(n):
    phone = ''.join(str(e) for e in n)
    phone = '(' + phone[:3] + ')' + ' ' + phone[3:6] + '-' + phone[6:]
    return phone

print(create_phone_number([1,2,4,5,4,3,2,2,1,1,1])) """


# Best practices

""" def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n) """



#------------------------------------------------

# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

#------------------------------------------------

""" def find_outlier(integers):
    listodd = list()
    listeven = list()
    for i in integers:
        if i%2 != 0:
            listodd.append(i)
        elif i%2 == 0:
            listeven.append(i)
        elif len(listeven) >=1 and len(listodd) >= 1:
            break
        
    if len(listeven) == 1:
        listend = listeven[0]
    else:
        listend = listodd[0]
        
    return listend

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) """


# Best practices

""" def find_outlier(integers):
    listEven = []
    listOdd = []
    for n in integers:
        if n % 2 == 0:
            listEven.append(n)
        else:
            listOdd.append(n)
            
    if len(listEven) == 1:
        return listEven[0]
    else:
        return listOdd[0] """
    
    

#------------------------------------------------

# You just got done with your set at the gym, and you are wondering how much weight you could lift if you did a single repetition. Thankfully, a few scholars have devised formulas for this purpose (from Wikipedia) :

# Epley

# (Look formula in wikipedia)

# McGlothin
# (Look formula in wikipedia)

# Lombardi
# (Look formula in wikipedia)

 
# Your function will receive a weight w and a number of repetitions r and must return your projected one repetition maximum. Since you are not sure which formula to use and you are feeling confident, your function will return the largest value from the three formulas shown above, rounded to the nearest integer. However, if the number of repetitions passed in is 1 (i.e., it is already a one rep max), your function must return w. Also, if the number of repetitions passed in is 0 (i.e., no repetitions were completed), your function must return 0.

#------------------------------------------------


""" def calculate_1RM(w, r):
    
    if r == 0:
        return 0
    elif r == 1:
        return w
    else:
        eply = w*(1+r/30)
        mcglothin = 100*w/(101.3-2.67123*r)
        lombardi = w*r**(0.10)
    
        return round(max([eply, mcglothin, lombardi]))



print(calculate_1RM(100,3)) """



#------------------------------------------------

# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

#------------------------------------------------



""" def friend(x):

# Solution 1
    mine = list()
    for i in x:
        if len(i) == 4:
            mine.append(i)
        
# Solution 2
    
    mine2 = [i for i in x if len(i) == 4]
    
    return mine2

print(friend(["Ryan", "Kieran", "Jason", "Yous"])) """




#------------------------------------------------

# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)

#------------------------------------------------

""" def persistence(n):
    newn = 1
    count = 0
    if len(str(n)) == 1:
        return 0
    else:
        nstr = str(n)
        while len(nstr) != 1:
            for i in nstr:
                newn = newn * int(i)   
            count += 1
            nstr = str(newn)   
            if len(nstr) != 1:
                newn = 1
    return count
        

print(persistence(39)) """


# Best practice 

""" def persistence(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count """

# Best code

""" import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i """
    
    
    
    
#------------------------------------------------

# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

#------------------------------------------------

""" import string

def pig_it(text):
    newword = ''
    for i in text.split():
        if i in string.punctuation:
            newword += i + ' '
        else:
            
            newword += i[1:] + i[0] + 'ay' + ' '
        
    return newword[:-1]
    


print(pig_it('Quis custodiet ipsos custodes ?')) """


# Best practice

# method isalpha detects if the letters of the word are not punctuation marks

""" def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res) """



# Best Code

""" def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst]) """
    
    
    
    
    

#------------------------------------------------

# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

#------------------------------------------------


""" def count_bits(n):
   count = 0
   for i in str(bin(n)[2:]):
       if i == '1':
           count+=1
   return count


print(count_bits(1234)) """


# Best Code

# You should always try to see if there is a method before implementing a loop

""" def countBits(n):
    return bin(n).count("1") """


#------------------------------------------------

# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# Please note that using encode is considered cheating.

#------------------------------------------------

""" import string

 def rot13(message):
    alphabet = list(string.ascii_letters)
    newm = ''
    for i in message:
        if i.isalpha():
            if string.ascii_letters.index(i) + 13 < 26:
                newm += alphabet[string.ascii_letters.index(i) + 13]
            elif string.ascii_letters.index(i) + 13 < 39 :
                newm += alphabet[string.ascii_letters.index(i) + 13 - 26] 
            else:
                newm += alphabet[string.ascii_letters.index(i) + 13 - 26].upper()
        else:
            newm += i
    return newm 


print(rot13('aA bB zZ 1234 *!?%'))  """


# Best practice 

# Use the % for getting the remainder of a division is important when looping over a closed list like the alphabet one.

""" import string
from codecs import encode as _dont_use_this_

def rot13(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    outputMessage = ""
    for letter in message:
        if letter in alpha.lower():
            outputMessage += alpha[(alpha.lower().index(letter) +13) % 26].lower()
            
        elif letter in alpha:
            outputMessage += alpha[(alpha.index(letter) +13) % 26]
        else:
            outputMessage += letter
        
    print((alpha.index('Z') ) )
    return outputMessage


print(rot13('aA bB zZ 1234 *!?%')) """


#------------------------------------------------

# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

#------------------------------------------------

""" def is_pangram(s):
    import string
    alphabet_dic = dict.fromkeys(list(string.ascii_lowercase), 0)
    for i in s.lower():
        if i.lower() in list(string.ascii_lowercase):
            alphabet_dic[i] += 1
    return not 0 in alphabet_dic.values()
        

print(is_pangram('The quick brown fox jumps over the lazy dog'))
 """






#------------------------------------------------

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

#------------------------------------------------


""" def rgb(r, g, b):
    
    
    hexa = ''
    for i in [r, g, b]:
        if i < 0:
            i = 0
        elif i > 255:
            i = 255
        hexa += hex(int(i/16))[2:] + hex(int(i%16))[2:]
        
    return hexa.upper() """


# One linner but I haven't been able to remove spaces between 3 numbers of [r, g, b]
""" def rgb(r, g, b):
    
    x = [''.join(hex(int(i/16))[2:].upper()) + ''.join(hex(int(i%16))[2:].upper()) for i in [r, g, b]] """

""" print(rgb(201,25,0)) """
    


#-------------------------------------#

# You need to write regex that will validate a password to make sure it meets the following criteria:

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)

#-------------------------------------#


# Best Practice

""" from re import search


regex = (
    '^'            # start line
    '(?=.*\d)'     # must contain one digit from 0-9
    '(?=.*[a-z])'  # must contain one lowercase characters
    '(?=.*[A-Z])'  # must contain one uppercase characters
    '[a-zA-Z\d]'   # permitted characters (alphanumeric only)
    '{6,}'         # length at least 6 chars
    '$'            # end line
)


print(bool(search(regex, 'fjd3IR9'))) """





#-------------------------------------#

# You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.

# Task:
# Return an array or a tuple or a string depending on the language (see "Sample Tests") with

# the smallest number you got
# the index i of the digit d you took, i as small as possible
# the index j (as small as possible) where you insert this digit d to have the smallest number.
# Examples:
# smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
# 126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

#-------------------------------------#


# Best solution        

""" def smallest(n):
    s = str(n)
    min1, from1, to1 = n, 0, 0
    for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        for j in range(len(removed)+1):
            num = int(removed[:j] + s[i] + removed[j:])
            if (num < min1):
                min1, from1, to1 = num, i, j
    return [min1, from1, to1] 




print(smallest(209917)) """



#------------------------------------------------

# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

#------------------------------------------------



""" def alphabet_position(text):
    import string
    
    posiletter = ''
    for i in text:
        if i.lower() in string.ascii_lowercase:
            posiletter += str(string.ascii_letters.index(i.lower()) + 1) + ' '
    
    return posiletter[:-1] 




print(alphabet_position("The sunset sets at twelve o' clock.")) """


 # Best practice 

"""def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha()) """








#------------------------------------------------

# We want to create a function that will add numbers together when called in succession.

# add(1)(2) # equals 3
# We also want to be able to continue to add numbers to our chain.

# add(1)(2)(3) # 6
# add(1)(2)(3)(4); # 10
# add(1)(2)(3)(4)(5) # 15
# and so on.

# A single call should be equal to the number passed in.

# add(1) # 1
# We should be able to store the returned values and reuse them.

# addTwo = add(2)
# addTwo # 2
# addTwo + 5 # 7
# addTwo(3) # 5
# addTwo(3)(5) # 10
# We can assume any number being passed in will be valid whole number.

#------------------------------------------------

# Defining a class is required in order to call a function with multiple () arguments like add()()()...

""" class add(int):
    def __call__(i,n):
        return add(i+n)
    

print(add(3)(5)(12))

addTwo = add(2)

print(addTwo) """





#------------------------------------------------

# Sum of Pairs
# Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

# If there are two or more pairs with the required sum, the pair whose second element has the smallest index is the solution.

# sum_pairs([11, 3, 7, 5],         10)
# #              ^--^      3 + 7 = 10
# == [3, 7]

# sum_pairs([4, 3, 2, 3, 4],         6)
# #          ^-----^         4 + 2 = 6, indices: 0, 2 *
# #             ^-----^      3 + 3 = 6, indices: 1, 3
# #                ^-----^   2 + 4 = 6, indices: 2, 4
# #  * the correct answer is the pair whose second value has the smallest index
# == [4, 2]

# sum_pairs([0, 0, -2, 3], 2)
# #  there are no pairs of values that can be added to produce 2.
# == None/nil/undefined (Based on the language)

# sum_pairs([10, 5, 2, 3, 7, 5],         10)
# #              ^-----------^   5 + 5 = 10, indices: 1, 5
# #                    ^--^      3 + 7 = 10, indices: 3, 4 *
# #  * the correct answer is the pair whose second value has the smallest index
# == [3, 7]
# Negative numbers and duplicate numbers can and will appear.

# Note: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.

#------------------------------------------------



""" def sum_pairs(ints, s):
    from itertools import combinations
    
    comb = set(list(combinations(ints,2)))
    
    listIndex = list()
    listNum = list()
       
    for t in comb:
        
        if sum(t) == s:
            listNum.append([t[0], t[1]])
            listIndex.append(ints.index(t[1],ints.index(t[0])+1))

    if listNum == []:
        return None    
        
    min_index = listIndex.index(min(listIndex))  
    
    print(comb)  
    return listNum[min_index]


print(sum_pairs([10, 5, 2, 3, 7, 5], 10)) """




# Fast version. We loop only once through the list so the computational time is O(n) instead of O(n^2)

""" def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i) """






















##############################################################
####### Code to count the number of excercises done ##########
##############################################################

fp=open('Python\CodeWars.py')
c = 0
nc = 0
for line in fp:
    if line.startswith('#------------------------------------------------'):
        c+=1
    elif line.startswith('#-------------------------------------#'):
        nc += 1
        
print('Num exercises done:', int(c/2))
print('Num excercises not completed: ', int(nc/2))

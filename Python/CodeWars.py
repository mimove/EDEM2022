
#This file includes all the excercises solved in CodeWars website. To run any of the cases uncomment the code after the #------------------------------------------------ line

#------------------------------------------------

""" Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3] """


#------------------------------------------------

""" def unique_in_order(iterable):
    
    listnorep = list()
    for i in range(len(iterable)):
        if i==0:
            listnorep.append(iterable[i])
        elif iterable[i] != iterable[i-1]:
            listnorep.append(iterable[i])
    

    return print(listnorep)


unique_in_order('A')


# Best Practices 

def unique_in_order(iterable):
    k = []
    for i in iterable:
        if k == []:
            k.append(i)
        elif k[-1] != i:
            k.append(i)
    return k """



#------------------------------------------------


""" Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces. """

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

""" Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455. """

#------------------------------------------------

""" def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    x = numbers[0] + numbers[1]
    
    return x

# Best Practices 

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    
    return sum(numbers[:2])


print(sum_two_smallest_numbers([10, 32423423, 20, 23423234, 30]))
     """
    
    

#------------------------------------------------

""" This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z. """

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

def accum(s):
    output = ""
    for i in range(len(s)):
        output+=(s[i]*(i+1))+"-"
    return output.title()[:-1]
                          
print(accum('addas'))

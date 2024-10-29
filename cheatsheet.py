"""
Summary of Programming Code for Imperative Programming Course for BSc Artificial Intelligence
Feel free to commit/edit this document
"""

"""
General Info:
"""
#Built in functions:
abs() #-> Returns absolute value of a number
all() #-> Return True if all items in an iterable object are true
any() #-> Return True if any item in an iterable object is true
bin() #-> Return the binary version of a number
bool() #- Returns boolean value of specified object
chr() #-> Returns character from Ascii --> Input: int, output: str
dict() #-> Returns dictionary --> Input: key = value, output: dict
enumerate() #-> Returns tuple with format (index, element) --> Input: list/dict/set/tuple, output: (index, element) --> Note for dict element = key
eval() #-> Evaluates expression
float() #-> Convert into float
format() #-> Format code (More info below)
hex() #-> Convert into hexadecimal
input() #-> Ask for user input
int() #-> Convert to integer (negatives allowed)
len() #-> Return length of list/dict/set/tuple
list() #-> Returns list, for example putting each char of a string into a list
max() #-> Returns largest item --> input: items separated by commas, or list/dict/set/tuple --> Note for dict: item = key
min() #-> Returns smallest item --> input: items separated by commas, or list/dict/set/tuple --> Note for dict: item = key
ord() #-> Convert character into number in Ascii --> Input: str, output: int
pow(x, y) #-> Returns x to the power of y (x^y) 
print() #-> Print function
range(start, end, step) #-> Returns list of numbers, starting and including "start" till excluding "end" with increments of size "step"
  #--> Defaults: Start = 0, step = 1
reversed() #-> Returns reversed iterator, input: list/dict/tuple/set
set() #-> Create new set
slice(start, end, step) #-> Returns slice object (Might be confusing, use normal slicing with [])
sorted() #-> Returns sorted list/dict/tuple/set --> With dict: sort keys
sum() #-> Sums all objects in list/dict/tuple/set --> With dict: sum keys
tuple() #-> Returns tuple --> Input: list/dict/tuple/set
type() #-> Returns type of input

#String methods - str = string:
str.capitalize() #-> Convert first character to uppercase
str.casefold() #-> Convert string to lower case
str.count(x) #-> Count how many times substring "x" occurs in string
str.endswith(x) #-> Returns whether string ends with substring "x"
str.find(x) #-> Returns index of first occurance of "x" in string, if no match --> return -1
str.format(x) #-> More info below
str.index(x) #-> Returns index of first occurance of "x" in string, if no match --> Error
str.isalnum() #-> Returns True if all characters in string are alphabetic letters or numbers
str.isalpha() #-> Returns True if all characters in string are alphabetic
str.isascii() #-> Returns True if all characters in string are ascii characters
str.isdecimal() #-> Returns True if all characters in string are decimals
str.isdigit() #-> Returns True if all characters in string are digits
str.islower() #-> Returns True if all characters in string are lower case
str.isnumeric() #-> Returns True if all characters in string are numeric (digits, exponents, fractions)
str.isspace() #-> Returns True if all characters in string are whitespace
str.isupper() #-> Returns True if all characters in string are upper case
"x".join(lst) #-> Join all elements in list/dict/tuple/set and separate them with x --> Note that lst must only have strings and for dict, keys are considered
str.lower() #-> Convert string to lowercase
str.lstrip() #-> Remove any whitespaces in front
str.partition(x) #-> Return tuple with format (everything before x, x, everything after x) for first occurance of x
str.replace(a, b, n) #-> Replace the first n occurances of a in str with b --> Deafult of n = 0
str.rfind(x) #-> Returns last occurance of x in string --> Return -1 if not found
str.rindex(x) #-> Returns last occurance of x in string --> Error if not found
str.rpartition(x) #-> Return tuple with format (everything before x, x, everything after x) for last occurance of x
str.rstrip() #-> Remove all whitespaces at the end
str.split(x) #-> Split string at each occurance of x into list --> Default of x is " " (whitespace)
str.startswith(x) #-> Returns True when string starts with x
str.strip() #-> Remove all whitespaces at beginning or end of string
str.swapcase() #-> Lowercase of string become uppercase and vice versa
str.upper() #-> Convert string into uppercase

#List methods - list = lst:
# !!!Note that unless "Returns" is included, the methods do not return any value but modify the original list !!

lst.append(x) #-> Add x at the end of original list --> Only 1 input allowed
lst.clear() #-> Remove all element in original list
lst.copy() #-> Returns copy of original list
lst.count(x) #-> Returns number of occurances of x in list 
lst.extend(lst2) #-> Add all element in lst2 (the second list) to the end of lst
lst.index(x) #-> Returns index of first occurance of "x" --> Not found returns Error
lst.insert(position, element) #-> Inserts "element" into original list at index "position". So index of "element" within lst becomes "position"
lst.pop(x) #-> Removes element at index "x", default x is -1 (last item)
lst.remove(x) #-> Remove first occurance of "x" in list
lst.reverse(x) #-> Reverse order of list
lst.sort(x) #-> Sort list

#Dictionary methods- dictionary = dct:
dct.clear() #-> Remove all element from original dictionary
dct.copy() #-> Returns copy of original dictionary
dct.fromkeys(x, y) #-> Returns a dictionary with specificied keys and values
  #  x can be string/list/tuple and wil be the keys
  #  y can be string/list/tuple and wil be the values
  # Each key is matched to the value
dct.get(key) #-> Returns value of specificied key
dct.items() #-> Returns list of tuples with format (key, value)
dct.keys() #-> Returns list with all dictionary keys
dct.pop(key) #-> Removes key-value pair that has key "key"
dct.popitem() #-> Removes last inserted key-value pair
dct.setdefault(key, value) #-> Returns value of specified key, if key does not exist: insert key with specified value
dct.update(x) #-> Add key-value pair to dictionary, Input: list/tuple/set
dct.values(x) #-> Returns list of all values of dictionary

#Tuple methods - tuple = tpl:
tpl.count(x) #-> Returns number of times "x" occurs in tuple
tpl.index(x) #-> Returns index of first occurance of "x" in tuple --> Error if not found

"""
Lecture code:
"""

  #Week 6: 
    #Parser:
    def parser():
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        register = [alphabet.find(letter) for letter in input()]
        instructions = input()
        
        position = 0
        for instruction in instructions:
            if instruction == "<":
                position = (position + len(register) - 1) % len(register)
            if instruction == ">":
                position = (position + 1) % len(register)
            if instruction == "*":
                register[position] = (register[position] + register[(position + 1) % len(register)]) % len(alphabet)
            if instruction == "+":
                register[position] = (register[position] + 1) % len(alphabet)
            if instruction == "-":
                register[position] = (register[position] + len(alphabet) - 1) % len(alphabet)
        for number in register:
            print(alphabet[number], end="")
        print()

"""
General functions:
"""

  #Function that reverses a list or string:
    def reverse(item):
      return item[::-1]
      
  #Function that checks if a number is a prime:
    def check_prime(number):
      if number < 2:
        return False
        
      i = 2
      while i*i <= number:
        if number % i == 0:
          return False
        i += 1
          
      return True
    
  #Function that determines whether a number is divisble by each of its digits:
    def digit_divisible(number: int):
      for i in str(number):
        if number % int(I) != 0:
            return False
        else:
            return True

 #Function determining the number of solutions of a given quadratic equation:
    def number_of_quadratic_solutions(a,b,c):
      if b**2-4*a*c == 0:
        return 1
      elif b**2-4*a*c>0:
        return 2
      elif b**2-4*a*c<0:
        return 0
      
#Function that recursively exponentiates a number to a given power:
  def exponentiation(a,b):
      if b == 0:
          return 1
      else:
          return a * exponentiation(a, b - 1)
      
#Function that recursively computes the factorial of a given number:
  def factorial(x):
      if x == 0:
          return 1
      else:
          return x * factorial(x-1)
      
#Function that determines if a number is prime:
  def is_prime(n):
      if n <= 1:
          return False
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              return False
      return True
    
#Function that determines if a number is a nested prime:
  def is_prime(n):
      if n <= 1:
          return False
      for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
              return False
      return True

  def nested_prime(number):
      count = len(str(number)) 
      i = 0
      while i != count:
          if is_prime(number/10**i):
              i += 1
          else:
              return False
        
    return True

#Function that recursively determines if a word is a palindrome:
  def recursive_palindrome(word):
      if len(word) < 2:
          return True
      if word[0] == word[-1]:
          return recursive_palindrome(word[1:-1])
      
      return False
    
#Function that determines whether two lists are permutations of each other (a bit cheeky, but works nonetheless):
  def is_permutation(a, b):
      if sorted(a) == sorted(b):
          return True
      else:
          return False

#Function that determines the highest number in a list recursively:
  def find_max(lst):
    if len(lst) == 1:
      return lst[0]
      
    max_value = find_max(lst[1:])
    if lst[0] > max_value:
      return lst[0]
    else:
      return max_value

#Function to do the Tower of Hanoi:
  def tower_hanoi(n, a, b, c):
    #N = number of disks
    #A = Current pole
    #B = Auxillary pole
    #C = Destination

    if n == 1:
      return print("Move 1st disk from ", a, " to ", b)
    tower_hanoi(n - 1, a, c, b)
    print("Move ", n, "the disk from ", a, " to ", c)
    tower_hanoi(n - 1, b, a, c)


      
#Extra:




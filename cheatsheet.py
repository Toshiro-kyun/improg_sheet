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
#some very important info about slicing

"""
Methods on how to solve the multiple choice questions:

There are two forms of these questions, the ones that ask you to find the process in which you find the answer and the ones that ask you
to follow a certain path of instructions and then you give the answer.

Both can generally be solved with this method (If your question is type two, just follow the instrucitons they give you and compare the answers)
1. Write out the initial values of X and of Y (This is shown in the first line of the question)
    These should have a subscript of 0 meaning that they are X_0 and Y_0 (X with a tiny 0 underneath and Y_0)
2. Write out the final answer the question is trying to get from you (Second line of the question)

3. There is a few rules that you should follow to know if each one is correct or wrong.
  1. Firstly, each time you do an instruction, you change the subscript of the variable you are editing to the current instruciton number
  2. After an instruciton is carried out, you must take that new value as the current one for that given variable
  3. Repeat untill all instructions are done for each one of the options (A, B and C) or untill the instructions given are done
  4. If for any of them the final values of the variables are the same as the final answer, then that option is correct.

There are some exceptions to this method that have to be understood so that it works correctly:
If the answer requires you to give the answer in the form constant = variable + variable or something along those lines, you have to
substitue the values that you got for your variables at the end and then confirm. You may also have to rearrange the answer to get 
it in the requested form.

Dont be scared of squared, and 1/2, usually (if the answer is correct) they will cancel eachother out or resolve somehow.

Sometimes you have to take things analytically, for example, if you see x+y=A and the first instruction is X=X+Y, then you 
are correct to assume that X=A
  
-----------------------------------------------------------------------
Lets go over a simple example:
We get the following question:
/* x == A, y == B */
/* x == 2*A + 2*B, y == B - A */

(a) x = 2*x + 2*y; y = y - x
(b) y = y - x; x = 4*x + 2*y
(c) x = 2*x + 2*y; y = (x - y)/2

Firstly we write on our scrap paper:
X_0 == A      Y_0 == B  / X==2A+2B    Y==B-A (Now we know our initial conditions and the final values to be obtained)

Then we start with A:
Option A:
(The first instruction tells us that the new value of X should be 2*x + 2*y so we write out:)
X_1=2X_0 + 2Y_0 ---> X_1= 2A+2B (We use the initial values of X and Y to create the new value of X)

(From now onwards, our value of X will be X_1 untill edited again)

The next instruction tells us that (Y = Y - x) so we write out:
Y_2 = Y_0 - X_1 --> Y_2 = B - (2A + 2B) --> Y_2 = -B-2A

We have reached the end of our instructions so that means that we have to compare the final values of Y and X obtained
In this case, the final values of X and Y are X_1 and Y_2 now, X_1 does equal to the final answer but Y_2 dosent
So we move on to the next option, option B:

Option B:
(First instruciton tells us that y = y - x so we write out:)
Y_1 = Y_0 - X_0 --> Y_1 = B-A

Now we go onto the next instruction, x = 4*x + 2*y, so we write out:
X_2 = 4X_0 + 2Y_1 --> X_2 = 4A + 2B - 2A --> X_2 = 2A + 2B

Thats the end of the instructions. We can see that X_2 is the same as the X final answer and Y_1 is the same as the final Y answer.
Therefore, option B is correct

Hopefullt this helps clear out some stuff, if you are reading this during the exam, best of luck!
If you are reading this before the exam and dont understand how the method works, contact ricardo@rubert.es
---------------------------------------------------------------
"""



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


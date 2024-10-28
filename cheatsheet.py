# Summary of Programming Code for Imperative Programming Course for BSc Artificial Intelligence
# Feel free to commit/edit this document

#General Info:
#some very important info about slicing

#Lecture code:

#General functions:
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




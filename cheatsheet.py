# Summary of Programming Code for Imperative Programming Course for BSc Articificial Intelligence
# Feel free to commit/edit this document

#General Info:
#some very important info about slicing
#Lecture code:

#Assignment code:
  #Function that determines whether a number is divisble by each of its digits:
    def digit_divisible(number):
    for i in number:
        try:
            i = int(i)
            if int(number) % i != 0:
                return False
        except ZeroDivisionError:
            pass
        else:
            return True

 #Function determining the number of solutions of a given quadratic equation:
    import math
    def number_of_quadratic_solutions(a,b,c):
      number = 0
      if b**2-4*a*c == 0:
          number += 1
          return(number)
      elif b**2-4*a*c>0:
          number +=2
          return(number)
      elif b**2-4*a*c<0:
          return(number)
      
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
#Extra:




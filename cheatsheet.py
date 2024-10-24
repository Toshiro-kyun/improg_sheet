# Summary of Programming Code for Imperative Programming Course for BSc Articificial Intelligence
# Feel free to commit/edit this document

#General Info:
#some very important info about slicing
#Lecture code:

#Assignment code:
  #Function that determines whether a number is divisble by each of its digit:
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



 #Function determining the number of solution of a given quadratic equation:
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

#Extra:




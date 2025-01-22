"""
Summary of Programming Code for Imperative Programming Course for BSc Artificial Intelligence
Feel free to commit/edit this document
"""

print("Hello world!")

"""
General Info:
"""
#List/string slicing:
def slice_string():
  obj[start:end:step] 
  
# Any of these can be excluded, but use ":" to indicate
# Return the same type (string/list) from and including "start" till but excluding "end" with a stepsize of "step"
# Start and end must be within the length of the object
# Examples:
  
def examples():
  string = "helloWorld"
  string[1:] #--> "elloWorld"
  string[:5] #--> "hello"
  string[1:3] #--> "el"
  string[1:8:2] #--> elWr
  string[::-1] #--> dlroWolleh

#Accessing items in string/list/dict/tuples:
#Remember that indexing starts at 0 and ends at (len(obj) - 1)
def access():
  obj[index] #-> Returns item at index "index" --> Used for strings, list, tuples
  obj[key] #-> Returns value associated with "key" in dictionary

#Changing items in list/dict:
def change():
  obj[index] = new_value #-> Makes the value of the element at index "index" in list "obj" equal to "new_value"
  obj[key] = new_value #->  Makes the value of the value of pair with key "key" in dict "obj" equal to "new_value" 

#Add 2 lists:
def add():
  list1 = [1]
  list2 = [2]
  return list1 + list2 #-> Returns [1, 2]

#List into string:
# -> X = "" (empty string) returns the elements in lst joined into a string
# -> E.g: lst = ["Hello", "World"], x = "" ====> "HelloWorld"
# -> X = " " (Space) returns the elements in lst joined into a string with a space between each element 
# -> E.g: lst = ["Hello", "World"], x = " " ====> "Hello World"
def list_to_string(lst, x):
  return f"{x}".join(lst) 
  
#List comprehension:
# Easier to demonstrate with an example
# Suppose we want to convert all elements to strings:
def list_convert_str():
  lst = [1, 2, 3, 4, 5, 6]
  return [str(x) for x in lst]
  
#Suppose we want to only return elements that are even:
def sort_even():
  lst = [1, 2, 3, 4, 5, 6]
  return [x for x in lst if x % 2 == 0]
  
#Suppose we want to return, 0 if it is even and 1 if an element is odd 
def one_odd_zero_even():
  lst = [1, 2, 3, 4, 5, 6]
  return [0 if x % 2 == 0 else 1 for x in last]

#Passing unknown amounts of parameters:
def pass_parameters(*args):
  return args #-> For example: pass_parameters(1, 2, 3, 4) will return args = [1, 2, 3, 4]

def pass_parameters(**kwargs):
  return kwargs #-> For example: pass_parameters(A= 1, B= 2) will return kwargs = {"A": 1, "B": 2} !!Keywords, e.g. A & B, are needed

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
        
#Function to create a board:
def create_board(width, height):
  return [[0 for _ in range(width)] for _ in range(height)]
                                                  
#Function to return all possible substrings of a string
def substrings(s):
  substring_lst = []
  
  for x in range(len(s)):
    for y in range(x + 1, len(s) + 1):
      substring_lst.append(s[x:y])

  return substring_lst

#Function to convert integer to binary:
def binary_convert(x: int):
  return f"{x:b}"
  
#Function to check whether all the word only consists of characters stored in s
def check_char(word, s):
  return all([x in s for x in word])
    
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

def main():
  print(recursive_permutation("happy"))
  
# Function that recursively finds all possible swapcase permutations of a string. Eg. "ab" would return ["ab, "Ab, "aB, "AB"]
def recursive_permutation(s):
  # Base case: if the string is empty, return an empty list of permutations
  if s == "":
    return [""]
  
  result = []
  # Process each character in the string
  for i in range(len(s)):
    # Choose the character at index i
    char = s[i]
    # Rest of the string after removing char
    remaining = s[:i] + s[i+1:]
    
    # Recursive call for permutations of the remaining string
    for perm in recursive_permutation(remaining):
      # Append both lowercase and uppercase variations
      result.append(char.lower() + perm)
      result.append(char.upper() + perm)

  return result
  
def main():
  print(recursive_gcd(7, 12))

# Function that recursively finds the gcd of two numbers
def recursive_gcd(a, b):
  if a == b:
      return a
  elif a > b:
      if a % b == 0:
          return b
      else:
          return recursive_gcd(a, b - 1)
  elif a < b:
      if b % a == 0:
          return a
      else:
          return recursive_gcd(a - 1, b)
#Function that recursively finds sum of digits
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
#Function that recursively reverses a string
def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

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

#Function that recursively flattens a nested list:
def recursive_flatten(nested_list):
  result = []
  for item in nested_list:
      if isinstance(item, list):  # Check if the item is a list
          result.extend(flatten(item))  # Recursively flatten and extend the result
      else:
          result.append(item)  # Add non-list items to the result
  return result
  
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
      
#Function that prints out a given number in expanded form ie. 324 = 300 + 20 + 4. Admittedly very lengthy, but still works
def expanded_form(num):
  if len(str(num)) == 1:
      return str(num)
  counter = len(str(num))
  list_number = []
  while num >= 10:
      remainder = num % 10**(counter - 1)
      list_number.append(num - remainder)
      num = remainder
      counter -= 1
  list_number.append(remainder)
  final_list_number = []
  for number in list_number:
      if number != 0:
          final_list_number.append(number)
      else:
          pass
  final_list_number2 = []
  for number in final_list_number:
      if number not in final_list_number2:
          final_list_number2.append(number)
      else:
          pass
  result = ""
  result += f"{final_list_number2[0]} +"
  for number in final_list_number2[1:len(final_list_number2) - 1]:
      result += f" {number} +"
      
  result += f" {str(final_list_number2[len(final_list_number2) - 1])}"
  result = result.split(" + ")
  result2 = []
  for element in result:
      if element not in result2:
          result2.append(element)
      else:
          pass
  return " + ".join(result2)

def main():
  print(expanded_form(343203))

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

#Recursively find all ways to compute the target with a list of numbers:
def recursive_compute(nums, target):
  if len(nums) == 1:
    return int(nums[0] == target)

  rest_nums = nums[2:]
  possibilities = [
    nums[0] + nums[1],
    nums[0] - nums[1],
    nums[0] * nums[1],
    nums[0] / nums[1]
  ]
  return sum([recursive_computer(x + rest_nums, target) for x in possibilities])

"""
Lecture code:
"""
#Week 1:
  #Code deemed the basics of basics and therefore not included

#Week 2: 
  #Determine days in a month
def day_month():
  month = input().lower()
  match month:
    case "january" | "1" | "march" | "3" | "may" | "5" | "july" | "7" | \
            "august" | "8" | "october" | "10" | "december" | "12":
      print("That month has 31 days")
    case "april" | "4" | "june" | "6" | "september" | "9" | "november" | "11":
      print("That month has 30 days")
    case "february" | "2":
      print("That month has 28 days")
    case other:
      print("That is not a valid month.")

  #Imperial units:
def imperial():
  meters = float(input())
  inches = meters / 0.0254
  print(int(inches // 12), "ft", int(inches % 12),"in")

  #Vector-length:
def vector_length():
  import math
  
  def get_vector_length(x, y):
      return math.sqrt(x*x + y*y)

#Week 3:
  #Intersecting lines:
def intersecting_lines():
  line1_x1 = float(input())
  line1_y1 = float(input())
  line1_x2 = float(input())
  line1_y2 = float(input())
  # Represents line (line1_x1, line1_x2) - (line1_x2, line1_y2)
  line2_x1 = float(input())
  line2_y1 = float(input())
  line2_x2 = float(input())
  line2_y2 = float(input())
  # Represents line (line2_x1, line2_x2) - (line2_x2, line2_y2)

  def process(line1_x1, line1_y1, line1_x2, line1_y2, line2_x1, line2_y1, line2_x2, line2_y2):
    if line1_x1 > line1_x2:
      return process(line1_x2, line1_y2, line1_x1, line1_y1, line2_x1, line2_y1, line2_x2, line2_y2)
    if line2_x1 > line2_x2:
      return process(line1_x1, line1_y1, line1_x2, line1_y2, line2_x2, line2_y2, line2_x1, line2_y1)
    # Now, line1_x1 <= line1_x2 and line2_x1 <= line2_x2
    if max(line1_x1, line1_x2) < min(line2_x1, line2_x2) or min(line1_x1, line1_x2) > max(line2_x1, line2_x2):
      # x-coordinates do not overlap
      print("NONE")
    elif max(line1_y1, line1_y2) < min(line2_y1, line2_y2) or min(line1_y1, line1_y2) > max(line2_y1, line2_y2):
      # y-coordinates do not overlap
      print("NONE")
    elif line1_x2 == line1_x1:
      # Vertical line
      if line2_x2 == line2_x1:
        # Two overlapping vertical lines
        if max(line1_y1, line1_y2) == min(line2_y1, line2_y2):
          # Lines meet in a single point
          print("(" + str(line1_x1)+", "+str(max(line1_y1, line1_y2))+")")
        elif min(line1_y1, line1_y2) == max(line2_y1, line2_y2):
          # Lines meet in a single point
          print("(" + str(line1_x1)+", "+str(min(line1_y1, line1_y2))+")")
        else:
          # Overlapping line segments
          print("OVERLAP")
      else:
        # One vertical line
        y = line2_y1 + (line1_x1 - line2_x1) / (line2_x2 - line2_x1) * (line2_y2 - line2_y1)
        if y < min(line1_y1, line1_y2) or y > max(line1_y1, line1_y2):
          print("NONE")
        else:
          print("("+str(line1_x1)+", "+str(y)+")")
    elif line2_x2 == line2_x1:
      # One vertical line, switch the lines
      return process(line2_x1, line2_y1, line2_x2, line2_y2, line1_x1, line1_y1, line1_x2, line1_y2)
    else:
      # Two non-vertical lines
      b1 = (line1_y2 - line1_y1) / (line1_x2 - line1_x1)
      a1 = line1_y1 - line1_x1 * b1
      # First line is a1 + b1 * x
      b2 = (line2_y2 - line2_y1) / (line2_x2 - line2_x1)
      a2 = line2_y1 - line2_x1 * b2
      # Second line is a2 + b2 * x
      if b2 == b1:
        # Parallel lines
        if a1 == a2:
          # Overlapping lines
          if line1_x1 == line2_x2:
            # Lines meet in a single point
            print("(" + str(line1_x1) + ", " + str(line1_y1) + ")")
          elif line1_x2 == line2_x1:
            # Lines meet in a single point
            print("(" + str(line1_x2) + ", " + str(line1_y2) + ")")
          else:
            print("OVERLAP")
        else:
            # No overlap
            print("NONE")
      else:
          x = (a1 - a2) / (b2 - b1)
          if x < min(line1_x1, line1_x2) or x > max(line1_x1, line1_x2):
            # Intersection point is not part of line 1
            print("NONE")
          elif x < min(line2_x1, line2_x2) or x > max(line2_x1, line2_x2):
            # Intersection point is not part of line 2
            print("NONE")
          else:
            print("("+str(x)+", "+str(a1 + b1 * x)+")")

  def main():
    process(line1_x1, line1_y1, line1_x2, line1_y2, line2_x1, line2_y1, line2_x2, line2_y2)

  #Oddsevens:
def oddsevens():
  player1 = float(input())
  player2 = float(input())
  if player1 <= 0 or player2 <= 0:
    print("FORFEIT")
  elif int(player1) < player1 or int(player2) < player2:
    print("FORFEIT")
  elif (player1 + player2) % 2 == 1:
    print("ODDS")
  else:
    print("EVENS")

#Week 4:
  #Letter occurrence:
def letter_occurance():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letter_counts = [0] * len(alphabet)
  print("Please enter a text:")
  for letter in input():
    if letter.lower() in alphabet:
      letter_counts[ord(letter.lower()) - ord("a")] += 1
  
  for letter in range(len(alphabet)):
    if letter_counts[letter] > 0:
      print(alphabet[letter] + ": " + str(letter_counts[letter]))

  #Encoding - Reverse alphabetic characters:
def encoding():
  line = input()
  for character in line:
    if "a" <= character <= "z":
      print(chr(ord("z") + ord("a") - ord(character)), end="")
    elif "A" <= character <= "Z":
      print(chr(ord("Z") + ord("A") - ord(character)), end="")
    else:
      print(character, end="")
  print()

  #Lunar vacation:
def lunar():
  import math

  x = int(input())
  y = int(input())
  speed_x = 0
  speed_y = 0
  line = input()
  t = 0
  gravity = -1.625
  thrust = 3
  while line != "":
    delay = int(line)
    rotation = int(input())
    duration = int(input())
    x = x + speed_x * (delay + duration) + thrust * math.sin(rotation/180 * math.pi) * duration * duration / 2
    speed_x += thrust * math.sin(rotation/180 * math.pi) * duration
    y = y + speed_y * delay + gravity * delay * delay / 2
    speed_y += delay * gravity
    y = y + speed_y * duration + (gravity + thrust * math.cos(rotation/180 * math.pi)) / 2 * duration * duration
    speed_y += (thrust * math.cos(rotation/180 * math.pi) + gravity) * duration
    if y < 0:
      print("CRASHED")
      exit(0)
    if -5 < x < 5 and y < 1 and rotation == 0 and speed_x*speed_x + speed_y*speed_y <= 1:
      print("SUCCESSFUL")
      exit(0)
    line = input()
    
  print("UNSUCCESSFUL")

#Week 5:
  #Game of life:
def game_of_life():
  def get_number_of_neighbours(grid, x, y):
    count = 0
    for row in [-1, 0, 1]:
      for column in [-1, 0, 1]:
        if 0 <= x + row < len(grid) and 0 <= y + column < len(grid):
          count += grid[x + row][y + column]
    count -= grid[x][y]
    return count


  def show_grid(grid):
    for row in grid:
      for cell in row:
        print(" " if cell == 0 else "*", end="")
      print()


  BOARD_SIZE = 31
  grid_now = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
  grid_next = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

  center = BOARD_SIZE // 2
  grid_now[center - 1][center] = 1
  grid_now[center][center + 1] = 1
  grid_now[center + 1][center - 1] = 1
  grid_now[center + 1][center] = 1
  grid_now[center + 1][center + 1] = 1
  show_grid(grid_now)
  while input() == "":
    for x in range(BOARD_SIZE):
      for y in range(BOARD_SIZE):
        neighbours = get_number_of_neighbours(grid_now, x, y)
        if neighbours == 3:
          grid_next[x][y] = 1
        elif neighbours != 2:
          grid_next[x][y] = 0
        else:
          grid_next[x][y] = grid_now[x][y]
    for x in range(BOARD_SIZE):
      for y in range(BOARD_SIZE):
        grid_now[x][y] = grid_next[x][y]
    show_grid(grid_now)

  #Descriptive:
def descriptive():
  items = [float(term) for term in input().split()]
  sum_x = 0
  sum_squared = 0
  for item in items:
    sum_x += item
    sum_squared += item*item
  print(round(sum_x/len(items),3))
  print(round((sum_squared - sum_x * sum_x / len(items))/(len(items) - 1), 3))

  #Playfair:
def playfair():
  def encode(grid: str, pair: str, offset = 1) -> str:
    pos1 = grid.index(pair[0])
    pos2 = grid.index(pair[1])
    if pos1 == pos2:
      pos2 = grid.index("&")
    if pos1 == pos2:
      # Plaintext &&
      return pair
    if pos1 // 7 == pos2 // 7:
      # Same row
      return grid[(pos1 // 7) * 7 + ((pos1 + offset) % 7)] + grid[(pos2 // 7) * 7 + ((pos2 + offset) % 7)]
    if pos1 % 7 == pos2 % 7:
      # Same column
      return grid[(((pos1 // 7) + offset) % 7)  * 7 + (pos1 % 7)] + grid[(((pos2 // 7) + offset) % 7) * 7 + (pos2 % 7)]
    
    return grid[(pos1 // 7) * 7 + (pos2 % 7)] + grid[(pos2 // 7) * 7 + (pos1 % 7)]


  alphabet = "0123456789abcdefghijklmnopqrstuvwxyz .,'\"!?:;()@&"
  
  codephrase = input().lower()
  plaintext = input().lower()
  
  grid = ""
  remaining = alphabet
  for letter in codephrase:
    if letter in remaining:
      grid += letter
      pos = remaining.index(letter)
      remaining = remaining[:pos] + remaining[(pos + 1):]
  grid += remaining
  
  pairs = ""
  for letter in plaintext:
    if letter in alphabet:
      pairs += letter
  if len(pairs) % 2 != 0:
    pairs += " "
  
  codetext = ""
  while len(pairs) > 0:
    pair = pairs[0:2]
    encoded = encode(grid, pair)
    print(pair, encoded)
    codetext += encoded
    pairs = pairs[2:]
  
  print(codetext)


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

  #Oddsevens recursively:
def oddsevens_recursive():
  def is_even(number):
    return True if number == 0 else is_odd(number - 1)
  
  def is_odd(number):
    return False if number == 0 else is_even(number - 1)

  #Factorial_recursive:
def factorial_recursive():
  def factorial_recursive(n):
    if n <= 1:
      return 1
    return n * factorial_recursive(n - 1)


  print("Please enter a number")
  number = int(input())
  print(str(number) + "! = " + str(factorial_recursive(number)))

  #Power_recursive:
def power_recursive():
  def power(g, m):
    if m == 0:
      return 1
    return g * power(g, m - 1)

  #Sudoku-solver:
def sudoku_solver():
  def print_sudoku(sudoku):
    for block in range(0,3):
      for row in range(block,block+3):
        print(" ".join(str(value) for value in sudoku[row][0:3]), end=" | ")
        print(" ".join(str(value) for value in sudoku[row][3:6]), end=" | ")
        print(" ".join(str(value) for value in sudoku[row][6:9]))
      if block != 2:
          print("-" *21)
  
  
  def is_valid_digit(sudoku, row, column, digit):
    for i in range(9):
      if sudoku[row][i] == digit:
        return False
      if sudoku[i][column] == digit:
        return False
    block_row = row - row % 3
    block_column = column - column % 3
    for x in range(3):
      for y in range(3):
        if sudoku[x + block_row][y + block_column] == digit:
          return False
    return True
  
  
  def solve_sudoku(sudoku, row, column):
    if column >= len(sudoku):
      column = 0
      row += 1
    if row >= len(sudoku):
      print_sudoku(sudoku)
      return
    if sudoku[row][column] != 0:
      solve_sudoku(sudoku, row, column + 1)
    else:
      for digit in range(1,10):
        if is_valid_digit(sudoku, row, column, digit):
          sudoku[row][column] = digit
          solve_sudoku(sudoku, row, column + 1)
          sudoku[row][column] = 0
  
  sudoku = [[6, 0, 3, 4, 0, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 4, 7, 0],
            [0, 7, 1, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 7, 0, 4, 0, 2, 0],
            [0, 2, 5, 0, 3, 0, 7, 1, 0],
            [0, 0, 4, 8, 0, 0, 9, 0, 0],
            [0, 6, 9, 0, 0, 0, 2, 0, 8],
            [0, 0, 8, 0, 0, 9, 1, 4, 0],
            [1, 0, 7, 0, 0, 0, 3, 0, 9]]
  
  solve_sudoku(sudoku, 0, 0)

#Week 7:
  #Rebasing (Lecturers method):
def rebasing_lec():
  def rebase(number: str, base_original: int, base_target: int, alphabet: str = "0123456789abcdefghijklmnopqrstuvwxyz") -> str:
    value = 0
    for character in number:
      value = value * base_original + alphabet.find(character)
    number = ""
    while value > 0:
      number = alphabet[value % base_target] + number
      value //= base_target
    return number


  number = input()
  base_original = int(input())
  base_target = int(input())
  number = rebase(number, base_original, base_target)
  if number != "":
      print(number)
  else:
      print(0)
          
#Rebasing (Tutor's method):
def rebasing_tut():
  x = input()
  old_base = int(input())
  new_base = int(input())
  
  # Define the base symbols (up to base 36)
  base = "0123456789abcdefghijklmnopqrstuvwxyz"
  
  # Convert the input to base 10
  base10 = int(x, old_base)
  
  # function to convert from base 10 to new base
  def convert_to_new(number, new):
      base_inter = []
      while number > 0:
          remain = number % new
          base_inter.append(remain)
          number //= new
      return base_inter[::-1]
  
  # calling the function
  new_val = convert_to_new(base10, new_base)
  
  # Create the output string from the new base digits
  new_output = ''
  for i in new_val:
      new_output += base[i]
  
  print("Converted number:", new_output)

  #Letter-count with dictionary:
def letter_count_dict():
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  letter_counts = {}
  print("Please enter a text:")
  for letter in input():
    if letter.lower() in alphabet:
      if letter.lower() in letter_counts:
        letter_counts[letter.lower()] += 1
      else:
        letter_counts[letter.lower()] = 0
        
  for letter in letter_counts:
    print(letter + ": " + str(letter_counts[letter]))

  #Maximum of sequence using tuples:
def get_maximum(seq: list[int]) -> (int, int):
  maximum_value: int = seq[0]
  maximum_index: int = 0
  for i, value in enumerate(seq):
    if value > maximum_value:
      maximum_value = value
      maximum_index = i
  return maximum_index, maximum_value


sequence: list[int] = [int(term) for term in input().split()]
index, value = get_maximum(sequence)
print("The maximum value of", value, "is achieved at position", index)

#Week 11:

  #Tricky cubes:
def tricky_cubes():
  n, m = [int(k) for k in input().split()]
  count = 0
  k = 0
  while k**3 < n:
      k += 1
  while k**3 <= m:
      k += 1
      count += 1
  print(count)

  #Mastermind:
  def get_clues(guess: str, code: str) -> tuple[int, int]:
    i = len(guess) - 1
    correct = 0
    while i >= 0:
        if guess[i] == code[i]:
            guess = guess[:i] + guess[i+1:]
            code = code[:i] + code[i + 1:]
            correct += 1
        i -= 1
    i = len(guess) - 1
    misplaced = 0
    while i >= 0:
        if code.find(guess[i]) >= 0:
            pos = code.find(guess[i])
            guess = guess[:i] + guess[i+1:]
            code = code[:pos] + code[pos + 1:]
            misplaced += 1
        i -= 1
    return correct, misplaced


  def check_possibility(code: str) -> bool:
    for clue in clues:
        information = get_clues(code, clue[0])
        if information[0] != clue[1] or information[1] != clue[2]:
            return False
    return True

  def generate_codes(length: int, code: str = "") -> int:
    count = 0
    if len(code) < length:
        for letter in alphabet:
            count += generate_codes(length, code + letter)
        return count
    if check_possibility(code):
        return 1
    return 0


  alphabet = "abcdefghijklmnopqrstuvwxyz"
  clues = []
  line = input()
  answer = ""
  while line != "":
      clues.append(line.split())
      clues[-1][1] = int(clues[-1][1])
      clues[-1][2] = int(clues[-1][2])
      if clues[-1][1] == 0 and clues[-1][2] == 0:
          for letter in clues[-1][0]:
              pos = alphabet.find(letter)
              if pos >= 0:
                  alphabet = alphabet[:pos] + alphabet[pos+1:]
      if clues[-1][1] == len(clues[-1][0]):
          answer = clues[-1][0]
      line = input()
  if answer != "":
      if check_possibility(answer):
          print(1)
      else:
          print(0)
  else:
      print(generate_codes(len(clues[0][0])))


  #Week 12
    #Flipping coins:

import math

n = int(input())
print(n - math.isqrt(n))

    #Scheduling nightmare:

def get_optimal_assignment_value(matrix: list[list], current_line = 0, taken: list = []):
    """
    Returns the optimal satisfaction given a matrix of satisfactions
    :param matrix: Matrix of individual (row) satisfactions for being assigned tasks (column),
                   or X if satisfaction is minus infinity
    :param current_line: Current individual being assigned a task
    :param taken: Which tasks have already been taken
    :return:
    """
    if current_line >= len(matrix):
        return 0
    current_best = 0
    possible = False
    for option in range(len(matrix[current_line])):
        # For each possible task
        if option not in taken and matrix[current_line][option] != "X":
            # If the task is not taken, and assignment of
            # individual current_line to option is possible,
            # find the best assignment of future individuals
            value = get_optimal_assignment_value(matrix, current_line + 1, taken + [option])
            if value >= 0 and value + matrix[current_line][option] >= current_best:
                # If such an assignment of future individuals is possible
                # and leads to a better satisfaction than currently known,
                # update the satisfaction value
                possible = True
                current_best = value + matrix[current_line][option]
    if possible:
        # If we have found a possible assignment,
        # return the best we found
        return current_best
    # Impossible assignment reached
    return -1

matrix = []
matrix.append([value if value == "X" else int(value) for value in input().split()])
while len(matrix) < len(matrix[0]):
    matrix.append([value if value == "X" else int(value) for value in input().split()])

best_value = get_optimal_assignment_value(matrix)
if best_value >= 0:
    print(best_value)
else:
    print("IMPOSSIBLE")
  
def generate_subsets(s):
    if s == "":
        return [""]
    smaller_subsets = generate_subsets(s[1:])
    return smaller_subsets + [s[0] + subset for subset in smaller_subsets]
"""
Sorting algorithms:
!! Assume worst time-complexity !!

| Algorithm       | Worst            | Best             | Average          | Space  |
| --------------- | ---------------- | ---------------- | ---------------- | ------ |
| Selection sort  | O(n^2)           | O(n^2)           | O(n^2)           | O(1)   |
| Insertion sort  | O(n^2)           | O(n)             | O(n^2)           | O(1)   |
| Bubble sort     | O(n^2)           | O(n)             | O(n^2)           | O(1)   |
| Merge sort      | O(n*log(n))      | O(n*log(n))      | O(n*log(n))      | O(n)   |
| Quicksort       | O(n^2)           | O(n*log(n))      | O(n*log(n))      | O(1)   |
| Counting sort   | O(n+k)           | O(n+k)           | O(n+k)           | O(k)   |
| Radix sort      | O(log_r(k)(n+r)) | O(log_r(k)(n+r)) | O(log_r(k)(n+r)) | O(n+r) |
"""

# Selection sort
def selection_sorting_algorithm():
  def swap_elements(sequence: list[int], x: int, y: int) -> None:
    temp_element = sequence[x]
    sequence[x] = sequence[y]
    sequence[y] = temp_element


  def selection_sort(sequence: list[int]) -> None:
    for i in range(len(sequence)):
        minimum_index = i
        for j in range(i+1, len(sequence)):
            if sequence[j] < sequence[minimum_index]:
                minimum_index = j
        swap_elements(sequence, i, minimum_index)

#Insertion sort
def intersection_sorting_algorithm():
  def insertion_sort(sequence: list[int]) -> None:
    for i in range(1, len(sequence)):
        value = i
        j = i
        while j > 0 and sequence[j - 1] > value:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = value

#Bubble sort
def bubble_sorting_algorithm():
  def swap_elements(sequence: list[int], x: int, y: int) -> None:
    temp_element = sequence[x]
    sequence[x] = sequence[y]
    sequence[y] = temp_element

  def bubble_sort(sequence: list[int]) -> None:
    for right in range(len(sequence), 0, -1):
      for i in range(1, right):
        if sequence[i - 1] > sequence[i]:
          swap_elements(sequence, i, i - 1)

#Merge sort
def merge_sorting_algorithm():
  def merge(sequence: list[int], midpoint: int) -> list[int]:
    left = 0
    right = midpoint
    mergedList = [0] * len(sequence)
    for position in range(len(mergedList)):
      if left < midpoint:
        if right < len(sequence) and sequence[left] > sequence[right]:
          mergedList[position] = sequence[right]
          right += 1
        else:
          mergedList[position] = sequence[left]
          left += 1
      else:
        mergedList[position] = sequence[right]
        right += 1
    return mergedList

  def merge_sort(sequence: list[int]) -> list[int]:
    if len(sequence) == 1:
      return sequence
    midpoint = len(sequence) // 2
    sequence = merge_sort(sequence[:midpoint]) + merge_sort(sequence[midpoint:])
    return merge(sequence, midpoint)
  
# Quick sort
def quick_sorting_algorithm():
  def swap_elements(sequence: list[int], x: int, y: int) -> None:
    temp_element = sequence[x]
    sequence[x] = sequence[y]
    sequence[y] = temp_element

  def quicksort(sequence: list[int], start: int = 0, end: int = -1) -> None:
    if end < 0:
      end = len(sequence)
    if end - start <= 1:
      return
    pivot = sequence[start]
    left = start + 1
    right = end - 1
    while left <= right:
      while left <= right and sequence[left] <= pivot:
        left += 1
        while left <= right and sequence[right] > pivot:
          right -= 1
        if left < right:
          swap_elements(sequence, left, right)
    swap_elements(sequence, start, left - 1)
    quicksort(sequence, start, left - 1)
    quicksort(sequence, left, end)

# Shell sort (Varaition on insertion sort)
def shell_sorting_algorithm():
  def swap_elements(sequence: list[int], x: int, y: int) -> None:
    temp_element = sequence[x]
    sequence[x] = sequence[y]
    sequence[y] = temp_element

  def shellsort(sequence: list[int]) -> None:
    gap = len(sequence) // 2
    while gap > 0:
      for position in range(gap, len(sequence)):
        i = position
        while i >= gap and sequence[i - gap] > sequence[i]:
          swap_elements(sequence, i - gap, i)
          i -= gap
      gap //= 2

# Shaker sort (Variation bubble sort)
def shaker_sorting_algorithm():
  def swap_elements(sequence: list[int], x: int, y: int) -> None:
    temp_element = sequence[x]
    sequence[x] = sequence[y]
    sequence[y] = temp_element

  def shaker_sort(sequence: list[int]) -> None:
    left = 0
    right = len(sequence)
    while left < right:
      for i in range(left + 1, right):
        if sequence[i - 1] > sequence[i]:
          swap_elements(sequence, i, i - 1)
      right -= 1
      for i in range(right - 1, left, -1):
        if sequence[i - 1] > sequence[i]:
          swap_elements(sequence, i, i - 1)
      left += 1

# Counting sort
def counting_sorting_algorithm():
  MAX_NUMBER = 1001

  def counting_sort(sequence: list[int]) -> None:
    tally = [0] * MAX_NUMBER
    for value in sequence:
      tally[value] += 1
    position = 0
    for value in range(len(tally)):
      while tally[value] > 0:
        sequence[position] = value
        position += 1
        tally[value] -= 1

def radix_sorting_algorithm():
  MAX_NUMBER = 1000000000
  RADIX = 10


  def counting_sort(sequence: list[int], factor: int = 1) -> None:
    output = [0] * len(sequence)
    tally = [0] * RADIX
    for value in sequence:
      tally[(value // factor) % RADIX] += 1
    for i in range(1, RADIX):
      tally[i] += tally[i - 1]
    position = len(sequence) - 1
    while position >= 0:
      tally_position = (sequence[position] // factor) % RADIX
      tally[tally_position] -= 1
      output[tally[tally_position]] = sequence[position]
      position -= 1
    for position in range(len(sequence)):
      sequence[position] = output[position]


  def radix_sort(sequence: list[int]) -> None:
    factor = 1
    while factor < MAX_NUMBER:
      counting_sort(sequence, factor)
      factor *= RADIX

"""
Recursion General Functions:
"""

# Calculate sum of numbers from 1 to n
def sum_to_n(n):
  if n == 0:
    return 0
  return n + sum_to_n(n-1)


# Amount of characters in a string
def count_characters(s):
  if s == "":
    return 0
  return 1 + count_characters(s[1:])

# Check if string is a palindrome
def is_palindrome(s):
  if len(s) <= 1:
    return True
  return s[0] == s[-1] and is_palindrome(s[1:-1])

# Reverse a string
def reverse_string(s):
  if s == "":
    return ""
  return s[-1] + reverse_string(s[:-1])

# Count number of vowels in a string
def count_vowels(s):
  vowels = "aeiouAEIOU"
  if s == "":
    return 0
  return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

# Generate all subsets of a string
# Output: ['', 'c', 'b', 'bc', 'a', 'ac', 'ab', 'abc']
def generate_subsets(s):
  if s == "":
    return [""]
  smaller_subsets = generate_subsets(s[1:])
  return smaller_subsets + [s[0] + subset for subset in smaller_subsets]

#n-th item in a Fibonacci sequence
def fibonacci(n):
  if n == 0:
    return 0
  if n == 1:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

# Generate all permutations of a given number
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
def generate_permutations(nums):
  if len(nums) == 0:
    return [[]]
  permutations = []
  for i in range(len(nums)):
    rest = nums[:i] + nums[i+1:]
    for perm in generate_permutations(rest):
      permutations.append([nums[i]] + perm)
  return permutations

# Vignere cipher
# Explanation: The Vigenère cipher is a method of encrypting alphabetic text where each letter of the plaintext is encoded with a different Caesar cipher, whose increment is determined by the corresponding letter of another text, the key.

def vigenere_cipher(text, key, encrypt=True):
  def shift(c, k, encrypt):
    if not c.isalpha():
      return c
    base = 'A' if c.isupper() else 'a'
    offset = ord(k.upper() if c.isupper() else k.lower()) - ord(base)
    if not encrypt:
      offset = -offset
    return chr((ord(c) - ord(base) + offset) % 26 + ord(base))

  def recursive_cipher(t, k):
    if not t:
      return ""
    current_shift = shift(t[0], k[0], encrypt) if t[0].isalpha() else t[0]
    return current_shift + recursive_cipher(t[1:], k[1:] + k[0] if len(k) > 1 else k)

  return recursive_cipher(text, key)

# Double vowels:
def double_vowels(s):
  vowels = "aeiouAEIOU"
  if s == "":
    return ""
  return (s[0] * 2 if s[0] in vowels else s[0]) + double_vowels(s[1:])

# Expand a run-length encoding
# Explaination: Run-length encoding is a form of lossless data compression in which runs of data are stored as a single occurrence of that data value and a count of its consecutive occurrences, rather than as the original run.

def expand_run_length_encoded_string(s):
  if not s:
    return ""
  num = ""
  i = 0
  while i < len(s) and s[i].isdigit():
    num += s[i]
    i += 1
  return (s[i] * int(num)) + expand_run_length_encoded_string(s[i+1:]) if num else ""

# Check if array is sorted
def is_sorted(arr):
  if len(arr) <= 1:
    return True
  return arr[0] <= arr[1] and is_sorted(arr[1:])

# Infix to postfix
def infix_to_postfix(exp):
  precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

  def helper(tokens, stack=[]):
    if not tokens:  # Base case: No more tokens
      return "".join(stack[::-1])  # Remaining operators in stack are appended to the result in reverse order

    token = tokens[0]

    # Case 1: Operand (alphabet or digit)
    if token.isalnum():
      return token + helper(tokens[1:], stack)

    # Case 2: Left Parenthesis
    elif token == '(':
      return helper(tokens[1:], ['('] + stack)

    # Case 3: Right Parenthesis
    elif token == ')':
      result = ""
      while stack and stack[-1] != '(':
        result += stack.pop()
      stack.pop()  # Remove the '(' from stack
      return result + helper(tokens[1:], stack)

    # Case 4: Operator
    else:
      result = ""
      while (stack and stack[-1] != '(' and
            precedence.get(stack[-1], 0) >= precedence.get(token, 0)):
        result += stack.pop()
      stack.append(token)
      return result + helper(tokens[1:], stack)

  # Split input into tokens and process them recursively
  return helper(list(exp))

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
Methods

!!!Note that unless "Returns" is included, the methods do not return any value but modify the original !!
"""

#Built in functions:
def built_functions():
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
  type() #-> Returns type   of input

#String methods - str = string:
def string_methods():
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
  str.translate(d) #-> Replace every key of d in the string with the value of the key, d must be a dicitonary and the keys and values must be ascii
  str.upper() #-> Convert string into uppercase

#List methods - list = last:
def list_methods():
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
def dictionary_methods():
  dct.clear() #-> Remove all element from original dictionary
  dct.copy() #-> Returns copy of original dictionary
  dict.fromkeys(x, y) #-> Returns a dictionary with specificied keys and values
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
def tuple_methods():
  tpl.count(x) #-> Returns number of times "x" occurs in tuple
  tpl.index(x) #-> Returns index of first occurance of "x" in tuple --> Error if not found

#Set methods - set = set:
def set_methods():
   set.add(x) #-> Adds x to set
   set.clear() #-> Empties set
   set.copy() #-> Returns copy of set
   set.difference(set2) #-> Returns what is in set but not in set2
   set.difference_update(set2) #-> Removes all items in set that are also included in set2
   set.discard(x) #-> Removes x from set
   set.intersection(set2) #-> Returns a set that is the intersection of set and set2
   set.intersection_update(set2) #-> Removes items in set that are not in set2
   set.isdisjoint(set2) #-> Returns whether set and set2 have an intersection
   set.issubset(set2) #-> Returns True if all items in the set exist in set2, otherwise false
   set.issuperset(set2) #-> Returns True if all items in set2 exist in set1, otherwise False
   set.pop() #-> Remove random item from set
   set.remove(x) #-> Removes x from set
   set.symmetric_difference() #-> Returns a set with all items from both sets but not items present in both sets
   set.symmetric_difference_update() #-> Insert symmetric differences from set and set2
   set.union(set2) #-> Returns a set with union of set and set2
   set.update(set2) #-> Update set with union of this set and set2

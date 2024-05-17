# This time we want to write calculations using functions and get the results.
# Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

##### submitted
# # numbers
# def zero(sum = []):
#   if not sum:
#     return [0]
#   else:
#     match sum[1]:
#       case '+':
#         ans = sum[0]
#       case '-':
#         ans = 0 - sum[0]
#       case '*':
#         ans = 0
#       case '/':
#         ans = 0 // sum[0]
#     return ans
  
# def one(sum = []):
#   if not sum:
#     return [1]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 1 + sum[0]
#       case '-':
#         ans = 1 - sum[0]
#       case '*':
#         ans = sum[0]
#       case '/':
#         ans = 1 // sum[0]
#     return ans

# def two(sum = []):
#   if not sum:
#     return [2]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 2 + sum[0]
#       case '-':
#         ans = 2 - sum[0]
#       case '*':
#         ans = 2 * sum[0]
#       case '/':
#         ans = 2 // sum[0]
#     return ans

# def three(sum = []):
#   if not sum:
#     return [3]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 3 + sum[0]
#       case '-':
#         ans = 3 - sum[0]
#       case '*':
#         ans = 3 * sum[0]
#       case '/':
#         ans = 3 // sum[0]
#     return ans

# def four(sum = []):
#   if not sum:
#     return [4]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 4 + sum[0]
#       case '-':
#         ans = 4 - sum[0]
#       case '*':
#         ans = 4 * sum[0]
#       case '/':
#         ans = 4 // sum[0]
#     return ans

# def five(sum = []):
#   if not sum:
#     return [5]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 5 + sum[0]
#       case '-':
#         ans = 5 - sum[0]
#       case '*':
#         ans = 5 * sum[0]
#       case '/':
#         ans = 5 // sum[0]
#     return ans

# def six(sum = []):
#   if not sum:
#     return [6]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 6 + sum[0]
#       case '-':
#         ans = 6 - sum[0]
#       case '*':
#         ans = 6 * sum[0]
#       case '/':
#         ans = 6 // sum[0]
#     return ans

# def seven(sum = []):
#   if not sum:
#     return [7]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 7 + sum[0]
#       case '-':
#         ans = 7 - sum[0]
#       case '*':
#         ans = 7 * sum[0]
#       case '/':
#         ans = 7 // sum[0]
#     return ans

# def eight(sum = []):
#   if not sum:
#     return [8]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 8 + sum[0]
#       case '-':
#         ans = 8 - sum[0]
#       case '*':
#         ans = 8 * sum[0]
#       case '/':
#         ans = 8 // sum[0]
#     return ans

# def nine(sum = []):
#   if not sum:
#     return [9]
#   else:
#     match sum[1]:
#       case '+':
#         ans = 9 + sum[0]
#       case '-':
#         ans = 9 - sum[0]
#       case '*':
#         ans = 9 * sum[0]
#       case '/':
#         ans = 9 // sum[0]
#     return ans

# # operations
# def plus(sum):
#   sum.append('+')
#   return sum

# def minus(sum):
#   sum.append('-')
#   return sum

# def times(sum):
#   sum.append('*')
#   return sum

# def divided_by(sum):
#   sum.append('/')
#   return sum

# print(four(plus(nine())))

##### revised
def zero(f=None): return 0 if not f else f(0)
def one(f=None): return 1 if not f else f(1)
def two(f=None): return 2 if not f else f(2)
def three(f=None): return 3 if not f else f(3)
def four(f=None): return 4 if not f else f(4)
def five(f=None): return 5 if not f else f(5)
def six(f=None): return 6 if not f else f(6)
def seven(f=None): return 7 if not f else f(7)
def eight(f=None): return 8 if not f else f(8)
def nine(f=None): return 9 if not f else f(9)

def plus(n): return lambda a: a + n
def minus(n): return lambda a: a - n
def times(n): return lambda a: a * n
def divided_by(n): return lambda a: a // n

print(five(times(eight())))
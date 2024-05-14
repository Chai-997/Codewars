# Check to see if a string has the same amount of 'x's and 'o's.
# The method must return a boolean and be case insensitive.
# The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

##### submitted
# def xo(s):
#     chars = list(s.lower())
#     result = False
#     x = chars.count('x')
#     o = chars.count('o')
#     if x == o:
#         result = True
#     return result

# print(xo("ooxxxgsdf"))

##### revised
def xo(s):
    chars = s.lower()
    return chars.count('x') == chars.count('o')

print(xo("ooxxgsdf"))
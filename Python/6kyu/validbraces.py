# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, but introduces new characters:
# brackets [], and curly braces {}. Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are matched with the correct brace.

# Examples
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False

##### submitted
# def valid_braces(string):
#     check = []
#     valid = True
#     try:
#         for c in string:
#             if c == "(" or c == "[" or c == "{":
#                 check.append(c)
#             elif c == ")" and check[-1] == "(":
#                 check = check[:-1]
#             elif c == "]" and check[-1] == "[":
#                 check = check[:-1]
#             elif c == "}" and check[-1] == "{":
#                 check = check[:-1]
#             else:
#                 valid = False
#     except:
#         valid = False

#     if len(check) != 0:
#         valid = False

#     return valid


# print(valid_braces("(((({{"))


##### revised
def valid_braces(string):
    while "()" in string or "[]" in string or "{}" in string:
        string = string.replace("()", "")
        string = string.replace("[]", "")
        string = string.replace("{}", "")
    return string == ""


print(valid_braces("(((({{"))

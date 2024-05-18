# In this kata we want to convert a string into an integer.
# The strings simply represent the numbers in words.

# Examples:

# "one" => 1
# "twenty" => 20
# "two hundred forty-six" => 246
# "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
# Additional Notes:

# The minimum number is "zero" (inclusively)
# The maximum number, which must be supported is 1 million (inclusively)
# The "and" in e.g. "one hundred and twenty-four" is optional,
# in some cases it's present and in others it's not
# All tested numbers are valid, you don't need to validate them

def parse_int(string):
    print(string)
    numwords = {}
    units = [
      "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
      "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
      "sixteen", "seventeen", "eighteen", "nineteen",
    ]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["hundred", "thousand", "million"]

    for i, word in enumerate(units): numwords[word] = (1, i)
    for i, word in enumerate(tens): numwords[word] = (1, i * 10)
    for i, word in enumerate(scales): numwords[word] = (10 ** (i * 3 or 2), 0)

    current = result = 0
    for word in string.replace(" and ", ' ').replace('-', ' ').split(' '):
        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

print(parse_int("one thousand three hundred and thirty-seven"))
#100031337
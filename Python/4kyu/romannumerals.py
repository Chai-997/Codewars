# Write two functions that convert a roman numeral to and from an integer value.
# Multiple roman numeral values will be tested for each function.

# Modern Roman numerals are written by expressing each digit separately starting
# with the left most digit and skipping any digit with a value of zero.
# In Roman numerals:

# 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
# 2008 is written as 2000=MM, 8=VIII; or MMVIII
# 1666 uses each Roman symbol in descending order: MDCLXVI.
# Input range : 1 <= n < 4000

# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
#   86 -> "LXXXVI"
#    1 -> "I"

# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "LXXXVI"  ->   86
# "I"       ->    1
# Help
# +--------+-------+
# | Symbol | Value |
# +--------+-------+
# |    M   |  1000 |
# |   CM   |   900 |
# |    D   |   500 |
# |   CD   |   400 |
# |    C   |   100 |
# |   XC   |    90 |
# |    L   |    50 |
# |   XL   |    40 |
# |    X   |    10 |
# |   IX   |     9 |
# |    V   |     5 |
# |   IV   |     4 |
# |    I   |     1 |
# +--------+-------+

class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        ans = ''
        num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        i = 0
        while  val > 0:
            for _ in range(val // num[i]):
                ans += syb[i]
                val -= num[i]
            i += 1
        return ans

    @staticmethod
    def from_roman(roman_num : str) -> int:
        ans = 0
        num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(roman_num)):
            try:
                if syb.index(roman_num[i+1]) < syb.index(roman_num[i]):
                    ans -= num[syb.index(roman_num[i])]
                else:
                    ans += num[syb.index(roman_num[i])]
            except:
                ans += num[syb.index(roman_num[i])]
        return ans
    

print(RomanNumerals.to_roman(4))
print(RomanNumerals.from_roman('IV'))
# There is an array with some numbers.
# All numbers are equal except for one. Try to find it!

# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.

# This is the first kata in series:

# Find the unique number (this kata)

##### submitted
# def find_uniq(arr):
#     n = False
#     uniques = set(arr)
#     for value in uniques:
#         if arr.count(value) == 1:
#             n = value
#             break
#     return n

# print(find_uniq([ 3, 10, 3, 3, 3 ]))

##### revised
def find_uniq(arr):
    a, b = set(arr)
    return a if arr.count(a) == 1 else b

print(find_uniq([ 3, 10, 3, 3, 3 ]))
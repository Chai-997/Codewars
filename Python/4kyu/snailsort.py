# Given an n x n array, return the array elements arranged from outermost elements
# to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:


# NOTE: The idea is not sort the elements from the lowest value to the highest;
# the idea is to traverse the 2-d array in a clockwise snailshell pattern.

# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

def snail(snail_map):
    elems = len(snail_map) * len(snail_map)
    sorted = []
    top = False

    while len(sorted) != elems and elems != 1:
        if top == False:
            for i in range(len(snail_map[0])): # right
                sorted.append(snail_map[0][i])
            snail_map.pop(0)
            top = True
        else:
            for i in range(len(snail_map)): # down
                sorted.append(snail_map[i].pop(-1))
            snail_map[-1].reverse()

            for i in range(len(snail_map[-1])): # left
                sorted.append(snail_map[-1][i])
            snail_map.pop(-1)

            for i in range(len(snail_map)): # up
                sorted.append(snail_map[-(i+1)].pop(0))
            top = False

    return snail_map[0] if elems == 1 else sorted

print(snail([ [1, 2, 3, 4],
              [12,13,14,5],
              [11,16,15,6],
              [10,9, 8, 7]]))

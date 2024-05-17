# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

##### submitted
# def find_short(text):
#     text = list(text.split())
#     lengths = []
#     for val in text:
#         lengths.append(len(val))
#     return min(lengths)

# print(find_short("bitcoin take over the world maybe who knows perhaps"))

##### revised
def find_short(s):
    return min(len(x) for x in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))
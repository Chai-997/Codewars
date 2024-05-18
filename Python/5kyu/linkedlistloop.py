# You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

# For example in the following picture the size of the dangling piece is 3 and the loop size is 12:

# Use the `next' attribute to get the following node
# node.next

def loop_size(node):
    seen = set()
    fulllist = []
    looped = False
    while looped == False:
        fulllist.append(node)
        seen.add(node)
        node = node.next
        
        if node in seen:
            ans = len(fulllist) - fulllist.index(node)
            if ans == 0:
                ans = len(fulllist)              
            looped = True
    return ans
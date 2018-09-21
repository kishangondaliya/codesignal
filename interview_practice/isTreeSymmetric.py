#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     
#     

def is_palindrome(f):    
    i = 0
    while i < len(f)//2:
        if f[i] != f[len(f)-1 -i]:
            return False
        i +=1
    return True

def isTreeSymmetric(t):
    res = []    
    current_floor = []
    if t is None:
        return True
    
    if t and t.value:
        current_floor.append(t)
    floors = []
    while len(current_floor):
        next_floor = []
        f = []
        for n in current_floor:
            if n and n.value:
#                print("n:",n.value)
                f.append(n.value)
            if n is None:
                f.append("!")
            if n and n.left:
                next_floor.append(n.left)
            if n and n.left is None:
                next_floor.append(None)
            if  n and n.right:
                next_floor.append(n.right)
            if n and n.right is None:
                next_floor.append(None)
    #        print("next:",next_floor)
        current_floor =  next_floor
        floors.append(f)


    for f in floors:
        if is_palindrome(f) is False:
            return False
    return True
    

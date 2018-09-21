#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
#     
def largestValuesInTreeRows(t):
    current_floor = [t]
    res = []
    while len(current_floor):

        next_floor = []
        m = []
        for node in current_floor:
            # print("node:", node)
            if node and node.value:
                # print("root:", node.value)
                m.append(node.value)
            if node and node.left:
                # print("left :", node.left.value)
                
                next_floor.append(node.left)
            if node and node.right:
                # print("right:", node.right.value)
                next_floor.append(node.right)
        if len(m) > 0:
            res.append(max(m))
        current_floor = next_floor
    return res

#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None    

main_arr = []
res = []
def my_digit_tree_sum(t):
    
    if t is None:
        return
    res.insert(0, t.value)
    if t.left is None and t.right is None:
        main_arr.append(res[::-1])
        # print("res:", res)
    my_digit_tree_sum(t.left)
    my_digit_tree_sum(t.right)
    res.pop(0)


def digitTreeSum(t):
    my_digit_tree_sum(t)
    s = ""
    new_arr =[]
    for sub_arr in main_arr:
        s = ""
        for i in sub_arr:
            s += str(i)
        new_arr.append(s)
    new_arr = [int(e) for e in new_arr]
    return sum(new_arr)


import math

def packageBoxing(pkg, boxes):

    min_space = math.inf
    current_min_index = -1
    # print("Min space", min_space)
    pkg = sorted(pkg)
    for i, elem in enumerate(boxes):
        elem = sorted(elem)
        # if sorted(elem) == sorted(pkg):
        #     return i
        if pkg[0] <= elem[0] and pkg[1] <= elem[1] and pkg[2] <= elem[2]:
            if (elem[0] * elem[1] * elem[2]) < min_space :
                min_space = (elem[0] * elem[1] * elem[2])
                current_min_index = i
            
    
    return current_min_index

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
#
  
def add_zero_in_front(missing_zero):
    missing_zero = str(missing_zero)
    if len(missing_zero) == 1:
        return "000" + missing_zero
    elif len(missing_zero) == 2:
        return "00" + missing_zero
    elif len(missing_zero) == 3:
        return "0" + missing_zero
    else:
        return missing_zero
    
    
def addTwoHugeNumbers(a, b):
    
    tmpa =  a
    tmpb = b
    stra = ""
    strb = ""
    while tmpa:
        stra += add_zero_in_front(tmpa.value)
        tmpa = tmpa.next
    while tmpb:
        strb += add_zero_in_front(tmpb.value)
        tmpb = tmpb.next
    
    restmp = int(stra) + int(strb)
    res = []
    strres = str(restmp)
#    print("stres", strres)
    i = len(strres)-1
    j = 1
    res = []
    new_res = []
    while i >= 0:
        new_res.insert(0,strres[i])
        if j==4:
            res.insert(0,new_res)
            new_res = []
            j=0
        j+=1
        i -= 1
    if len(new_res):
        res.insert(0,new_res)
#    print("rs:",res)
    res2 = []
    for i in res:
        z = ""
        for e in i:
            z += e
        res2.append(int(z))
    return res2

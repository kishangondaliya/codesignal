# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    res = []
    
    while l1 and l2:
        if l1 and l2 and l1.value < l2.value:
            res.append(l1.value)
            l1 = l1.next
        if l1 and l2 and l2.value < l1.value:
            res.append(l2.value)
            l2 = l2.next
        if l1 and l2 and l1.value == l2.value:
            res.append(l1.value)
            res.append(l2.value)
            l1 = l1.next
            l2 = l2.next
        if  l1 and l2 is None:
            res.append(l1.value)
            l1 = l1.next
        if  l2  and l1 is None:
            res.append(l2.value)
            l2 = l2.next

    if l1 is None:
        while l2:
            res.append(l2.value)
            l2 = l2.next 
    if l2 is None:
        while l1:
            res.append(l1.value)
            l1 = l1.next 
    
    return res


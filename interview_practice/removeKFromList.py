# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
  
    if l is None:
        return []

    
    while l and l.value == k:
        l = l.next
    tmp = l
    while tmp:
        trailer = tmp
        tmp = tmp.next
        while tmp and (tmp.value == k):
            tmp = tmp.next
        trailer.next = tmp
        

        
    return l

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    tmp = l
    list_len = 0
    left = 0 
    right = 0
    while tmp:
        list_len += 1
        tmp = tmp.next
    tmp = l

    
    if list_len == 0 or list_len == 1:
        return True
    
    head = l
    i = 0
    if list_len % 2 == 0:
        current = head
        prev = None
        nn_next = None
        new_list = None
        while current and i < list_len//2:
            current_next = current.next
            nn_next = current.next
            current.next = prev
            prev = current
            current = current_next
            i += 1
        head = prev
        tmp =  head
        while tmp and nn_next:
            if tmp.value != nn_next.value:
                return False
            tmp = tmp.next
            nn_next = nn_next.next
        return True
    else:
        current = head
        prev = None
        nn_next = None
        new_list = None
        while current and i < list_len//2:
            current_next = current.next
            nn_next = current.next
            current.next = prev
            prev = current
            current = current_next
            i += 1
        head = prev
        nn_next = nn_next.next
        tmp =  head
        while tmp and nn_next:            
            if tmp.value != nn_next.value:
                return False
            tmp = tmp.next
            nn_next = nn_next.next
        return True
    return False

    

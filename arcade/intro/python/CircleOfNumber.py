
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    # def add_in_front(self, value):
    #     tmp = self.head
    #     n = Node(value)
    #     n.next = tmp
    #     self.head = n

    def add_in_end_list(self, value):
        tmp = self.head
        if tmp is None:
            n = Node(value)
            n.next = n
            self.head = n
        else:
            while tmp.next is not self.head:
                tmp = tmp.next
            #print("Tmp value:", tmp.value)
            n = Node(value)
            tmp.next = n
            n.next = self.head

    def traverse_linked_list(self):
        tmp = self.head
        print(self.head.value)
        while tmp.next != self.head:
            tmp = tmp.next
            print(tmp.value)

    def traverse_linked_list_n(self, current, n):
        tmp = self.head
        print(self.head.value)
        while tmp.value != current:
            tmp = tmp.next
        print("current node:", tmp.value)
        i = 0
        while i < n:
            tmp = tmp.next
            i += 1
        return tmp.value
        # print("res:",tmp.value)


# if __name__ == '__main__':
#     print("Start")
#     L = CircularLinkedList()
#     for i in range(10):
#         L.add_in_end_list(i)

#     L.traverse_linked_list_n(8, 5)





def circleOfNumbers(n, firstNumber):
    L = CircularLinkedList()
    for i in range(n):
        L.add_in_end_list(i)
    a = L.traverse_linked_list_n(firstNumber, n/2)  
    return a

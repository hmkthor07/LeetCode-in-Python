"""

A linked list where a node have pointers to both previous and next node.


"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def creatList(self, arr):

        start = self.head
        n = len(arr)
        i = 0

        while i<n:
            newNode = Node(arr[i])
            if (i == 0):
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i += 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while temp:
            linked_list += (str(temp.data) + " ")
            temp = temp.next

        print(linked_list)

# 1 -> 2 -> 3 -> 4 -> 5
arr = [1,2,3,4,5]

llist = LinkedList()
llist.creatList(arr)
llist.printList()

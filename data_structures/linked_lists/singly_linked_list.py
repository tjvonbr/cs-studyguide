class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def returnLength(self):
        return self.length

    def printList(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length = self.length + 1

    def append(self, value):
        new_node = Node(value)
        cur_node = self.head

        while cur_node.next != None:
            cur_node = cur_node.next
            
        cur_node.next = new_node
        self.length += 1

if __name__=="__main__":
    llist = SinglyLinkedList()
    llist.prepend(1)
    llist.prepend(2)
    llist.append(4)

    llist.printList()
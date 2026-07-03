class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self): # Initiating a linked list with two nodes from the get go
        # One dummy node at the beginning and another at the end
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def getPrev(self, index):
        # For most efficient solution, write a forward and backward solution
        if index <= self.size//2:
            cur = self.head
            for i in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size - index + 1):
                cur = cur.prev
        return cur

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getPrev(index).next.val        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        prev = self.getPrev(index)
        node = ListNode(val)
        node.prev = prev
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        prev = self.getPrev(index)
        cur = prev.next
        prev.next = cur.next
        cur.next.prev = prev
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
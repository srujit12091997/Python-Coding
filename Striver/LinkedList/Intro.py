class Node:
    def __init__(self, data1, next1 = None):
        self.data = data1
        self.next = next1
        
    def printLL(head):
        while head is not None:
            print(head.data, end ="")
            head = head.next
    def insertHead(head, val):
        temp = Node(val, head)
        return temp
    if __name__ == "__main__":
        arr = [12, 8, 5, 7]
        val = 100
        
        head = Node(arr[0])
        head.next =Node(arr[1])
        head.next.next = Node(arr[2])
        
        head = insertHead(head,val)
        printLL(head)
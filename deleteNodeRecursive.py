


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    inputList = [int(ele) for ele in input().split()]
    head = None
    for currentdata in inputList:
        if currentdata == -1:
            break
        newNode = Node(currentdata)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

def printll(head):
    while head is not None:
        print(str(head.data) ,"->", end = " ")
        head = head.next
    print("None")
    return

def deleteNodeRecursive(head, k):
    if k<0:
        return head
    if head == None:
        return None
    if k == 0:
        res = head.next
        return res
    head.next = deleteNodeRecursive(head.next, k-1)
    return head

head = takeInput()
print(printll(deleteNodeRecursive(head,4)))





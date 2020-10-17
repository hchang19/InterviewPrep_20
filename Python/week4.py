class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = head
        self.length = 0

    def addToEnd(self, val):
        tempNode = Node(val)
        if(self.head == None and self.head == self.tail):
            self.head = tempNode
            self.tail = tempNode
            return
        self.tail.next = tempNode
        self.tail = tempNode
        self.length += 1
    def isEmpty(self):
        return self.length == 0
    
    def addToFront(self, val):

        tempNode = Node(val)
        tempNode.next = self.head
        self.head = tempNode
        self.length += 1

    def printAllValues(self):
        tempPtr = self.head
        result = []
        while(tempPtr):
            result.append(tempPtr.val)
            tempPtr = tempPtr.next
        print(result)

    def deleteNode(self, val):
        #first check the head
        if(self.head.val == val):
            self.head = self.head.next
            return True
        ptr1 = None
        ptr2 = self.head
        while(ptr2):
            if(ptr2.val == val):
                if(ptr2.next == None):
                    self.tail = ptr1
                ptr1.next = ptr2.next
                return True

            ptr1 = ptr2
            ptr2 = ptr2.next
        
        return False


def printReverseIndex(head):
    counter = 0
    if(head == None):
        return 0
    counter = printReverseIndex(head.next) 
    print(counter,head.val)
    return counter + 1

def findMiddleValue(head):
    ptr1 = head
    ptr2 = head

    while(ptr2.next is not None and ptr2.next.next is not None):
        ptr1 = ptr1.next
        ptr2= ptr2.next.next
    
    return ptr1.val


def addTwoValueInLinkedList(head):
    if head is None:
        return 0
    
    if head.next is None:
        return head.val
    
    ptr1 = head
    ptr2 = head
    while(ptr2.next is not None and ptr2.next.next is not None):
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    print(ptr1.val)
    print(sumUpLinkedList(head, ptr1))
    print(sumUpLinkedList(ptr1))
    
    
def sumUpLinkedList(start, stop = None):
    if(start is None):
        return 0
    if(start.next is stop):
        return start.val
   
    result = start.val + (sumUpLinkedList(start.next, stop) * 10)
    return result

#123 + 555 should return 678 
# return [8,7,6]

def sumLists(head1, head2,carry=0):
    if(head1 is None):
        return head2
    if(head2 is None):
        return head1
    
    sum = head1.val + head2.val
    newHead = Node(sum%10)
    newHead.next = sumLists(head1.next, head2.next, 1 if sum >= 10 else 0)

    return newHead



def newTextEditor(operations):

    copyText = ''
    previousStates = []
    result = ''
    #Loop through and parse the operation
    for operation in operations:
        operation = operation.split(' ')
        
        opKey = operation[0]
        
        if(opKey == "UNDO"):
            if(previousStates):
                result = previousStates[-1]
                result = previousStates.pop()
            continue
        if(opKey == "COPY"):
            if(int(operation[1]) >= len(result)):
                copyText = ''
            else:
                copyText = result[int(operation[1]):]
            continue
            
        
        if(opKey == "INSERT"):
            previousStates.append(result)
            result += operation[1]
            
            continue
        if(opKey == "DELETE"):
            
            if(len(result) > 0):
                previousStates.append(result)
                result = result[:-1]
                
            continue
        
        if(opKey == "PASTE"):
            previousStates.append(result)
            result += copyText
            
            continue
    
    return result

operations1 =["INSERT Da", "COPY 0", "UNDO", "PASTE", 
            "PASTE", "COPY 2", "PASTE", "PASTE", "DELETE", "INSERT aaam"]

operations2= ["INSERT Code", "INSERT Signal", "DELETE", "UNDO"]

operations3 = ["INSERT a", 
 "DELETE", 
 "DELETE", 
 "COPY 0", 
 "UNDO", 
 "PASTE", 
 "UNDO", 
 "INSERT b", 
 "COPY 0", 
 "PASTE", 
 "COPY 2", 
 "PASTE", 
 "UNDO", 
 "DELETE", 
 "UNDO"]

print(operations3)
print(newTextEditor(operations3))
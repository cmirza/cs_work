# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def insertValueIntoSortedLinkedList(l, value):

    newNode = ListNode(value)
    
    # check if list is empty or if value should be inserted at the beginning
    if l is None or l.value > newNode.value:
        newNode.next = l
        return newNode
        
    # begin traversing list
    prevNode = l
    currNode = l.next
    
    # run loop until we reach none
    while currNode is not None:
        # if current node's value is larger, insert it
        if currNode.value > newNode.value:
            prevNode.next = newNode
            newNode.next = currNode
            return l
        # iterate nodes
        prevNode = currNode
        currNode = currNode.next
        
    # add item to the end
    prevNode.next = newNode
    return l

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    
    # instantiate a new node for the merged list
    mergedList = ListNode(0)
    # create current node for tail
    currNode = mergedList
    
    while True:
        # check if either list is empty, if so, add the other list
        if l1 is None:
            currNode.next=l2
            break
        if l2 is None:
            currNode.next= l1
            break

        # check values of lists, append the smallest value to the end of the merged list
        if l1.value <= l2.value:
            currNode.next =  l1
            l1 = l1.next
        else:
            currNode.next = l2
            l2 = l2.next
    
        # advance the node 
        currNode =  currNode.next
        
    # return the merged list
    return mergedList.next
def binaryTreeInOrderTraversal(root):

    if root is None:
        return []
        
    return binaryTreeInOrderTraversal(root.left) + [root.value] + binaryTreeInOrderTraversal(root.right)



def traverseTree(t):

    queue = [t]
    values = []
    
    while queue != []:
        current = queue.pop(0)
        
        if current != None:
            values.append(current.value)
            
            if current.left != None:
                queue.append(current.left)
                
            if current.right != None:
                queue.append(current.right)
                
    return values
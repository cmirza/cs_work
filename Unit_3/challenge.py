def csBSTRangeSum(root, lower, upper):
    
    # base case to check if there is an empty element
    if root == None:
        return 0
        
    # if the current value is less than the lower range, traverse to the right
    if root.value < lower:
        return csBSTRangeSum(root.right, lower, upper)
        
    # if the current value is greater than the upper range, traverse to the left
    if root.value > upper:
        return csBSTRangeSum(root.left, lower, upper);
    
    # return the sum of the searched values
    return root.value + csBSTRangeSum(root.right, lower, upper) + csBSTRangeSum(root.left, lower, upper)


def csBinaryTreeInvert(root):

    # base case
    if (root == None): 
        return
  
    temp = root  
        
    # recursive calls to traverse tree
    csBinaryTreeInvert(root.left)  
    csBinaryTreeInvert(root.right)  

    # swap the pointers on node
    temp = root.left  
    root.left = root.right  
    root.right = temp
        
    # return root
    return root


def csFindAllPathsFromAToB(graph):
    
    list = []
    
    def findpath(n = 0, root = [0]):
        if n < len(graph)-1:
            for i in graph[n]:
                findpath(i, root+[i])
        else:
            list.append(root)
            
    findpath()
    
    return list
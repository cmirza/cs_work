def get_max_depth(root):
    if root is None:
        return 0

    return 1 + max(get_max_depth(root.left), get_max_depth(root.right))

def balancedBinaryTree(root):

    if root is None:
        return True
        
    left = get_max_depth(root.left)
    right = get_max_depth(root.right)
    
    if ((left - right) <= 1) and balancedBinaryTree(root.left) is True and balancedBinaryTree(root.right) is True:
        return True
    
    return False

def minimumDepthBinaryTree(root):

    if root is None:
        return 0
        
    if root.left is None and root.right is None:
        return 1
        
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
        
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
        
        
    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1


#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Answer 1:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findMaxSubtreeSum(root):
    max_sum = float('-inf')  # Initialize the maximum sum to negative infinity
    _, max_sum = calculateSubtreeSum(root, max_sum)
    return max_sum

def calculateSubtreeSum(node, max_sum):
    if node is None:
        return 0, max_sum

    left_sum, max_sum = calculateSubtreeSum(node.left, max_sum)
    right_sum, max_sum = calculateSubtreeSum(node.right, max_sum)

    subtree_sum = node.val + left_sum + right_sum
    max_sum = max(max_sum, subtree_sum)

    return subtree_sum, max_sum


# In[2]:


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Find the maximum subtree sum
result = findMaxSubtreeSum(root)
print(result)


# In[3]:


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(-6)
root.right.right = TreeNode(2)

# Find the maximum subtree sum
result = findMaxSubtreeSum(root)
print(result)


# In[7]:


#Answer 2:

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insertIntoBST(root.left, value)
    else:
        root.right = insertIntoBST(root.right, value)

    return root

def constructBST(level_order):
    if not level_order:
        return None

    root = None
    for value in level_order:
        root = insertIntoBST(root, value)

    return root

def printBST(root, space=0):
    if root is None:
        return
    
    space += 10
    
    printBST(root.right, space)
    
    print(" " * space, root.val)
    
    printBST(root.left, space)


# In[9]:


level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(level_order)
printBST(root)


# In[23]:


#ANswer 3:

def canRepresentBST(arr):
    n = len(arr)

    # Check if the given array is empty
    if n == 0:
        return True

    # Check if the array is non-decreasing
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False

    return True


# In[25]:


arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
result1 = canRepresentBST(arr1)
print(result1)


# In[26]:


arr2 = [11, 6, 13, 5, 12, 10]
result2 = canRepresentBST(arr2)
print(result2)


# In[ ]:





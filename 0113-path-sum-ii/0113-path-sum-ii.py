# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result=[]
        helper(root, targetSum, [], result)
        return result
def helper(root, target, slate, result):
    if root is None:
        return
    if root.left is None and root.right is None:
        if target == root.val:
            slate.append(root.val)
            result.append(list(slate))
            slate.pop()
            return 
    slate.append(root.val)
    helper(root.left, target-root.val, slate, result)
    # slate.remove(root.val)
    helper(root.right, target-root.val, slate, result)
    slate.pop()


        
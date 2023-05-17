"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []
        stack = []

        if root is None:
            return result

        stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push child nodes in reverse order
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])

        return result
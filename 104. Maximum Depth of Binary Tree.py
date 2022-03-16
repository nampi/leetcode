# 3 solutions
# 1. recursive DFS O(n) -- unbalanced tree
# 2. iterative BFS - level ordered traversal
# 3. iterative DFS

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, node=None):
        self.val = val
        self.next = node


def max_depth_recursive_dfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth_recursive_dfs(root.left), max_depth_recursive_dfs(root.right))


def max_depth_iterative_bfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    q = deque([root])  # deque([root]), because TreeNode object is not iterable
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level


def max_depth_iterative_dfs(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    s = [(root, 1)]
    max_depth = 1
    while s:
        node, depth = s.pop()
        max_depth = max(max_depth, depth)
        if node.right:
            s.append((node.right, depth + 1))
        if node.left:
            s.append((node.left, depth + 1))
    return max_depth

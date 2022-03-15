# 3 solutions
# 1. recursive DFS O(n) -- unbalanced tree
# 2. iterative BFS - level ordered traversal
# 3. iterative DFS

def maxDepthRecursiveBfs(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def maxDepthIterativeBfs(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        q = deque([root])  # [] or deque
        # why deque([root]) and not deque(root)
        # TreeNode object is not iterable
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


def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
    if root is None:
        return 0

    s = [(root, 1)]
    maxDepth = 1
    while s:
        node, depth = s.pop()
        maxDepth = max(maxDepth, depth)
        if node.right:
            s.append((node.right, depth + 1))
        if node.left:
            s.append((node.left, depth + 1))
    return maxDepth
from utils.tools import *
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        out = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            out.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(out)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        out = data.split()
        bfs = [TreeNode(int(i)) if i != '#' else None for i in out]
        slow_idx = 0  # the id in array nodex
        fast_idx = 1  # the id in array bfs
        root = bfs[0]
        nodes = [root]
        while slow_idx < len(nodes):
            node = nodes[slow_idx]
            slow_idx += 1  # each time we handle one node in nodes
            node.left = bfs[fast_idx]
            node.right = bfs[fast_idx + 1]
            fast_idx += 2  # each time we only handle two nodes in bfs
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root


string = Codec().serialize(stringToTreeNode("[1,2,3,null,null,4,5]"))
print(string)
root = Codec().deserialize(string)
print(treeNodeToString(root))

from tools import *
from collections import defaultdict, deque


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        out = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            out.append(str(node.val) if node else '#')
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(out).rstrip(' #')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        out = data.split(" ")
        # once we have a non-none node, we definitely have its two children
        nodes_with_no = [TreeNode(int(o)) if o != '#' else None for o in out]
        nodes = [o for o in nodes_with_no if o]
        i, j = 0, 1
        while i < len(nodes):
            node = nodes[i]
            if j < len(nodes_with_no):
                node.left = nodes_with_no[j]
            if j + 1 < len(nodes_with_no):
                node.right = nodes_with_no[j + 1]
            i += 1
            j += 2

        return nodes_with_no[0]


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = stringToTreeNode("[1,2,3,null,null,4,5,6,7]")
stri = ser.serialize(root)
print(stri)
ans = deser.deserialize(stri)
print(treeNodeToString(ans))

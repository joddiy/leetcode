# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    class Codec:

        def serialize(self, root):
            """Encodes a tree to a single string.

            :type root: TreeNode
            :rtype: str
            """
            if root is None:
                return "[]"
            queue = [root]
            output = []
            while queue:
                node = queue.pop(0)
                if node:
                    output.append(str(node.val))
                    queue.extend([node.left, node.right])
                else:
                    output.append("null")
            print("[" + ",".join(output) + "]")
            return "[" + ",".join(output) + "]"

        def deserialize(self, data):
            """Decodes your encoded data to tree.

            :type data: str
            :rtype: TreeNode
            """
            if data == "[]":
                return None
            data = data[1:-1].split(",")
            length = len(data)
            root = TreeNode(data[0])
            queue = [(root, 0)]
            while queue:
                node, index = queue.pop(0)
                left_index = 2 * index + 1
                if left_index < length:
                    if data[left_index] != "null":
                        node.left = TreeNode(data[left_index])
                        queue.append([node.left, left_index])
                right_index = left_index + 1
                if right_index < length:
                    if data[right_index] != "null":
                        node.right = TreeNode(data[right_index])
                        queue.append([node.right, right_index])
            return root

    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')

        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        vals = iter(data.split())
        return doit()


# Your Codec object will be instantiated and called as such:
codec = Codec()
str = codec.serialize(codec.deserialize("[1,2,3,null,null,4,5]"))
print(str)

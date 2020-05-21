def allKindsOfNodeDepths(root):
	sumOfAllDepths = 0
	stack = [root]
	while len(stack) > 0:
		node = stack.pop()
		if node is None:
			continue
		sumOfAllDepths += nodeDepths(node)
		stack.append(node.left)
		stack.append(node.right)
	return sumOfAllDepths

def nodeDepths(node, depth=0):
	if node is None:
		return 0
	return depth + nodeDepths(node.left, depth + 1) + nodeDepths(node.right, depth + 1)
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
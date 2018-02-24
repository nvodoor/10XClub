class Node():

	def __init__(self, value):

		self.value = value;
		self.right = None;
		self.left = None;

class BST():

	def __init__(self):

		self.root = None;

	def addRoot(self,value):

		if self.root == None:
			self.root = Node(value)
		else:
			leaf = self.root
			self.root = Node(value)
			if self.root.value > leaf.value:
				self.root.left = leaf
			else:
				self.root.right = leaf
			return True

	def addNode(self,value,root):
		if root == None:
			root = self.root

		if self.root == None:
			self.root = Node(value)
			return True
		else:
			if root.value < value and root.right != None:
				return self.addNode(value, root.right)
			elif root.value < value and root.right == None:
				root.right = Node(value)
				return True
			elif root.value > value and root.left != None:
				return self.addNode(value, root.left)
			else:
				root.left = Node(value)
				return True


Tree = BST();
Tree.addRoot(3);
Tree.addNode(5, None);
Tree.addNode(2, None);
Tree.addNode(1, None);
Tree.addNode(4, None);
print(Tree.root)
print(Tree.root.right.value)
print(Tree.root.right.left.value)
print(Tree.root.left.left.value)



	
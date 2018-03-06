class Node():

	def __init__(self,value=None):
		self.value = value;
		self.children = {};

class Trie():

	def __init__(self):
		self.root = Node();

	def add(self, value):

		node = self.root;

		for s in value:
			if (s not in node.children):
				node.children[s] = Node();
			node = node.children[s]
		node.value = value

	def find(self, value):

		node = self.root

		for s in value:
			if (s in node.children):
				node = node.children[s]
			else:
				return False
		return node.value == value

	def print(self):

		children = [{'prefix': "", 'node': self.root}]

		while (len(children) > 0):
			child = children.pop(0);
			node = child['node'];
			prefix = child['prefix'];
			keys = node.children.keys();
			for key in keys:
				children.append({'prefix': prefix+key, 'node': node.children[key]})
				if (len(prefix) == 0):
					print(" " + "_" + "->" + prefix + key + " [label=\"" + key + "\"]")
				else:
					print("  " + prefix + " -> " +
                    	prefix + key + " [label=\"" + key + "\"]")


trie = Trie();

trie.add('pie');

print(trie.find('pie'));

print(trie.find('pies'));

trie.print();
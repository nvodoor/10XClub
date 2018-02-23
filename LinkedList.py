from flask import jsonify 

class Node():

	def __init__(self, value):
		self.value = value
		self.next = None;

class LinkedList():

	def __init__(self):
		self.head = None;

	def addStart(self,value):
		
		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head
			self.head = Node(value)
			self.head.next = current

	def addEnd(self, value):

		if self.head == None:
			self.head = Node(value)
		else:
			current = self.head

			while current.next != None:
				if current.next == None:
					break
				else:
					current = current.next

			current.next = Node(value)

	def addAt(self,value, index):

		if index == 0:
			self.addStart(value)
		else:
			count = 0
			prev = None;
			current = self.head
			while index >= count:
				if count == index:
					future = current
					current = Node(value)
					prev.next = current
					current.next = future
					break
				else:
					count +=1
					prev = current
					current = current.next

	def deleteStart(self):

		if self.head == None:
			return "This Linked List is empty."
		else:
			self.head = self.head.next

	def deleteEnd(self):

		if self.head == None:
			return "This Linked List is empty."
		else:
			current = self.head
			prev = None
			while current != None:
				if current.next == None:
					prev.next = None
					return True
				else:
					prev = current
					current = current.next

	def deleteAt(self,index):

		count = 0;
		current = self.head
		prev = None

		while count <= index:
			if count == index:
				prev.next = current.next
				return True
			else:
				prev = current
				current = current.next
				count += 1

		return False
	


	def listValues(self):
		return self.head.value

	def listAllValues(self):
		valarr = []
		current = self.head
		while current != None:
			valarr.append(current.value)
			current = current.next
		return valarr


LL = LinkedList()
LL.addStart(3)
print(LL.listValues())
LL.addStart(4)
LL.addStart(5)
LL.addEnd(6)
LL.addAt(7,2)

# print(LL.listValues())
print(LL.listAllValues())
LL.deleteStart()
print(LL.listAllValues())
LL.addStart(5)
LL.deleteEnd()
print(LL.listAllValues())
LL.addEnd(6)
LL.deleteAt(2)
print(LL.listAllValues())

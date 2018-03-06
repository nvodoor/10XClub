class MaxHeap():

	def __init__(self):
		self.heap = []

	def push(self,value):
		self.heap.append(value);
		self.siftUp(len(self.heap) - 1)

	def peek(self):
		if self.heap[0]:
			return self.heap[0]
		else:
			return False

	def pop(self):
		value = self.heap.pop(0);

		for i in range(0, len(self.heap)):
			self.siftUp(i)

		return value

	def swap(self,a,b):
		self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
		return True

	def siftUp(self, idx):
		parent = idx // 2;

		if idx < 1:
			return True;

		if self.heap[idx] > self.heap[parent]:
			self.swap(idx, parent)
			self.siftUp(parent)

	def merge(self,arr):

		for i in range(0, len(arr)):
			self.heap.append(arr[i]);
			self.siftUp(len(self.heap)-1);


heap = MaxHeap();

heap.push(2);
heap.push(3);
heap.push(1);
heap.push(15);
heap.push(4);
heap.push(7);

print (heap.heap)
print (heap.peek())
print (heap.pop())
print (heap.heap)

heap.merge([30,8,6])

print(heap.heap)
print(heap.pop())
print(heap.pop())
print(heap.peek())

class MinHeap():

	def __init__(self):
		self.heap = []

	def push(self,value):
		self.heap.append(value);
		self.siftDown(len(self.heap) - 1)

	def peek(self):
		if self.heap[0]:
			return self.heap[0]
		else:
			return False

	def pop(self):
		value = self.heap.pop(0);

		for i in range(0, len(self.heap)):
			self.siftDown(i)

		return value

	def swap(self,a,b):
		self.heap[a], self.heap[b] = self.heap[b], self.heap[a]
		return True

	def siftDown(self, idx):
		parent = idx // 2;

		if idx < 1:
			return True;

		if self.heap[idx] < self.heap[parent]:
			self.swap(idx, parent)
			self.siftDown(parent)

	def merge(self,arr):

		for i in range(0, len(arr)):
			self.heap.append(arr[i]);
			self.siftDown(len(self.heap)-1);

heap = MinHeap();

heap.push(2);
heap.push(3);
heap.push(1);
heap.push(15);
heap.push(4);
heap.push(7);

print (heap.heap)
print (heap.peek())
print (heap.pop())
print (heap.heap)
import math

def HashFunction(obj):

	string = str(obj)
	a = 101;
	n = pow(2,32);
	k = len(string)
	running_a = pow(a, k)

	result = 0;
	for i in range(0, k):
		running_a = running_a / a
		c = ord(string[i])
		# ord is function to invoke to get charCode
		result += c*running_a
		result = result % n;

	return result;


print(HashFunction('block'))


class Hash():

	def __init__(self, size):
		self.data = [None for i in range(0,size)]

	def add(self,key, value):
		keyHash = HashFunction(key) % len(self.data)
		self.data[keyHash] = value;

	def delete(self,key):
		keyHash = HashFunction(key) % len(self.data)
		self.data[keyHash] = None;

	def get(self,key):
		keyHash = HashFunction(key) % len(self.data)
		return self.data[keyHash]

	def print(self):
		root = math.ceil(math.sqrt(len(self.data)))
		square = root*root
		print("P2")
		print(str(root) + " " + str(root));
		print("2");

		line = []
		for i in range(0,square):
			if i >= len(self.data):
				line.append("1")
			elif self.data[i]:
				line.append("0")
			else:
				line.append("2")

		if (i % root == root - 1):
			print(" ".join(line))
			line = [];

		return True
		

Hashing = Hash(10)

Hashing.print()

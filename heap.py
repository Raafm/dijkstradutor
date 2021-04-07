# código autoral de Eduardo Geber

def left(i):
	# the calculations are adapted to serve an array of first index 0
	# instead of 1
	return 2*(i+1) - 1


def right(i):
	return 2*(i+1)


def parent(i):
	return (i+1)//2 - 1


def maxHeapify(array, i, n, comp=lambda a, b: a < b):
	"""Check MaxHeap's documentation to understand how comp is used.
	i: the index of the beggining of the 'heapification'
	n: the length of the heap contained by the array
	"""
	l = left(i)
	r = right(i)
	greatest = i
	if l < n:
		if comp(array[i], array[l]):
			greatest = l
		if r < n and comp(array[greatest], array[r]):
			greatest = r
	if greatest != i:
		array[greatest], array[i] = array[i], array[greatest]
		maxHeapify(array, greatest, n, comp)


class MaxHeap:
	# if you want a min heap, just choose a proper comparator function
    def __init__(self, heap_array=[], comp=lambda a, b: a < b):
    	"""
    	heap_array: the array where the elements of the heap will be stored,
    	default is an empty Python list. Any value other than that should be
    	a dynamic array which supports append() and pop() methods, the
    	__len__ special method and indexation with the [] operator.
    	self.comp: it works just as the reference for C++'s std priority_queue
    	explains: comp is a binary predicate that takes two elements as
    	arguments and returns a bool. The expression comp(a, b), where a and b
    	are elements in the container, shall return True if a must be below b
        in the binary tree. It defaults to the less-than operator (a < b), so
        a default MaxHeap will indeed be a max heap (of numbers or strings,
        which support the '<' operator). On the other hand, passing lambda a,
        b: a > b to comp will actually make MaxHeap a min heap.
    	"""
    	self.comp = comp
    	self.array = heap_array


    def empty(self):
        return len(self) == 0


    def insert(self, elem):
        # this only serves for creating a new space in the end of the array
        self.array.append(elem)
        i = len(self.array)-1  # the last index
        p = parent(i)
        while i != 0 and self.comp(self.array[p], elem):
            # then the parent of elem should be below elem
            self.array[i] = self.array[p]  # bring the parent down
            i = p
            p = parent(p)
        # now i has the value of the index where elem should be inserted
        self.array[i] = elem


    def heapify(self, i):
        maxHeapify(self.array, i, len(self.array), self.comp)


    def top(self):
    	return self.array[0]


    def pop(self):
        max_ = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.heapify(0)
        return max_


    def getHeapsorted(self):
        """Returns the heapsorted self.array. self.array isn't changed"""
        array = self.array
        i = len(array)-1
        while i > 0:
            array[0], array[i] = array[i], array[0]
            maxHeapify(array, 0, i, self.comp)
            i -= 1
        return array


    def __len__(self):
        return len(self.array)

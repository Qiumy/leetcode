# Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
#
# Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].
#
# Call next() gets you 1, the first element in the list.
#
# Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
#
# You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.
#
# Hint:
#
# Think of "looking ahead". You want to cache the next element.
# Is one variable sufficient? Why or why not?
# Test your design with call order of peek() before next() vs next() before peek().
# For a clean implementation, check out Google's guava library source code.

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        self.tmp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.tmp

    def next(self):
        """
        :rtype: int
        """
        ret = self.tmp
        self.tmp = self.iter.next() if self.iter.hasNext() else None
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.tmp is not None

        # Your PeekingIterator object will be instantiated and called as such:
        # iter = PeekingIterator(Iterator(nums))
        # while iter.hasNext():
        #     val = iter.peek()   # Get the next element but not advance the iterator.
        #     iter.next()         # Should return the same value as [val].

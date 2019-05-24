from collections import deque


class FlatennedIterator:
    """
    Given a list of iterators, this FlattenedIterator class incrementally iterates over the elements from all the
    iterators in an interleaved fashion.
    """
    def __init__(self, *iters):
        self.iterators = deque()  # queue of all non-zero iterators
        for cur_iter in iters:
            if cur_iter.hasNext():
                self.iterators.append(cur_iter)

    def next(self):
        """
        :return: The next element of the FlatennedIterator
        """
        if self.hasNext():
            cur_iter = self.iterators.popleft()  # get the iterator which is in the front of the queue
            elt = cur_iter.next()  # get the next element of the given iterator
            if cur_iter.hasNext():  # hasNext does not exist in python. We are assuming it exists for the task.
                self.iterators.append(cur_iter)  # add iterator to end of the queue if it is not empty yet
            return elt
        raise StopIteration

    def hasNext(self):
        """
        :return: True if the iterator has an element to iterate over, False otherwise
        """
        if len(self.iterators):
            return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

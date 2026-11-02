# Program Description: Circular Buffer Assignment. This program defines the CircularBuffer class, a fixed-size
#   queue-based FIFO circular buffer. Items are inserted at the
#   tail and removed from the head; head and tail wrap around to index 0 using
#   the modulus operator. Adding an item to a full buffer overwrites the
#   oldest item.
# Author: Gregory Ayala
# Date: November 1st, 2026

"""
    Create circular buffer class to perform data operations
"""

class CircularBuffer:
    """Circular buffer of fixed size. FIFO based. Items are stored in a list.

    The head holds the index of the first current item. The tail holds the index
    where the next item will be inserted. The modulus operator wraps indices to
    zero at the end of the list. Adding to a full buffer overwrites the oldest item.
    """
    # initializer
    def __init__(self, capacity):
        """Initialize an empty circular buffer with the given capacity."""
        self.__capacity = capacity
        self.__size = 0
        self.__buffer = [None] * capacity
        self.__head = 0
        self.__tail = 0

    # getters and setter
    def get_capacity(self):
        """Return the maximum number of items a buffer can hold."""
        return self.__capacity
        
    def set_capacity(self,capacity):
        """ Set max number of items buffer can hold. """
        self.__capacity = capacity
        
    def get_buffer(self):
        """ Return the list that stores buffer items """
        return self.__buffer
        
    def get_head(self):
        """ Return index of the first current item in buffer. """
        return self.__head
        
    def get_tail(self):
        """Return the index where the next item will be inserted."""
        return self.__tail
        
    def get_size(self):
        """ Return number of items in buffer """
        return self.__size

    # methods
    def add(self,item):
        """ Insert item into tail position. Advance tail with wrap-around. If buffer is full then 
        oldest item is overwritten. Size grows until buffer is full. """
        self.__buffer[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__capacity
        if self.__size < self.__capacity:
            # room was available: one more current item
            self.__size += 1
        else:
            # buffer was full, so the item we stored replaced the oldest
            # one; move the head past that slot
            self.__head = (self.__head + 1) % self.__capacity
        
    def delete(self):
        """ Remove item at head position, return it, and advance the head with wraparound. If buffer is empty
        display 'Buffer is empty' and return None. """
        if self.__size == 0:
            print(" Buffer is empty")
            return None
        item = self.__buffer[self.__head]
        self.__buffer[self.__head] = None
        self.__head = (self.__head + 1) % self.__capacity
        self.__size -= 1
        return item
        
    def clear(self):
        """Reset positions in buffer list to None. Reset head, tail, and size to 0."""
        for i in range(self.__capacity):
            self.__buffer[i] = None
        self.__head = 0
        self.__tail = 0
        self.__size = 0        
        
    def is_empty(self):
        """ Return True if buffer holds no items otherwise returns False """
        return self.__size == 0
        
    def peek_first(self):
        """ Return first item in buffer. """
        return self.__buffer[self.__head]
        
    def peek_last(self):
        """ Return last item in buffer """
        return self.__buffer[(self.__tail - 1) % self.__capacity] 

        
    def find(self,item):
        """Return True if the item is present; otherwise return False."""
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            if self.__buffer[index] == item:
                return True
        return False
    
    def __str__(self):
        """Return a string of current items in queue order, separated by -->.

        Return 'Buffer is empty' for an empty buffer.
        """
        if self.__size == 0:
            return(" Buffer is empty")
        items = []
        for i in range(self.__size):
            index = (self.__head + i) % self.__capacity
            items.append(str(self.__buffer[index]))
        return " --> " .join(items)



    

    
        




            
        

# Program Description: Circular Buffer Test Program. This program prompts the user for a buffer capacity,
#   creates a CircularBuffer object, and runs the 14 sample steps from the
#   assignment, and then clears the buffer.
# Author: Gregory Ayala
# Date: November 1st, 2026

"""
    Test circular buffer class to perform data operations
"""
# Import Circular Buffer class here
from circular_buffer import CircularBuffer

def main():
    """ main function to test the functionality of circular buffer """
    capacity = int(input("Enter Buffer Capacity: "))
    cb = CircularBuffer(capacity)

    print()
    print("1. Delete Operation")
    deleted = cb.delete()
    if deleted is not None:
        print(f" {deleted} has been deleted")
        print(f" Buffer: {cb}")

    print("2. Add 15:")
    cb.add(15)
    print(f" Buffer: {cb}")

    print("3. Add 5:")
    cb.add(5)
    print(f" Buffer: {cb}")

    print("4. Delete operation")
    deleted = cb.delete()
    if deleted is not None:
        print(f" {deleted} has been deleted")
        print(f" Buffer: {cb}")

    print("5. Add 3:")
    cb.add(3)
    print(f" Buffer: {cb}")

    print("6. Add 26:")
    cb.add(26)
    print(f" Buffer: {cb}")

    print("7. Delete operation")
    deleted = cb.delete()
    if deleted is not None:
        print(f" {deleted} has been deleted")
        print(f" Buffer: {cb}")

    print("8. Add 76:")
    cb.add(76)
    print(f" Buffer: {cb}")
    
    print("9. Add 105:")
    cb.add(105)
    print(f" Buffer: {cb}")

    print("10. Search 48:")
    if cb.find(48):
        print(" 48 is in the buffer")
    else:
        print(" 48 is not in the buffer")

    print("11. Peek First/Last:")
    print(f" {cb.peek_first()} is the First item.")
    print(f" {cb.peek_last()} is the Last item.")

    print("12. Sum of all items")
    print(f" Sum = {add_all(cb)}")

    print("13. Locate the Largest/Smallest items:")
    max_index= get_max_index(cb)
    min_index= get_min_index(cb)
    print(f" The largest item = {cb.get_buffer()[max_index]}")
    print(f" The smallest item = {cb.get_buffer()[min_index]}")

    print("14. Clear:")
    cb.clear()
    print(f" {cb}")    
    
def add_all(cb):
    """ Function used to return a sum of all current items in buffer. """
    total = 0
    capacity = cb.get_capacity()
    head = cb.get_head()
    size = cb.get_size()
    buffer = cb.get_buffer()

    for i in range(size):
        total += buffer[(head + i) % capacity]
    return total

def get_max_index(cb):
    """ Function used to return index of largest item in buffer. """
    capacity = cb.get_capacity()
    head = cb.get_head()
    size = cb.get_size()
    buffer = cb.get_buffer()
    max_index = head % capacity
    for i in range(1, size):
        index = (head + i) % capacity
        if buffer[index] > buffer [max_index]:
            max_index = index
    return max_index

    
def get_min_index(cb):
    """ Function used to return index of smallest item in buffer """
    capacity = cb.get_capacity()
    head = cb.get_head()
    size = cb.get_size()
    buffer = cb.get_buffer()
    min_index = head % capacity
    for i in range(1, size):
        index = (head + i) % capacity
        if buffer[index] < buffer [min_index]:
                min_index = index
    return min_index

if __name__ == '__main__':
    main()

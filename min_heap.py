# Course: CS261 - Data Structures
# Assignment: Assignment 5 - Min Heap Implementation
# Student: Dylan Mitchel Karambut
# Description: Implementation of Min Heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    # Function: add
    # Description: Add node into the Hash Map
    # Parameters: self, node: object
    # Pre-conditions:
    # Post-conditions: Added node of Hash Map
    def add(self, node: object) -> None:
        self.heap.append(node)

        if self.heap.length() == 1:
            return

        children = self.heap.length() - 1
        parents = (children - 1) // 2
        while self.heap.get_at_index(parents) > self.heap.get_at_index(children) and children != 0:
            self.heap.swap(parents, children)
            children = parents
            parents = (children - 1) // 2

    # Function: get_min
    # Description: Get the minimum key from the Hash Map
    # Parameters: self, node: object
    # Pre-conditions:
    # Post-conditions: Founded minimum key of Hash Map
    def get_min(self) -> object:
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    # Function: remove_min
    # Description: Remove the minimum key from the Hash Map
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Removed minimum key of Hash Map
    def remove_min(self) -> object:
        if self.heap.length() == 0:
            raise MinHeapException

        self.heap.swap(0, self.heap.length() - 1)
        return_node = self.heap.pop()

        if self.heap.length() == 0:
            return return_node

        parents_index = 0
        parents_value = self.heap.get_at_index(parents_index)
        children1_index = 1
        children2_index = 2
        minimum_index = self.min_index(children1_index, children2_index)
        minimum_value = self.heap.get_at_index(minimum_index)

        while not self.out_of_range(children1_index, children2_index) and parents_value > minimum_value:
            self.heap.swap(parents_index, minimum_index)
            parents_index = minimum_index
            parents_value = self.heap.get_at_index(parents_index)
            children1_index = (2 * parents_index) + 1
            children2_index = (2 * parents_index) + 2
            minimum_index = self.min_index(children1_index, children2_index)
            minimum_value = self.heap.get_at_index(minimum_index)

        return return_node

    # Function: build_heap
    # Description: Build the da for Hash Map
    # Parameters: self, da: DynamicArray
    # Pre-conditions:
    # Post-conditions: Built DynamicArray Hash Map
    def build_heap(self, da: DynamicArray) -> None:
        da2 = DynamicArray()
        for index in range(da.length()):
            da2.append(da.get_at_index(index))

        if da2.length() < 2:
            self.heap = da2
            return

        counter = 0
        root_bool = False

        while root_bool == False:
            if counter == 0:
                parents_outer_index = ((da2.length() // 2) - 1)
            else:
                parents_outer_index = parents_outer_index - 1

            if parents_outer_index == 0:
                root_bool = True

            parents_index = parents_outer_index
            parents_value = da2.get_at_index(parents_index)
            children1_index = (2 * parents_outer_index) + 1
            children2_index = (2 * parents_outer_index) + 2
            minimum_index = self.min_index_dynamic_array(children1_index, children2_index, da2)
            minimum_value = da2.get_at_index(minimum_index)

            counter += 1

            while not self.out_of_range_dynamic_array(children1_index, children2_index, da2) and parents_value > minimum_value:
                da2.swap(parents_index, minimum_index)
                parents_index = minimum_index
                parents_value = da2.get_at_index(parents_index)
                children1_index = (2 * parents_index) + 1
                children2_index = (2 * parents_index) + 2
                minimum_index = self.min_index_dynamic_array(children1_index, children2_index, da2)
                minimum_value = da2.get_at_index(minimum_index)

            self.heap = da2

    # Function: min_index
    # Description: Dependencies for remove_min
    # Parameters: self, index1: int, index2: int
    # Pre-conditions:
    # Post-conditions: Checked if it is minimum value or 0 considered as out of range
    def min_index(self, index1: int, index2: int) -> int:
        if index1 > self.heap.length() - 1 and index2 < self.heap.length():
            return index2

        if index2 > self.heap.length() - 1 and index1 < self.heap.length():
            return index1

        if index2 > self.heap.length() - 1 and index1 > self.heap.length() - 1:
            return 0

        value1 = self.heap.get_at_index(index1)
        value2 = self.heap.get_at_index(index2)

        if value1 < value2:
            return index1

        return index2

    # Function: out_of_range
    # Description: Dependencies for remove_min
    # Parameters: self, index1: int, index2: int
    # Pre-conditions:
    # Post-conditions: Checked if index1 and index2 are out of range
    def out_of_range(self, index1: int, index2: int) -> bool:
        if index1 > self.heap.length() - 1 and index2 > self.heap.length() - 1:
            return True

        return False

    # Function: min_index_dynamic_array
    # Description: Dependencies for build_heap
    # Parameters: self, index1: int, index2: int, da: object
    # Pre-conditions:
    # Post-conditions: Checked if it is minimum value or 0 considered as out of range
    def min_index_dynamic_array(self, index1: int, index2: int, da: object) -> int:
        if index1 > da.length() - 1 and index2 < da.length():
            return index2

        if index2 > da.length() - 1 and index1 < da.length():
            return index1

        if index2 > da.length() - 1 and index1 > da.length() - 1:
            return 0

        value1 = da.get_at_index(index1)
        value2 = da.get_at_index(index2)

        if value1 < value2:
            return index1

        return index2

    # Function: out_of_range_dynamic_array
    # Description: Dependencies for build_heap
    # Parameters: self, index1: int, index2: int, da: object
    # Pre-conditions:
    # Post-conditions: Checked if index1 and index2 are out of range
    def out_of_range_dynamic_array(self, index1: int, index2: int, da: object) -> bool:
        if index1 > da.length() - 1 and index2 > da.length() - 1:
            return True

        return False




# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

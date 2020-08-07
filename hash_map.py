# Course: CS261 - Data Structures
# Assignment: Assignment 5 - Hash Map Implementation
# Student: Dylan Mitchel Karambut
# Description: Implementing Hash Map


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    # Function: clear
    # Description: Clear the Hash Map
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Cleared Hash Map
    def clear(self) -> None:
        for index in range(self.capacity):
            self.buckets.set_at_index(index, LinkedList())

        self.size = 0

    # Function: get
    # Description: Get the value and key the Hash Map
    # Parameters: self, key: str
    # Pre-conditions:
    # Post-conditions: Returned value and the key of Hash Map
    def get(self, key: str) -> object:
        hash_value = self.hash_function(key)
        dynamic_array_index = hash_value % self.capacity

        if self.buckets.length() == 0:
            return False

        target_linked_list = self.buckets.get_at_index(dynamic_array_index)

        if target_linked_list.contains(key) is None:
            return None

        if target_linked_list.contains(key) is not None:
            return target_linked_list.contains(key).value

    # Function: put
    # Description: Update the key/value of Hash Map
    # Parameters: self, key: str, value: object
    # Pre-conditions:
    # Post-conditions: Updated key/value of Hash Map
    def put(self, key: str, value: object) -> None:
        hash_value = self.hash_function(key)
        dynamic_array_index = hash_value % self.capacity

        if self.buckets.get_at_index(dynamic_array_index).contains(key) is not None:
            self.buckets.get_at_index(dynamic_array_index).remove(key)
            self.buckets.get_at_index(dynamic_array_index).insert(key, value)
            return

        if self.buckets.get_at_index(dynamic_array_index).contains(key) is None:
            self.buckets.get_at_index(dynamic_array_index).insert(key, value)
            self.size += 1

    # Function: remove
    # Description: Remove the key/value of Hash Map
    # Parameters: self, key: str
    # Pre-conditions:
    # Post-conditions: Removed key/value of Hash Map
    def remove(self, key: str) -> None:
        hash_value = self.hash_function(key)
        dynamic_array_index = hash_value % self.capacity

        if self.buckets.get_at_index(dynamic_array_index).remove(key):
            self.size -= 1

    # Function: contains_key
    # Description: Check if it is containing key of Hash Map
    # Parameters: self, key: str
    # Pre-conditions:
    # Post-conditions: Checked key state of Hash Map
    def contains_key(self, key: str) -> bool:
        hash_value = self.hash_function(key)
        dynamic_array_index = hash_value % self.capacity

        if self.buckets.length() == 0:
            return False

        current_linked_list = self.buckets.get_at_index(dynamic_array_index)

        if current_linked_list.contains(key) is None:
            return False

        if current_linked_list.contains(key) is not None:
            return True

    # Function: empty_buckets
    # Description: Return the number of empty buckets of Hash Map
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Number of empty buckets of Hash Map
    def empty_buckets(self) -> int:
        counter = 0
        for index in range(self.buckets.length()):
            if self.buckets.get_at_index(index).length() == 0:
                counter += 1

        return counter

    # Function: table_load
    # Description: Shows the Hash Map table load
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Showed Hash Map table load
    def table_load(self) -> float:
        return float(self.size / self.capacity)

    # Function: empty_buckets
    # Description: Return the number of empty buckets of Hash Map
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Number of empty buckets of Hash Map
    def resize_table(self, new_capacity: int) -> None:
        if new_capacity < 1:
            return

        new_dynamic_array = DynamicArray()
        for _ in range(new_capacity):
            new_dynamic_array.append(LinkedList())

        for index in range(self.capacity):
            current_linked_list = self.buckets.get_at_index(index)
            for node in current_linked_list:
                hash_value = self.hash_function(node.key)
                new_dynamic_array_index = hash_value % new_capacity
                new_dynamic_array.get_at_index(new_dynamic_array_index).insert(node.key, node.value)

        self.buckets = new_dynamic_array
        self.capacity = new_capacity

    # Function: get_keys
    # Description: Shows the keys of Hash Map
    # Parameters: self
    # Pre-conditions:
    # Post-conditions: Showed keys of Hash Map
    def get_keys(self) -> DynamicArray:
        return_dynamic_array = DynamicArray()

        for index in range(self.capacity):
            current_linked_list = self.buckets.get_at_index(index)
            for node in current_linked_list:
                return_dynamic_array.append(node.key)

        return return_dynamic_array


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

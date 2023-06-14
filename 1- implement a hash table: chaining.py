class LinkedList:
    class Node:
        def __init__(self, key=None, value=None, next=None):
            self.__value = value
            self.__key = key
            self.__next = next

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, node):
            self.__next = node

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, item):
            self.__value = item

        @property
        def key(self):
            return self.__key

        @key.setter
        def key(self, item):
            self.__key = item

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def add_or_replace(self, key, value):
        _, node = self.__get_node_and_index_by_key(key)
        if node:
            node.value = value
            return

        node = LinkedList.Node(key=key, value=value)
        if self.__is_empty():
            self.__first = self.__last = node
            return
        self.__last.next = node
        self.__last = node
        self.__size += 1

    def get_value_by_key(self, key):
        _, node = self.__get_node_and_index_by_key(key)
        return node and node.value

    def __get_node_and_index_by_key(self, key):
        current_node = self.__first
        index = 0
        while current_node:
            if key == current_node.key:
                return index, current_node
            index += 1
            current_node = current_node.next
        return -1, None

    def __is_empty(self):
        return self.__first == None

    def __delete_first(self):
        if self.__is_empty():
            raise IndexError("no such element")

        if self.__first == self.__last:
            # this if is for the time that there is one item in the list
            # i doubt this if is needed, i got no error whithout it
            self.__first = self.__last = None
        else:
            # if we have at least two nodes
            second = self.__first.next
            self.__first.next = None
            self.__first = second

        self.__size -= 1

    def __delete_last(self):
        if self.__is_empty():
            raise IndexError("empty list")

        if self.__first == self.__last:
            # this if is for the time that there is one item in the list
            self.__first = self.__last = None
        else:
            # if we have at least two nodes
            previous_node = self.__get_previous_node(self.__last)
            previous_node.next = None
            self.__last = previous_node

        self.__size -= 1

    def __delete_middle(self, deleting_node):
        prev_node = self.__get_previous_node(deleting_node)
        prev_node.next = deleting_node.next
        deleting_node.next = None

    def delete(self, key):
        index, node = self.__get_node_and_index_by_key(key)
        if index == 0:
            self.__delete_first()
        elif index == self.__size - 1:
            self.__delete_last()
        elif index == -1:
            pass
        else:
            self.__delete_middle(node)

    def __get_previous_node(self, node):
        if node == self.__first:
            return None

        current_node = self.__first
        while current_node != None:
            if current_node.next == node:
                return current_node
            current_node = current_node.next
        return None


class HashTable:
    def __init__(self, size=5):
        self.array = [LinkedList() for i in range(size)]

    def __hash(self, key):
        return sum([ord(i) for i in str(key)]) % len(self.array)

    def __get_bucket(self, key):
        index = self.__hash(key)
        bucket = self.array[index]
        return bucket

    def __setitem__(self, key, value):
        bucket = self.__get_bucket(key)
        bucket.add_or_replace(key, value)

    def __getitem__(self, key):
        bucket = self.__get_bucket(key)
        return bucket.get_value_by_key(key)

    def delete(self, key):
        bucket = self.__get_bucket(key)
        bucket.delete(key)


my_dct = HashTable()
my_dct["name"] = "Mohammad Javad"
my_dct["age"] = 23
my_dct["age"] = 24
my_dct["score"] = 100
my_dct["family name"] = "Ramezanpour"
my_dct["weight"] = 80
print(my_dct["score"])
my_dct.delete("score")
print(my_dct["age"])
print(my_dct["score"])

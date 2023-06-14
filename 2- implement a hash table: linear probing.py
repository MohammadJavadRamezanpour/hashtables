class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.array = [None] * self.size

    def __hash(self, key):
        return sum([ord(i) for i in str(key)]) % self.size

    def __linear_probe(self, key):
        index = self.__hash(key)

        for i in range(self.size):
            current_index = (index + i) % self.size

            if self.array[current_index] is None:
                return current_index

            if self.array[current_index][0] == key:
                return current_index

        raise Exception("Hash table is full")

    def __setitem__(self, key, value):
        index = self.__linear_probe(key)
        self.array[index] = (key, value)

    def __getitem__(self, key):
        index = self.__linear_probe(key)
        if self.array[index] is not None:
            return self.array[index][1]
        else:
            raise KeyError("Key not found")

    def delete(self, key):
        index = self.__linear_probe(key)
        if self.array[index] is not None:
            self.array[index] = None
        else:
            raise KeyError("Key not found")


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

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.array = [None] * self.size

    def __get_largest_prime(self):
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        for i in range(self.size - 1, 1, -1):
            if is_prime(i):
                return i

        return 2

    def __hash(self, key):
        return hash(key) % self.size

    def __hash2(self, key):
        the_prime = self.__get_largest_prime()
        return the_prime - (self.__hash(key) % the_prime)

    def __double_hash_probe(self, key):
        index = self.__hash(key)
        hash2 = self.__hash2(key)

        i = 0
        while (
            self.array[(index + i * hash2) % self.size] is not None
            and self.array[(index + i * hash2) % self.size][0] != key
        ):
            i += 1

        return (index + i * hash2) % self.size

    def __setitem__(self, key, value):
        index = self.__double_hash_probe(key)
        self.array[index] = (key, value)

    def __getitem__(self, key):
        index = self.__double_hash_probe(key)
        if self.array[index] is not None:
            return self.array[index][1]
        else:
            raise KeyError("Key not found")

    def delete(self, key):
        index = self.__double_hash_probe(key)
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
my_dct.delete("score")
print(my_dct["age"])
print(my_dct["score"])
class MyHashTable:
    DEFAULT_U = 1000  # Default size of all keys. for example, all possible ids
    DEFAULT_S = None  # Default size of keys - for example, all students ids

    def __init__(self, u=DEFAULT_U, s=DEFAULT_S):
        if s:  # Perfect Hash
            self.init_perfect_hash(u, s)
        else:
            self.init_hash()

    def generate_h_func(self):
        # TODO
        pass

    def init_perfect_hash(self, u, s):
        # TODO
        pass

    def init_hash(self):
        # TODO
        pass

class ArrayList:
    def __init__(self, initial_capacity=10):
        self._max_size = initial_capacity
        self._last_index = 0
        self._my_array = [None] * self._max_size

    def append(self, val):
        self._my_array[self._last_index] = val
        self._last_index += 1
        
    def size(self):
        return self._last_index

    def is_empty(self):
        return self._last_index == 0
        
    def __getitem__(self, idx):
        if 0 <= idx < self._last_index:
            return self._my_array[idx]
        raise LookupError("index out of bounds")

    def __setitem__(self, idx, val):
        if 0 <= idx < self._last_index:
            self._my_array[idx] = val
        else:
            raise LookupError("index out of bounds")
        
    def insert(self, idx, val):
        for i in range(self._last_index, idx, -1):
            self._my_array[i] = self._my_array[i - 1]
        self._my_array[idx] = val
        self._last_index += 1
        
    def erase(self, idx):
        if 0 <= idx < self._last_index:
            for i in range(idx, self._last_index - 1):
                self._my_array[i] = self._my_array[i + 1]
            self._my_array[self._last_index - 1] = None
            self._last_index -= 1
        else:
            raise LookupError("index out of bounds")
            
    def remove(self, val):
        for i in range(self._last_index):
            if self._my_array[i] == val:
                for j in range(i, self._last_index - 1):
                    self._my_array[j] = self._my_array[j + 1]
                self._my_array[self._last_index - 1] = None
                self._last_index -= 1
                return
        raise LookupError("value not found")
        
    def __str__(self):
        return '[' + ', '.join(str(self._my_array[i]) for i in range(self._last_index)) + ']'
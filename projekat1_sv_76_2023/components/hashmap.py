import random
class HashMap:
    def __init__(self, size=100):
        self._data = [[] for _ in range(size)]

        self._capacity = size
        self._size = 0
        self._prime = 109345121

        self._a = 1 + random.randrange(self._prime-1)
        self._b = random.randrange(self._prime)
        
    def _hash(self, key):
        hashed_value = (hash(key)*self._a + self._b) % self._prime
        compressed = hashed_value % self._capacity
        return compressed
    
    
    def __getitem__(self, key):
        hashed_key = self._hash(key)

        bucket = self._data[hashed_key]

        if bucket != None:
            for item in bucket:
                if item[0] == key:
                    return item[1]
                
        return None


    def __setitem__(self, key, value):
        hashed_key = self._hash(key)

        bucket = self._data[hashed_key]
        
        if bucket != None:
            for item in bucket:
                if item[0] == key:
                    item[1] = value

            bucket.append([key, value])
                
        return None

    def __delitem__(self, key):
        hashed_key = self._hash(key)

        bucket = self._data[hashed_key]

        if bucket != None:
            for item in bucket:
                if item[0] == key:
                    bucket.remove(item)
                    return True
                
        return False
    


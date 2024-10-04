# Runtime: 552ms
# Beats: 77.77%

# Memory: 78.54MB
# Beats: 23.34%

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.keys_age = {}
        self.age_keys = {}
        self.newest = -1
        self.oldest = -1
    

    def get(self, key: int) -> int:
        value = self.cache.get(key) 
        if value is None:
            return -1
        
        age = self.keys_age.get(key)

        if age == self.oldest:
            self.oldest += 1
            if self.capacity != 1 and self.size != 1:
                while self.age_keys.get(self.oldest) is None:
                    self.oldest += 1
            
        
        self.newest += 1
        self.keys_age[key] = self.newest

        del self.age_keys[age]
        self.age_keys[self.newest] = key

        if self.capacity != 1:
            while self.age_keys.get(self.oldest) is None:
                self.oldest += 1

        return value
        

    def put(self, key: int, value: int) -> None: 
        if self.size == self.capacity and self.cache.get(key) is None:
            oldest_key = self.age_keys[self.oldest]
            del self.keys_age[oldest_key]
            del self.age_keys[self.oldest]
            del self.cache[oldest_key]
            self.oldest += 1
            if self.capacity != 1:
                while self.age_keys.get(self.oldest) is None:
                    self.oldest += 1

            self.size -= 1


        if self.cache.get(key) is not None:
            age_key = self.keys_age[key]
            del self.age_keys[age_key]
            if self.oldest == age_key and self.size != 1:
                while self.age_keys.get(self.oldest) is None:
                    self.oldest += 1
        else:
            self.size += 1

        self.cache[key] = value

        if self.newest == -1 and self.oldest == -1:
            self.oldest += 1
        
        self.newest += 1
        self.keys_age[key] = self.newest
        self.age_keys[self.newest] = key
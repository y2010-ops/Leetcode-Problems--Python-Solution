# Time Complexity = O(1)
class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.nums.append(val)
            self.hashmap[val] = self.nums.index(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            index = self.hashmap[val]
            lastval = self.nums[-1]
            self.nums[self.hashmap[val]] = lastval
            self.nums.pop()
            self.hashmap[lastval] = index
            del self.hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
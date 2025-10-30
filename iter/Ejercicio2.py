class ImparesIter:
    def __init__(self):
        self.n = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.n <= 20:
            if self.n % 2 != 0:
                actual = self.n
                self.n += 1
                return actual
            self.n += 1
        raise StopIteration

for i in ImparesIter():
    print(i)
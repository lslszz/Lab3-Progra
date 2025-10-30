class ContadorIter:
    def __init__(self):
        self.n = 10
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 15:
            actual = self.n
            self.n += 1
            return actual
        raise StopIteration

c = ContadorIter()
it = iter(c)
for i in range(6):
    print(next(it))
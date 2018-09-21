class Prizes(object):
    def __init__(self,arr, n, d):
        self.purchases = arr
        self.n = n
        self.d = d
        self.arr = []
        self.cnt = 0
        self.p = []
        i = 0
        while i < len(arr) - 1:
            if i != 0:
                self.p.append((arr[i-1], i))
            i += n
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while self.cnt < len(self.p):
            i = self.cnt
            self.cnt += 1
            print("a:",self.p[i])
            if self.p[i][0] % self.d == 0:
                # print(self.p[i])
                # print(self.p[i][1])
                return self.p[i][1]
            # else:
            #     self.__next__()
        raise StopIteration()

def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))

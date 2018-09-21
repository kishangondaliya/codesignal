class FRange(object):
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            self.i = 0
            self.stop = start
            self.step = 1
        elif step is None:
            self.i = start
            self.stop = stop
            self.step = 1
        else:
            self.i = start
            self.stop = stop
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        i_ = self.i
        if self.step > 0 and i_ < self.stop or self.step < 0 and i_ > self.stop:
            self.i = i_ + self.step
            return i_
        else:
            raise StopIteration

def rangeFloat(args):
    return list(FRange(*args))

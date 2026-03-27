class AlternatingCounter:
    def __init__(self):
        self._a = 0
        self._b = 0
        self._turn_a = True

    def count(self):
        if self._turn_a:
            self._a += 1
        else:
            self._b += 1
        self._turn_a = not self._turn_a
        return (self._a, self._b)

    def reset(self):
        self._a = 0
        self._b = 0
        self._turn_a = True

counter = AlternatingCounter()
print(counter.count())
print(counter.count())
print(counter.count())
counter.reset()
print(counter.count())

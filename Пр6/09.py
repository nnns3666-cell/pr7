class EvenOddSumTracker:
    def __init__(self):
        self._even_sum = 0
        self._odd_sum = 0

    def add_number(self, n):
        if n % 2 == 0:
            self._even_sum += n
        else:
            self._odd_sum += n

    def even_sum(self):
        return self._even_sum

    def odd_sum(self):
        return self._odd_sum

tracker = EvenOddSumTracker()
tracker.add_number(2)
tracker.add_number(3)
tracker.add_number(4)
tracker.add_number(5)
print(tracker.even_sum())
print(tracker.odd_sum())

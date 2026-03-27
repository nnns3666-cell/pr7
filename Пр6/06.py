class MinMaxNumberFinder:
    def __init__(self):
        self._numbers = []

    def add_number(self, n):
        self._numbers.append(n)

    def min_numbers(self):
        if not self._numbers:
            return []
        mn = min(self._numbers)
        return [x for x in self._numbers if x == mn]

    def max_numbers(self):
        if not self._numbers:
            return []
        mx = max(self._numbers)
        return sorted(set(x for x in self._numbers if x == mx))

finder = MinMaxNumberFinder()
finder.add_number(5)
finder.add_number(1)
finder.add_number(9)
finder.add_number(1)
finder.add_number(7)
print(finder.min_numbers())
print(finder.max_numbers())

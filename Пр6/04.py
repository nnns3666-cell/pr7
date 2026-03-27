class NumberDivider:
    def __init__(self):
        self._divisible = [] # числа, кратные 3
        self._not_divisible = [] # числа, не кратные 3

    def add_number(self, n):
        if n% 3 == 0:
            self._divisible.append(n)
        else:
            self._not_divisible.append(n)

    def divisible(self):
        return self._divisible

    def not_divisible(self):
        return self._not_divisible

divider = NumberDivider()
divider.add_number(1)
divider.add_number(3)
divider.add_number(4)
divider.add_number(6)
divider.add_number(7)
print(divider.divisible())
print(divider.not_divisible())

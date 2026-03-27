class SeeSaw:
    def __init__(self):
        self.Left_weight = 0
        self.Right_weight = 0

    def add_right(self, weight):
        self.Right_weight += weight

    def add_left(self, weight):
        self.Left_weight += weight

    def balance(self):
        if self.Left_weight == self.Right_weight:
            return '='
        elif self.Right_weight > self.Left_weight:
            return 'R'
        else:
            return 'L'

seesaw = SeeSaw()
seesaw.add_right(8)
seesaw.add_left(5)
seesaw.add_left(4)
print(seesaw.balance())

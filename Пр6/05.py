class FlipFlopBell:
    def __init__(self):
        self.Is_flip = True

    def ring(self):
        if self.Is_flip:
            print("flip")
            self.Is_flip = False
        else:
            print("flop")
            self.Is_flip = True

bell = FlipFlopBell()
bell.ring()
bell.ring()
bell.ring()

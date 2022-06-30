class Numbers:
    def __init__(self, *args):
        self.numbers = args
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < len(self.numbers):
            return self.numbers[self.i]
        else:
            self.i = -1
            raise StopIteration

numbers = Numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
for number in numbers:
    print(number)
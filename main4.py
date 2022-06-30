        a = 5

        def __init__(self, weight: int, lenght: int) -> None:
            self.weight = weight
            self.lenght = lenght

        def foo(self, value):
            self.lenght += value

        @classmethod
        def bar(cls) :
            cls.a += 1


transport_0 = Transport(3000, 4)
transport_1 = Transport_1(4000, 5)

print("transport_0")

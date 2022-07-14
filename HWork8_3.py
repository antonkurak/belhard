N: int = int(input("N: "))

numbers = list[list[int]] = []

for j in range(N):
    raw: list[int] = []
    for i in range(N):
        if i == j:
            raw.append(3)
        elif i < j:
            raw.append(2)
        else:
            raw.append(1)
    numbers.append(raw)
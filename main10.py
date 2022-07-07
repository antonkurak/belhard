numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
i = 0
while True:
    direction: str = input("direction: ")
    if direction == ">":
        i += 1
        if i == len(numbers):
            i = 0
            print(numbers[i])
    elif direction == "<":
        i -= 1
        if i == -1:
            i = len(numbers) - 1
            print(numbers[i])
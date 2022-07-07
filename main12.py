numbers: list[int] = [1, 5, 3, 4, 6, 8, 9, 7, 2]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] . numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)

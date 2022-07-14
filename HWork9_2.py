numbers: list[list[int]] = [
    [1, 2, 3, 4, 5],
    [-1, -2, -3, -4, -5],
    [-2, 5, 3, -1],
    [7, -3, -1, 5],
]
def get_abs_sum_negative_numbers(numbers: list[list[int]]) ->
    count: int = 0
    for raw in numbers:
        for number in raw:
            if number < 0 and number % 2:
                count += number
        return count * -1
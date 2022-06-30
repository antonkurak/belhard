numbers = [1, 0, 2, 3, 0, 5, 6, 7, 0, 8, 9]
print(numbers)
for number in numbers:
    if number == 0:
        numbers.remove(number)


print(numbers)        


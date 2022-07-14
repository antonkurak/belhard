lst = [1, 2, 3, 4, 5, 6, 7, 8]
n = int(input("Сместить список на: "))


def shift(lst_n):
    shifted_n = lst_n
    counter = 0
    while counter != n:
        shifted_n.insert(0, shifted_n.pop())
        counter += 1
    return shifted_n


print(shift(lst))
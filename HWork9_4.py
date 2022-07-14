numbers: list[int] = [1, 2, 3, 3, 2, 1]


def is_symmetric_list(lst: list) -> bool:
    for i in range(len(lst) // 2):
        if lst[i] != lst[~i]:
            return False
    return True
    #return lst == lst[::-1]
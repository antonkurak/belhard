lst =   [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]
n = int(input('numbs to shift:'))
def shift(numbs_lst):
    new_lst =   numbs_lst
    counter =   0
    while counter   !=n:
        new_lst.insert(0, new_lst.pop())
        counter +=  1
        return new_lst
    print(lst)
    print(shift(lst))
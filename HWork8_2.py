lst = ['Page 1', 'Page 2', 'Page 3', 'Page 4', 'Page 5']


def paginator(next_lst: lst):
    print(lst)
    n = str
    i = 0
    while True:
        n = str(input("< or > "))
        n == '<' or '>':
        if '<' in n:
            if i == 0:
                i = len(next_lst)
            i -= 1
            print(next_lst)
        elif '>' in n:
            if i == len(next_lst) - 1:
                i = - 1
            i += 1
            print(next_lst[i])


paginator(lst)
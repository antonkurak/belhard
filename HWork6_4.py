lst = ["1", "a", "2", "b", "3", "c", "4", "e"]
lst_alp = list(filter(lambda i: i.isalpha(), lst))
lst_dig = list(filter(lambda i: i.isdigit(), lst))
print(lst_alp, lst_dig)
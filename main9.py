#[
#   [0, 0, 0, 1, 0, 0, 0],
#   [0, 0, 1, 0, 1, 0, 0],
#   [0, 1, 0, 2, 0, 1, 0],
#   [1, 0, 3, 0, 3, 0, 1],
#]

from pprint import pprint

n: int = int(input("Введите глубину треугольника: "))
triangle: list = []
lst: list = []
for i in range(n+n-1):
    lst.append(0)
for i in range(n):    
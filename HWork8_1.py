# 1 Вариант
n = int(input("Введите глубину: "))


def pascal_triangle(rows):
    row = [1]
    for i in range(rows):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


print(pascal_triangle(n))

#2 Вариант
n: int = int(input("Глубина"))
triangle: list = []
lst: list = []
for i in range(n+n-1):
    lst.append(0)
for i in range(n):
    triangle.append(lst.copy())
print(triangle)

triangle[0][(n+n-1)//2] = 1

for i in range(1, n):
    for j in range(n+n-1):
        if j == 0:
            triangle[i][j] = triangle[i-1][j+1]
        elif j == n+n-2:
            triangle[i][j] = triangle[i-1][j-1]
        else:
            triangle[i][j] = triangle[i-1][j+1] + triangle[i-1][j-1]

for i, lst in enumerate(triangle):
    triangle[i] = '|'.join(list(map(str, filter(lambda x: x != 0, lst)))).center(n*2)

triangle: str = '\n'.join(triangle)
print(triangle)
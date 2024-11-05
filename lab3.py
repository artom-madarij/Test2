## Лабораторна робота з дисципліни "Алгоритмізація та програмування"
## Виконав: Мадярій Артьом Іванович(ІР-14)
## Лабораторна робота №3 (Варіант 12)

def cust_len(l):
    count = 0
    for i in l:
        count += 1
    return count


def number(x):
    if x >= 0:
        return cust_len(str(n))
    else:
        return 'Ваше число менше 0'


def create_matrix(size):
    matrix = []
    for i in range(size):
        line = [size] * size
        matrix.append(line)
    return matrix


def print_matrix(matr):
    for line in matr:
        for element in line:
            print(element, end='')
        print()


while True:
    try:
        n = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Введіть число!!!")
num = number(n)
print("Кількість цифр у числі:", num)

matrix = create_matrix(num)
print("Матриця:")
print_matrix(matrix)

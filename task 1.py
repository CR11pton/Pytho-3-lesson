# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint
count = 0
i = 0
searching_number = int(input('Введите цифру в диапазоне от 1 до 1000: '))
list_lenght = int(input('Задайте длину списка: '))
while i <= list_lenght-1:
    if randint(0, 1000) == searching_number:
        count += 1
        i += 1
    else:
        i += 1
print(f'Введённые число встречается в списке: {count} раз')

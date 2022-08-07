"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(spisok):
    for index in range(len(spisok)):
        if spisok[index] not in spisok[:index]:
            print('No')
        elif spisok[index] in spisok[:index]:
            print('Yes')

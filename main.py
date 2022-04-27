from collections import OrderedDict
from collections import Counter
from functools import reduce
#1 Commit
#2 Commit
while True:
    cmd = input("Пункт: ")

    if cmd == "1":
        def ret(*args):
            a = list()
            for i, x in enumerate(args):
                a.append(x)
            return list(a)
        print(ret(1, 2, 3, 4 ,5, 'wasd'))

    if cmd == "2":
        def sortr(lst):
            lst = [int(i) for i in lst]
            lst.sort(reverse=True)
            return list(lst)
        print(sortr([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    if cmd == "3":
        dct = OrderedDict()
        print('Введите 5 значений словаря')
        for i in range(5):
            value = input(f'Введите {i+1}-й элемент словаря: ')
            dct[i+1] = value
        print(dct)
        print("ID словаря: " + str(id(dct)))

        # Меняем местами первый и последний элементы
        first = list(dct.items())[0]
        last = list(dct.items())[-1]
        dct.move_to_end(key=first[0])
        dct.move_to_end(key=last[0], last=False)

        # Удаляем второй элемент
        second = list(dct.items())[1]
        del dct[second[0]]

        # Вставляем новый элемент
        new_key = input('Введите new_key: ')
        new_value = input('Введите new_value: ')
        dct[new_key] = new_value
        print(dct)
        print("ID словаря: " + str(id(dct)))

    if cmd == "4":
        dct_1 = {'a': 11, 'b': 33, 'c': 42, 'd': 1337, 'e': 444, 'f': 11}
        dct_2 = {'a': 13, 'c': 22, 'e': 44, 'f': 77, 'g': 404}

        def max_dct(*dicts):
            return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

        def sum_dct(*dicts):
            return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))

        print(max_dct(dct_1, dct_2))
        print(sum_dct(dct_1, dct_2))

    if cmd == "5":
        def tpl_sort(tpl):
            for element in tpl:
                if not isinstance(element, int):
                    return tpl
            return tuple(sorted(tpl))
        print(tpl_sort((10, 1, 3, 5, 2)))
        print(tpl_sort((10, 1, 3.14, 5, 2)))

    if cmd == "6":
        def del_from_tuple(tpl, element):
            lst = list(tpl)
            if element in tpl:
                lst.remove(element)
            return tuple(lst)
        tpl = input('Введите кортеж: ').split()
        element = input('Введите элемент: ')
        print(del_from_tuple(tpl, element))
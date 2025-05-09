from EVO import EVO

def nessesary(num):
    if num == 1:
        flag = 0
        options = ((" + 1", " + 2", " * 2"), (" + 1", " + 3"), (" + 1", " + 3"), (" + 1", " + 2", " + 4"), (" + 1", " + 2", " + 3"),
                (" + 1", " * 2", " * 3"), (" + 1", " * 2", " * 3"), (" + 1", " + 2", " * 3"), (" + 1", " * 2"),
                (" + 1", " * 2"), (" + 2", " * 2", " + 3"), (" + 1", " * 2", " + 3"), (" + 1", " * 2", " + 3"),
                (" + 1", " * 2"), (" + 1", " * 2"), (" + 1", " * 3" , " + 2"), (" + 1", " * 3" , " + 2"), (" + 1", " + 3" , " * 3"),
                (" + 1", " * 2"), (" + 1", " + 2", " * 2"), (" + 1", " * 3" , " + 2"), (" + 1", " * 2"), (" + 1", " * 3"),
                (" + 1", " * 3"), (" + 1", " * 3"), (" + 1", " * 3"), (" + 1", " + 2", " * 3"), (" + 1", " + 2", " * 3"),
                (" + 2", " * 2"), (" - 1", " // 3"), (" - 1", " // 2"), (" + 1", " + 2", " * 2"),
                (" - 2", " // 2"), (" - 2", " // 2"), )
        througs = ((10, ), (9, ), (8, ), (8, ), (8, ), (14, ), (15, ), (8, 10), (10, 21), (12, 25), (11, ),
                (10, ), (12, ), (18, ), (14, ), (10, 12), (9, 11), (10, 17), (10, ), (11, ),
                (9, ), (13, 30), (22, ), (20, ), (28, ), (26, ), (8, ), (10, ), (18, ), (33, ),
                (16, ), (11, 13), (14, ), (16, ), )
        numbers = ((3, 12), (1, 17), (1, 15), (1, 15), (1, 15), (2, 28), (2, 30), (2, 12), (1, 30), (1, 40), (2, 22),
                (2, 14), (3, 16), (3, 37), (2, 29), (1, 15), (2, 12), (4, 23), (1, 20), (4, 13),
                (3, 14), (3, 60), (1, 70), (1, 65), (2, 90), (2, 87), (1, 15), (1, 15), (1, 52), (67, 5),
                (78, 4), (4, 15), (30, 1), (38, 2), )
        answers = (60, 169, 81, 961, 1936, 38, 42, 60, 28, 40, 100, 81, 96, 28, 26, 504, 50, 324, 28, 50,
                112, 48, 45, 36, 56, 55, 651, 672, 96, 20, 1232, 100, 36, 36)
        inverses = (29, 30, 32, 33)
        doubles = ()
        for i in range(len(answers)):
            all = EVO(options[i], through=througs[i], inverse=i in inverses, double=i in doubles)
            if all.evo(*numbers[i]) != answers[i]:
                print(f'Неверно: {i} Получилось: {all.evo(*numbers[i])} Ответ: {answers[i]}, Вводные: {numbers[i]} и {througs[i]}')
                flag += 1
        if not flag:
            print('Всё верно')
        else:
            print("Всего неправильно:", flag)
    tt = EVO((" + 1", " + 2", " + 3"))  # Укажите наименьшее натуральное число,
    # которое нельзя получить из исходного числа 1,
    # выполнив программу исполнителя РазДва, содержащую не более пяти команд.
    if num == 2:
        hf = EVO((" + 1", " + 2", " + 3"), through=(7, ))
        answer = hf.evo(1, 35)
        print(answer, 381662184, answer == 381662184)


def esc():
    flag = 0
    options = ((" + 1", " * 2 + 1"), (" + 1", " * 2 + 1"), (" + 1", " * 2", " + 3"), (" + 1", " * 2", " + 3"),
               (" + 1", " * 2", " ** 2"), (" + 1", " * 2", " ** 2"), (" + 1", " * 2", " ** 2"),
               (" - 1", " * 2", " * 3"), (" - 1", " * 2", " * 3"), (" - 1", " + 3", " * 2"),
               (" - 1", " + 3", " * 2"), (" - 1", " / 2", " / 3"), (" - 1", " / 2", " / 3"), )
    escapes = ((26, ), (24, ), (6, 12), (5, 10), (11, ), (12, ), (14, ), None, None,
               None, None, (12, 15), (10, 15), )
    numbers = ((1, 27), (1, 25), (3, 16), (2, 14), (2, 20), (3, 25), (3, 25), (3, 20), (3, 15),
               (3, 12), (4, 14), (19, 1), (22, 1), )
    answers = (13, 10, 22, 26, 37, 21, 26, 4, 6, 53, 46, 43, 53)
    inverses = (11, 12)
    doubles = (7, 8, 9, 10)
    ddoubles = (1, 1, 1, 1)
    for i in range(len(answers)):
        all = EVO(options[i], escape=escapes[i], inverse=i in inverses, double=ddoubles[doubles.index(i)] if i in doubles else False)
        if all.evo(*numbers[i]) != answers[i]:
            print(f'Неверно: {i}', all.evo(*numbers[i]), answers[i], numbers[i])
            flag += 1
    if not flag:
        print('Всё верно')
    else:
        print("Всего неправильно:", flag)


# first = EVO((' + 1', " * 3"), through=(28, ))
# print(first.evo(2, 90))

# nessesary(1)
# nessesary(2)
# esc()
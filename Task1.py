school = {
    '1a': 15,
    '1b': 20,
    '2c': 25,
    '6a': 30,
    '7b': 35
}

if __name__ == '__main__':
    while True:
        print('Вывести количество учеников - введи ОБЩ - '
              '\nИзменить количество учеников в классе - введи ИЗМ - '
              '\nСоздать новый класс - введи НК - '
              '\nУдалить класс - введи УДАЛИТЬ - '
              '\nПосчитать общее количество учеников - введи СЧЕТ'
              '\nЗавершить программу - введи ВЫХ')

        deystvie = input('\nВведи команду - ')
        if deystvie == 'ОБЩ':
            print(school.items())
            print('\n')

        elif deystvie == 'ИЗМ' or deystvie == 'НК':
            nomer_classa = input('\n Введи класс который нужно изменить или создать - ')
            kolichestvo = input('\n Введи количество учеников для класса - ')
            school[nomer_classa] = kolichestvo

        elif deystvie == 'УДАЛИТЬ':
            nomer_classa = input('\n Введи класс который нужно удалить - ')
            print(nomer_classa)
            del school[nomer_classa]

        elif deystvie == 'СЧЕТ':
            sum = 0
            for key in school.keys():
                sum += school[key]

            print(sum)
            print('\n')

        elif deystvie == 'ВЫХ':
            break
        else:
            print('Команда не найдена, попробуйте снова\n')
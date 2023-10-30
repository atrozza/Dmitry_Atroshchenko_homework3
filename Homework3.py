# Dmitry Atroshchenko
# Date: 30/10/2023
# Description: Homework 3
# My version Python 3.11


    #Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    #Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    #Входные данные - строка из чисел, разделенная пробелами.
    #Выходные данные - количество пар.
    #Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.


def pairs(numbers_string):
    # Разбиваем строку на список чисел, используя пробел в качестве разделителя
    numbers = numbers_string.split()

    # Создаем словарь для подсчета количества каждого числа
    counts = {}

    # Переменная для хранения общего количества пар
    total_pairs = 0

    # Подсчитываем количество каждого числа в словаре
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Для каждого числа в словаре, вычисляем количество пар
    for count in counts.values():
        total_pairs += count * (count - 1) // 2

    return total_pairs


    #Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    #Элементы нужно выводить в том порядке, в котором они встречаются в списке.


def uniques(array):
    # Создаем список для хранения уникальных элементов
    unique_elements = []
    # Создаем множество для быстрой проверки видимых элементов
    seen = set()

    # Проходим по элементам в заданной переменной array
    for item in array:
        # Если элемент еще не встречался в нашем множестве seen
        if item not in seen:
            # Добавляем его в список уникальных элементов unique_elements
            unique_elements.append(item)
            # Добавляем его в множество seen для отслеживания
            seen.add(item)
        # Если элемент встречается повторно и уже был добавлен в список unique_elements
        elif item in unique_elements:
            # Удаляем его из списка уникальных элементов unique_elements
            unique_elements.remove(item)

    return unique_elements


    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Верните полученный список.
    # Задача не проходит тест. Такой вариант решения мог бы быть, но всего с одним исправлением - item == 0 (см ответы)


def ordered_list(array):
    # Создаем список non_zeros, который содержит все ненулевые элементы из введённой переменной array
    non_zeros = [x for x in array if x != 0]
    # Вычисляем количество нулей путем вычитания количества ненулевых элементов non_zeros из общего числа элементов.
    zero_count = len(array) - len(non_zeros)
    # Создаем новый список, добавляя ненулевые элементы сначала, а затем нули в количестве, соответствующем zero_count.
    return non_zeros + [0] * zero_count


    #Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.


def tuple_to_list(in_tuple):
    # Преобразовываем кортеж (in_tuple) в список с помощью встроенной функции list().
    return list(in_tuple)


    #Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself


def euclid(a,b):
    # В цикле, пока b не равно 0, выполняем следующие действия:
    while b:
        # Меняем значения переменных a и b.
        a, b = b, a % b
        # Это позволяет найти наибольший общий делитель (НОД) чисел a и b,
        # используя алгоритм Евклида.

    # Когда b становится равным 0, цикл завершается, и возвращается значение a,
    # которое является НОДом чисел a и b.
    return a


    #Dictionaries

    #Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    #Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    #Входные данные
    #Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    #В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    #Выходные данные
    #Для каждого из запроса выведите название страны, в котором находится данный город.
    #Пример данных:
    #Входные данные
    #2
    #Russia Moscow Petersburg Novgorod Kaluga
    #Ukraine Kiev Donetsk Odessa
    #3
    #Odessa
    #Moscow
    #Novgorod
    #Выходные данные
    #Ukraine
    #Russia
    #Russia
    #input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Donetsk Odessa\n3\nOdessa\nMoscow\nNovgorod"
    #output_string = 'Ukraine\nRussia\nRussia'
    #country_map={}


def cities(input_string):
    # Разбиваем входную строку на отдельные строки и удаляем начальные и конечные пробелы и символы новой строки.
    input_lines = input_string.strip().split('\n')
    # Получаем количество стран (n) из первой строки.
    n = int(input_lines[0])
    # Создаем пустой словарь country_map, который будет связывать города с соответствующими странами.
    country_map = {}

    # Обрабатываем информацию о странах и городах.
    for i in range(1, n + 1):
        country_and_cities = input_lines[i].split()
        country = country_and_cities[0]
        cities = country_and_cities[1:]
        for city in cities:
            if city in country_map:
                # Если город уже существует в словаре, добавляем текущую страну к списку стран для этого города.
                country_map[city].append(country)
            else:
                # Если город еще не существует в словаре, создаем новую запись для него.
                country_map[city] = [country]

    # Получаем количество запросов (M) из строки после информации о странах и городах.
    m = int(input_lines[n + 1])
    # Получаем список запросов о городах из строк после количества запросов.
    queries = input_lines[n + 2:]

    # Создаем список для хранения ответов.
    result = []
    # Обрабатываем запросы о городах и находим соответствующие страны.
    for city in queries:
        if city in country_map:
            countries = country_map[city]
            result.append(" ".join(countries))

    # Возвращаем ответы в виде строки, разделяя их символами новой строки.
    return '\n'.join(result)


    #Sets

    #Задачи для домашней работы
    #Языки
    #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    #Входные данные
    #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    #Пример входных данных:
    #3 # N количество школьников
    #2 # M1 количество языков первого школьника
    #Russian # языки первого школьника
    #English
    #3 # M2 количество языков второго школьника
    #Russian
    #Belarusian
    #English
    #3
    #Russian
    #Italian
    #French
    #Выходные данные
    #В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    #Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    #input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
    #output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'

def languages(input_string):
    # Разбиваем входную строку на строки
    lines = input_string.strip().split('\n')
    # Количество школьников
    N = int(lines[0])
    # Удаляем первую строку с количеством школьников
    lines = lines[1:]

    # Создаем множества для языков, которые знают все и хотя бы один
    all_languages = set()
    any_languages = set()

    # Множество для языков текущего школьника
    current_student_languages = set()

    for line in lines:
        # Строка с количеством языков у школьника
        if line.isdigit():
            if current_student_languages:
                # Добавляем языки текущего школьника к множеству языков, которые знает хотя бы один
                any_languages.update(current_student_languages)
                if not all_languages:
                    # Если all_languages пусто, копируем множество текущего школьника
                    all_languages.update(current_student_languages)
                else:
                    # Иначе, оставляем только языки, которые есть и в all_languages, и у текущего школьника
                    all_languages.intersection_update(current_student_languages)
            # Очищаем множество для следующего школьника
            current_student_languages = set()
        else:
            # Добавляем язык текущего школьника к его множеству
            current_student_languages.add(line)

    # Обработка последнего школьника
    if current_student_languages:
        any_languages.update(current_student_languages)
        if not all_languages:
            all_languages.update(current_student_languages)
        else:
            all_languages.intersection_update(current_student_languages)

    # Формирование результирующих строк
    result = []
    # Добавляем количество языков, которые знают все школьники
    result.append(str(len(all_languages)))
    # Добавляем языки, которые знают все школьники
    result.extend(sorted(all_languages))
    # Добавляем количество языков, которые знает хотя бы один школьник
    result.append(str(len(any_languages)))
    # Добавляем языки, которые знает хотя бы один школьник
    result.extend(sorted(any_languages))

    return '\n'.join(result)


    #Generators

    #Генераторы списков
    #Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
    #пример:


def list_gen(arr1, arr2):
    # Создаем новый список result, используя генератор списка.
    # Проходим по всем элементам arr1 и каждый эллемент в arr1 это x,
    # проходим по всем элементам arr2 и каждый эллемент в arr2 это y,
    # добавлям к каждому эллементу x каждый элемент y
    result = [x + y for x in arr1 for y in arr2]
    return result


    #Генераторы словарей

    #Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.


def dict_gen(N):
    # Создаем словарь result, используя генератор словаря.
    # Проходим по числам от 1 до N (включительно) и создаем пары ключ-значение,
    # где ключ - число от 1 до N, а значение - куб этого числа.
    result = {x: x**3 for x in range(1, N + 1)}
    return result


    #Кортежи

    #Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.


def multiplication_table(N):
    # Проходим по числам от 0 до N включительно
    for i in range(N + 1):
        # Создаем строку, представляющую строку таблицы умножения для текущего числа i
        # Используем генератор списка для создания списка результатов умножения i на числа от 0 до N
        row = ' '.join([str(i * j) for j in range(N + 1)])
        # Возвращаем текущую строку как результат генератора
        yield row
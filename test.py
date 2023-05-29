import string


# Рекурсивная функция взятия значения из B по индексу
def getValueByIndexFromB(indB):
    # Берем первоначальное значение из B по индексу
    valB = B[indB]

    # Пробуем получить числа из найденного значения. Их мб много
    numsB = getNumbersFromValue(valB)
    if len(numsB) < 1:  # Нет никаких чисел, возвращаем ответ
        return valB

    # Сканируем массив полученных чисел
    for i, v in enumerate(numsB):
        # Текущее обрабатываемое число
        numB = v
        # Получаем индекс из A по его значению
        indA = getIndexByValueFromA(numB)
        if indA < 0:  # Нет такого числа в A, переходим к следующему числу
            continue

        # Получаем подмененное значение для текущего числа
        strB = getValueByIndexFromB(indA)
        # Подменяем число на полученное строковое значение в предполагаемом результате
        valB = valB.replace(str(numB), strB, 1)

    return valB


# Получаем индекс из A по его значению
def getIndexByValueFromA(num):
    for i, v in enumerate(A):
        if v == num:
            return i

    return -1


# Получаем список чисел в виде строк из переданного значения
def getNumbersFromValue(val):
    numList = []

    num = ''
    for char in val:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                numList.append(int(num))
                num = ''
    if num != '':
        numList.append(int(num))

    return numList


if __name__ == "__main__":
    # Входной массив с цифрами
    A = [4, 5, 6, 7, 8, 'RRJ2700041BD', '95007_95008_95010-95048_95050_95052_95055-95058+RRJ-27-00041-BD']
    # Входной массив с символами и цифрами
    B = ['d', 'e', 'f+4', 'g+6', 'h+5', '95041~95121','(95007+95008+95010~95048+95050+95052+95055~95058)*^RRJ-27-00041-BD' ]
    # Результат
    R = []

    # Сканируем неизменяемый массив В
    for i in range(len(B)):
        # Получаем значение по индексу в конечном виде со всеми подменами
        val = getValueByIndexFromB(i)
        # Добавляем его в результат
        R.append(val)

    # Печатаем входные данные и получившийся результат
    print("A:", A)
    print("B:", B)
    print("R:", R)


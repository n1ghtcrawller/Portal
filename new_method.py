
A = ['ALL', 'OPT-2140-401', 'ALL+(RRJ-27-00041-BD)', 'RRJ-27-00041-BD', 'AA', 'BB', 'OPT-2140-402']
    # Входной массив с символами и цифрами
B = ['(95007~95031+95031~95073+95075~95999)', '95001~95050', '(95007+95008+95010~95048+95050+95052+95055~95058)*^RRJ-27-00041-BD', '95041~95121', '95010+95012+95020~95035', '95010~95021','AA+BB' ]
    # Результат
R = []


def getElementsFromValueB(val):
    if '*' in val:
        element = val.split('*')
    elif '^' in val:
        element = val.split('^')
    elif '|' in val:
        element = val.split("|")
    element = element[-1]
    return element


def getIdentificator():
    count = 0
    rslt_list = []
    for i in range(len(A)):
        getValueListByID(i)


def getValueListByID(id):
    for i in range(len(B)):
        if A[id] in B[i]:
            result = replaceValues(A[id], B[i])
            return result
        else:
            continue

def replaceValues(cir_id, value):
    indexA = A.index(cir_id)
    indexB = B.index(value)
    if cir_id in value:
        result = value.replace(cir_id, B[indexA])

    return result

print(getIdentificator())

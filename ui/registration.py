import json

def return_not_registered_values(i, item):
    return data["items"][i][item]


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


def write_json(filename, datas):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(datas, file, indent=2)
    file.close()


A = []
B = []
data = read("not_registered.json")
for i in data["items"]:
    A.append(i["cirID"])


def finder(cirID):
    try:
        indexA = A.index(cirID)
        result = f'Идентификатор {cirID} найден. Зарегестрировать?'
        return result
    except Exception as result:
        result = 'Идентификатор не найден.'
        return result


def registration_data(cirID):
    indexA = A.index(cirID)
    data["items"][indexA]["is_registered"] = "yes"
    write_json("new.json", data)
    del data["items"][indexA]







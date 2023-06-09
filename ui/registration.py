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
new_data = read("new.json")
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
    new_data_item = data["items"][indexA]
    new_data["items"].append(new_data_item)
    del data["items"][indexA]
    write_json("not_registered.json", data)
    write_json("new.json", new_data)


def transport(cirID):
    try:
        registration_data(cirID)

    except Exception as e:
        return e

# print(transport(""))
# print(data["items"])
# print(new_data["items"])

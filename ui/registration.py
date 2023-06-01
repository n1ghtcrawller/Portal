import json


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("not_registered.json")

def write_object(filename, datas):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(datas, file, indent=2)
    file.close()


def add_object(cirID, eval, resolve):
    item = {'cirID': cirID, 'evaluate': eval, 'resolve': resolve}
    data["items"].append(item)
    write_object('new.json', data)


def return_not_registered_values(i, item):
    return data["items"][i][item]


def get_registered(cirID, eval, resolve, is_registered, index):
    if data["items"][index][is_registered] == "yes":
        add_object(data["items"][index][cirID], data["items"][index][eval], data["items"][index][resolve])
        del data["items"][index][is_registered]



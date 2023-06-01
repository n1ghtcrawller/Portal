import json


def read(filename):
    with open(filename, 'r', encoding="UTF-8") as file:
        return json.load(file)


data = read("objects_file.json")


def write_object(filename, datas):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(datas, file, indent=2)
    file.close()

# добвляем объект в таблицу
def add_object(cirID, eval, resolve):
    item = {'cirID': cirID, 'evaluate': eval, 'resolve': resolve, "is_registered": ""}
    data["items"].append(item)
    write_object('objects_file.json', data)
    print("1.OK")

# cirID = input()
# eval = input()
# resolve = input()
# add_object(cirID, eval, resolve)



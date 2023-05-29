import json
from ui import calc

with open("ui/objects_file.json") as objects:
    data = json.loads(objects)



def getValueByCirID():
    for i in data["items"]:
        if i["resolve"] == "":
            getNumbersByValue()
        else:
            continue


result_list = []


def getNumbersByValue():
    global result_list
    for i in data["items"]:
        new_list = []
        if i["evaluate"] != "":
            result = getIndexByEval(calc.spliter(i["evaluate"]))
            for j in result:
                new_list.append(data["items"][j]["resolve"])
            result_list.append(new_list)




def getIndexByEval(Eval):
    lst_index = []
    list_of_cir_id = [i["cirID"] for i in data["items"]]
    for el in Eval:
        if el in list_of_cir_id:
            lst_index.append(list_of_cir_id.index(el))
        else:
            continue
    return lst_index


def split_the_list(lst):
    new_list = []
    for i in lst:
        new_list.append(i.split("~"))
    return counter(new_list)


def counter(lst):
    int_list = []
    for i in lst:
        int_list.append((unpacker(i)))
    print(del_sames(rewriter(int_list)))


def rewriter(lst):
    length = len(lst)
    new_list = []
    for i in range(length):
        for j in range(len(lst[i])):
            new_list.append(lst[i][j])
            new_list.sort()
    return new_list


def unpacker(list):
    a = list[0]
    b = list[1]
    new_list = []
    for i in range(int(b)-int(a)):
        new_list.append(int(list[0])+i)
    new_list.append(int(list[1]))
    return new_list


def stringer(lst):
    string = ""
    for i in lst:
        if lst.index(i) % 2 == 0:
            string += f'{i}~'
        elif i == lst[-1]:
            string += f'{i}'
        else:
            string += f'{i}+'
    return string


def del_sames(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    return calc.stringer(calc.range_list(temp))


if __name__ == "__main__":
    getNumbersByValue()
    for i in result_list:
        split_the_list(i)



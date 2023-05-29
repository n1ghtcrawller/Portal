import re
import xml.etree.ElementTree as ET

def regular_exception():
    f = open('list.txt', 'r', encoding='utf-8')
    for line in f:
        result = re.findall('[-+]?\+9\d\d\d\d|[-+]?\-9\d\d\d\d|9\d\d\d\d|[-+]?\*9\d\d\d\d|[-+]?\^9\d\d\d\d|RRJ-95', line)
        new_result = []

        for i in range(0, (len(result) - 1)):
            if i == 0:
                new_result.append(result[i])
                continue
            if '^' in result[i]:
                result[i] = '^' + result[i]
                new_result.append(result[i])
                continue

            if int(result[i]) > 0:
                result[i] = '+' + str(abs(int(result[i])))
                new_result.append(result[i])

            if int(result[i]) < 0:
                result[i] = '~' + str(abs(int(result[i])))
                new_result.append(result[i])
            if '-UP' in result[i]:
                result[i] = result[i] + "~95999"
                new_result.append(result[i])

            string_result = "\n".join(new_result)
            print(string_result)
regular_exception()
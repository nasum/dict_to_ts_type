sample_dict = {
    "error": False,
    "id": 1234,
    "name": "nasum",
    "jobs": [
        {
            "name": "lapras2",
            "address": {
                "coutry": "japan",
                "prefecture": "tokyo"
            }
        },
        {
            "name": "lapras1",
            "address": {
                "coutry": "japan",
                "prefecture": "tokyo"
            }
        },
        {
            "name": "lapras",
            "address": {
                "coutry": "japan",
                "prefecture": "tokyo"
            }
        }
    ],
    "address": {
        "country": "japan",
        "prefecture": "tokyo"
    }
}

def explore(edge, fileobj, num=1):
    for k, v in edge.items():
        if type(v) is dict:
            _add_tab(fileobj, num)
            fileobj.write('{0}: {{\n'.format(k))
            explore(v, fileobj, num + 1)
            _add_tab(fileobj, num)
            fileobj.write('};\n')
        elif type(v) is list:
            _add_tab(fileobj, num)
            fileobj.write('{0}: Array<any>;\n'.format(k))
        else:
            _add_tab(fileobj, num)
            type_st = _return_type_st(v)
            fileobj.write('{}: {};\n'.format(k, type_st))


def _return_type_st(param):
    typeObj = type(param)

    if typeObj is str:
        return "string"

    if typeObj is bool:
        return "boolean"

    if typeObj is int:
        return "number"

    return "any"


def _add_tab(fileobj, num):
    for _ in range(num):
        fileobj.write('\t')


if __name__ == "__main__":
    file = "type.ts"
    fileobj = open(file, "w", encoding = "utf_8")
    fileobj.write('export type {0} = {{\n'.format('Hoge'))
    print(sample_dict)
    explore(sample_dict, fileobj)
    fileobj.write('}\n')
    fileobj.close()




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

def return_type_st(param):
    typeObj = type(param)

    if typeObj is str:
        return "string"

    if typeObj is bool:
        return "boolean"

    if typeObj is int:
        return "number"

    return "any"

def explore(edge, fileobj):
    for k, v in edge.items():
        if type(v) is dict:
            fileobj.write('{0}: {{\n'.format(k))
            explore(v, fileobj)
            fileobj.write('};\n')
        elif type(v) is list:
            fileobj.write('{0}: Array<any>;\n'.format(k))
            # for item in v:
            #     if type(item) is dict:
            #         explore(item, fileobj)
            #     else:
            #         type_st = return_type_st(item)
            # print(item)  
            # fileobj.write('>\n'.format(k))
        else:
            type_st = return_type_st(v)
            fileobj.write('{}: {};\n'.format(k, type_st))

if __name__ == "__main__":
    file = "type.ts"
    fileobj = open(file, "w", encoding = "utf_8")
    fileobj.write('export type {0} = {{\n'.format('Hoge'))
    print(sample_dict)
    explore(sample_dict, fileobj)
    fileobj.write('}\n')
    fileobj.close()

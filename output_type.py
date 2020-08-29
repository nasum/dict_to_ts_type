from py2tstype import explore

SAMPLE_DICT = {
    "error": False,
    "id": 1234,
    "name": "nasum",
    "jobs": [
        {
            "name": "company2",
            "address": {
                "coutry": "japan",
                "prefecture": "tokyo"
            }
        },
        {
            "name": "company1",
            "address": {
                "coutry": "japan",
                "prefecture": "tokyo"
            }
        },
        {
            "name": "company0",
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



if __name__ == "__main__":
    file = "type.ts"
    fileobj = open(file, "w", encoding = "utf_8")
    fileobj.write('export type {0} = {{\n'.format('Hoge'))
    print(SAMPLE_DICT)
    line_list = explore(SAMPLE_DICT)

    for line in line_list:
        fileobj.write(line)

    fileobj.write('}\n')
    fileobj.close()




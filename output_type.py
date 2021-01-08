from typing import List
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

def walk_throw(node_list: List):
    for node in node_list:
        tab = ""
        for _ in range(node.depth):
            tab += " "
        print(tab + str(node))
        walk_throw(node.children)


if __name__ == "__main__":
    print('json')
    print(SAMPLE_DICT)
    ast = explore(SAMPLE_DICT)
    print('ast')
    walk_throw(ast)




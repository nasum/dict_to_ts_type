# -*- coding: utf-8 -*-
from typing import List

def explore(edge, num=1) -> List[str]:
    line_list = []

    for k, v in edge.items():
        if type(v) is dict:
            first_line = _add_tab('{0}: {{\n'.format(k), num)
            line_list.append(first_line)

            for line in explore(v, num + 1):
                line_list.append(line)

            last_line = _add_tab('};\n', num)
            line_list.append(last_line)
        elif type(v) is list:
            line = _add_tab('{0}: Array<any>;\n'.format(k), num)
            line_list.append(line)
        else:
            type_st = _return_type_st(v)
            line = _add_tab('{}: {};\n'.format(k, type_st), num)
            line_list.append(line)

    return line_list


def _return_type_st(param):
    typeObj = type(param)

    if typeObj is str:
        return "string"

    if typeObj is bool:
        return "boolean"

    if typeObj is int:
        return "number"

    return "any"


def _add_tab(line, num):
    tab_line = ''
    for _ in range(num):
        tab_line += '\t'
    return tab_line + line

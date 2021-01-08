# -*- coding: utf-8 -*-
import dataclasses
from typing import List

@dataclasses.dataclass
class Node:
    key: str
    node_type: str
    raw_value: str
    children: List['Node']
    depth: int

    def __str__(self):
        return f'key: {self.key}, type: {self.node_type}, val: {self.raw_value}'

    def to_str(self) -> str:
        if self.node_type == 'Array':
            return f'{self.key}: Array<{self.node_type}>'
        else:
            return f'{self.key}: {self.node_type}'

    def is_premitive(self) -> bool:
        if node_type in ['number', 'string', 'boolean']:
            return True
        return False

def explore(edge: dict, num=1):
    node_list = []
    for k, v in edge.items():
        node = None
        children = []
        if type(v) is dict:
            type_st=''.join([word.capitalize() for word in k.split('_')]),
            children = explore(v, num + 1)
        elif type(v) is list:
            type_st = 'Array'
            children = _create_list_node(v, num)
        else:
            type_st = _return_type_st(v)

        node = Node(
            key=k,
            node_type=type_st,
            raw_value=str(v),
            children=children,
            depth=num
        )
        node_list.append(node)
    return node_list

def _create_list_node(val, num):
    children = []
    for v in val:
        tmp_type_st = _return_type_st(v)
        if tmp_type_st == 'dict':
            tmp_children = explore(v, num + 2)
            children.append(
                Node(
                    key=None,
                    node_type='dict',
                    raw_value=str(v),
                    children=tmp_children,
                    depth=num + 1
                )
            )
        else:
            tmp_type_st = _return_type_st(v)
            children.append(
                Node(
                    key=None,
                    node_type=tmp_type_st,
                    raw_value=str(v),
                    childrend=[],
                    depth=num + 1
                )
            )
    return children


def _return_type_st(param):
    typeObj = type(param)

    if typeObj is str:
        return "string"

    if typeObj is bool:
        return "boolean"

    if typeObj is int:
        return "number"

    if typeObj is dict:
        return "dict"

    return "any"

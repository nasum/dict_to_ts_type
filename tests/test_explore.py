# -*- coding: utf-8 -*-
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

def test_explore():
    assert False

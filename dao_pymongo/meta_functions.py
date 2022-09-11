import numpy as np


def test_installation():
    print("package dao_pymongo correctly installed")


def is_compound(object):
    if (
        isinstance(object, list)
        or isinstance(object, tuple)
        or isinstance(object, dict)
        or isinstance(object, np.ndarray)
    ):
        return True
    else:
        return False


def get_values_from_compound(object):
    return list(object.values()) if isinstance(object, dict) else object

from typing import Callable


def group(f: Callable, x: list) -> dict:
    """Groups list items by f(item) in a dictionary
    :param f: function with return value
    :x: list of items to be grouped
    """
    group_dict: dict = {}
    for item in x:
        val = f(item)
        if val in group_dict:
            group_dict[val].append(item)
        else:
            group_dict[val] = [item]
    return group_dict

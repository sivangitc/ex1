def find_all(string: str, subs: str, overlapping: bool = True) -> list:
    """Returns list of all indexes where substring occures in given string"""
    found_indexes = []
    i = 0
    while i < len(string):
        idx = string.find(subs, i)
        if idx == -1:
            break
        found_indexes.append(idx)
        if overlapping:
            i = idx + 1
        else:
            i = idx + len(subs)
    return found_indexes

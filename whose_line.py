import math
import os


def avg_diff(l1: list, l2: list) -> float:
    return sum([abs(l1[i] - l2[i]) for i in range(len(l1))]) / len(l1)


def no_whitespace(li: list) -> list:
    return [s.lstrip() for s in li]


def remove_line_whitespace(s: str) -> str:
    return '\n'.join([line.strip() for line in s.split('\n')])


def has_dup(li: list) -> bool:
    return len(li) != len(list(set(li)))


def flatten(li: list) -> list:
    return sum([flatten(sublist) for sublist in li], []) if (li and isinstance(li, list)) else [li]


def grep(folder: str, string: str) -> list:
    return [file for file in os.listdir(folder) if string in open(os.path.join(folder, file)).read()]


if __name__ == "__main__":
    assert avg_diff([1, 2, 1, 2], [2, 1, 2, 1]) == 1.0
    assert no_whitespace(["   string", "string   ", "\t\t\tstring\t", " \t"]) == ["string", "string   ", "string\t", ""]
    assert remove_line_whitespace("\nLine\n   Another Line\t\n  \tMore Lines\n\t \t So manyy\n   \n\n") == "\nLine\nAnother Line\nMore Lines\nSo manyy\n\n\n"
    assert not has_dup([1, 2, 3, 4])
    assert has_dup(["a", "aa", "b", "aa"])
    assert flatten([[[25, 15, 21], [1, 18, 5]], 3, 12, 5, 22, 5, 18]) == [25, 15, 21, 1, 18, 5, 3, 12, 5, 22, 5, 18]
    print(grep("Babynames", "Aja"))

    print("ALL GOOD")

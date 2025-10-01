from itertools import groupby

def group_by_first_letter(words):
    words_sorted = sorted(words, key=lambda x: x[0])
    return {k: list(g) for k, g in groupby(words_sorted, key=lambda x: x[0])}

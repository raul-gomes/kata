"""
import re

def solution(s):
    return re.findall(".{2}", s + "_")



from itertools import izip_longest


def solution(s):
    return [''.join(a) for a in izip_longest(s[::2], s[1::2], fillvalue='_')]
"""

def solution(s):
    list_a = []
    list_b = []
    for index, char in enumerate(s):
        if (index % 2 == 0):
            list_a.append(char)
        else:
            list_b.append(char)
           
    if len(list_a) != len(list_b):
        list_b.append('_')

    return [f'{a}{b}'for a, b in zip(list_a, list_b)]

if __name__ == '__main__':
    print(solution('asdqwrq'))
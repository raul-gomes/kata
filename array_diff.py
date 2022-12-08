from typing import List

"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]

"""

matriz_a = [1,2,2,2,3]
matriz_b = [2]
matriz_c = [1,2,2]
matriz_d = [1]
matriz_e = []
matriz_f = [1,2]
matriz_g = [-7, -1, -2, -12, 8, 10, 4, -10, 17]
matriz_h = [-6, -8, 16, 1] 


def array_diff(matriz_a: List[int], matriz_b: List[int]):

    return [num for num in matriz_a if num not in matriz_b]

if __name__ == '__main__':
    print(array_diff(matriz_a, matriz_b))
    print(array_diff(matriz_c, matriz_d))
    print(array_diff(matriz_c, matriz_e))
    print(array_diff(matriz_g, matriz_h))



import numpy as np

lista_animacion = []
    
def merge_arrs(left, right):
    left_idx, right_idx = 0, 0

    final_arr = []

    while left_idx < len(left) or right_idx < len(right):

        if left[left_idx] < right[right_idx]:
            final_arr.append(left[left_idx])
            left_idx+=1
        else:
            final_arr.append(right[right_idx])
            right_idx+=1

        if left_idx == len(left):
            final_arr.extend(right[right_idx:])
            break
        if right_idx == len(right):
            final_arr.extend(left[left_idx:])
            break
    
    return final_arr

@staticmethod
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, lista_animacion

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    left, aa = merge_sort(left)
    right, aa = merge_sort(right)
    
    result = list(merge_arrs(left, right))

    lista_animacion.append(result)
    
    return (result, lista_animacion)

def animation_arrays(arrs, original_arr):
    results = []

    for ar in arrs:
        indices = list(np.isin(original_arr, ar).nonzero()[0])

        original_arr[indices[0]:indices[-1] + 1] = ar

        results.append(original_arr[:])

    return results
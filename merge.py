array = [[9, 3], [4, 2], [5, 1]]

def merge_arrs(arr1, arr2):
    a = 0
    b = 0

    #c = 0
    f_arr = []

    while (a + b) < (len(arr1) * 2 ):
        if a == len(arr1):
            f_arr.append(arr2[b])
            b += 1
            continue
        elif b == len(arr2):
            f_arr.append(arr1[a])
            a += 1
            continue

        if arr1[a] < arr2[b]:
            f_arr.append(arr1[a])
            a+=1
        else:
            f_arr.append(arr2[b])
            b += 1


    
    return f_arr

sorted = merge_arrs(array[0], array[1])


print(sorted)
import numpy as np

class Sort():
    def __init__(self):
        self.array = [4, 9, 2, 3, 8, 1, 11, 6, 7]
        #self.array = np.random.choice(range(1, 100), size=50, replace=False)
        #self.array = list(self.array)
        #print(self.array)

    


    def merge_sort(self):
        new_array = []
        
        def merge_arrs(arr1, arr2):
            a = 0
            b = 0

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
        
        for a in self.array:
            new_array.append([a])
        self.array = new_array

        
        while len(self.array) != 1:
            new_array = []
            for a in range(0, len(self.array), 2):
                s_arrs = merge_arrs(self.array[a], self.array[a + 1])
                new_array.append(s_arrs)

            self.array = new_array
            print(new_array)
        
        self.array = self.array[0]

        return self.array
    



sort = Sort()

arr = sort.merge_sort()

print(arr)

def MergeSort(array):
    print("Splitting", array)
    if len(array) > 1:
        mid = len(array)//2
        lefthalf = array[mid:]
        righthalf = array[:mid]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i =+ 1
            else:
                array[k] = righthalf[j]
                j =+ 1
            k =+ 1

        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i =+ 1
            k =+ 1

        while j < len(righthalf):
            array[k] = righthalf[j]
            j =+ 1
            k =+ 1

    print("Merging", array)


array = [90, 60, 100, 40, 50, 20, 10, 30, 70, 80]
MergeSort(array)
print(array)
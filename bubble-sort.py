array = [90, 60, 100, 40, 50, 20, 10, 30, 70, 80]
n = len(array)
for i in range(n):
    alreadySorted = True
    for j in range(n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            alreadySorted = False
    if alreadySorted:
        print(array)
        break
dataset = [0, 14, 32, 18, 64, 7, 10]
i = 2
for i in range(len(dataset)):
    key = dataset[i]
    j = i - 1
    while j > 0 and dataset[j] > key:
        dataset[j + 1] = dataset[j]
        print(dataset)
        j = j - 1
    dataset[j + 1] = key
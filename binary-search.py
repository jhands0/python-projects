import sys
dataset = [0, 1, 5, 18, 32, 35, 64, 99, 101, 400]
min = 0
max = len(dataset)
target = 64

while min < max:
    midpoint = (min + max) / 2
    if dataset[int(midpoint)] == target:
        print("True")
        sys.exit(1)
    elif dataset[int(midpoint)] > target:
        max = int(midpoint) - 1
    elif dataset[int(midpoint)] < target:
        min = int(midpoint) + 1
print("False")
sys.exit(1)
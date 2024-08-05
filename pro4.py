def demo(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1

elements = [1, 3, 5, 8, 10, 23, 35]
target = 10
result = demo(elements, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found in the list.")


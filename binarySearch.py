container = [4, 10, 25, 40, 54, 78, 85, 100]

item = 78

def binary_search(list, item):
    left = 0
    right = len(list) - 1 

    while left <= right:
        mid = (left + right) // 2 
        print(left, right, mid)
        if item < list[mid]:
            right = mid - 1 
        elif item > list[mid]:
            left = mid + 1 
        else:
            return f"Item {item} found in index {mid}"

    return f"Item {item} not found in the container"

print(binary_search(container, item))
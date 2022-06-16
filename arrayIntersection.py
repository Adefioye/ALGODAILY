arr1 = ["green", "orange", "blue", "red"]
arr2 = ["black", "green", "red", "purple"]
arr3 = ["orange"]

nums1 = [1, 2, 2, 1];
nums2 = [2, 2];

nums3 = [4,9,5];
nums4 = [9,4,9,8,4];

# BRUTE FORCE SOLUTION O(n^2)

def array_intersection(array1, array2):
    
    result = []

    for i in array1:
        for j in array2:
            if i == j and i not in result:
                result.append(i)

    return result if len(result) > 0 else "No common items in both arrays"

# print(array_intersection(arr1, arr2))
# print(array_intersection(arr3, arr2))
# print(array_intersection(nums1, nums2))
# print(array_intersection(nums3, nums4))

#
def array_intersection1(array1, array2):
    result = []

    for i in array1:
        if i in array2 and i not in result:
            result.append(i)

    return result if len(result) > 0 else "No common items in both arrays"

print(array_intersection1(arr1, arr2))
print(array_intersection1(arr3, arr2))
print(array_intersection1(nums1, nums2))
print(array_intersection1(nums3, nums4))




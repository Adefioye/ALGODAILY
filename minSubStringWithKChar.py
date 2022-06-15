# “HGFDSAXZBJKC”
# "ABKC"

# 1) Register string in right pointer in window hashmap
# 2) Check if right pointer in target map and if value in window hashmap <= target map 

## Minimizing the window after getting string match
# 3) while left <= right and count == len(target) 

def minSubStringWindow(search_string, target):

    if target == "": return "Not found"

    window_map, target_map = {}, {} 
    have, need = 0, len(target) 
    res, resLens = [-1, -1], float("inf")
    left = 0

    for i in target:
        target_map[i] = 1 + target_map.get(i, 0) 

    for right in range(len(search_string)):
        current_char = search_string[right]
        window_map[current_char] = 1 + window_map.get(current_char, 0)

        if current_char in target_map and window_map[current_char] == target_map[current_char]:
            have += 1

        while have == need:
            if right - left + 1 < resLens:
                res = [left, right]
                resLens = right - left + 1 
            
            left_char = search_string[left] 
            window_map[left_char] -= 1 

            if left_char in target_map and window_map[left_char] < target_map[left_char]:
                have -= 1

            left += 1

    left, right = res 
    
    return search_string[left : right + 1] if resLens != float("inf") else "Not found"


# print(minSubStringWindow("HGFDSAXZBJKC", "ABKC"))
print(minSubStringWindow("HGFDSAXZBJKC", "BKW"))



# “HGFDSAXZBJKC”
# "ABKC"

# 1) Register string in right pointer in window hashmap
# 2) Check if right pointer in target map and if value in window hashmap <= target map 

## Minimizing the window after getting string match
# 3) while left <= right and count == len(target) 

def minWindowSubString(searchString, target):

    target_map, window_map = {}, {}
    have, need = 0, len(target)
    res, resLens = [-1, -1], float("inf")
    left = 0

    for i in target: 
        target_map[i] = 1 + target_map.get(i, 0)

    for right in range(len(searchString)):
        window_map[searchString[right]] = 1 + window_map.get(searchString[right], 0)
        if (searchString[right] in target_map) and (window_map[searchString[right]] == target_map[searchString[right]]):
            have += 1
        
        while have == need:
            # Check if len of pointers is less than resLens and update resLens
            print(f"Left: {left}, Right: {right}")
            if right - left + 1 < resLens:
                resLens = right - left + 1 
                res = [left, right]
            
            # Lets contract the window by popping the left and going rightwards 
                print(res, resLens)
            window_map[searchString[left]] -= 1 

            if (searchString[left] in target_map) and (window_map[searchString[left]] < target_map[searchString[left]]):
                have -= 1

            print(f"Have: {have}")
            left += 1 

    return f"Minimum substring is {searchString[res[0]: res[1] + 1]} and length is {resLens}"


print(minWindowSubString("HGFDSAXZBJKC", "ABKC"))



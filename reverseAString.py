demo_string = "abcde"

## BRUTE FORCE SOLUTION 0(n)
def reverse_a_string(sample_string):

    result = []
    
    if len(sample_string) == 0:
        return "No string to reverse"

    if len(sample_string) == 1:
        return sample_string

    for i in range(len(sample_string) - 1, -1, -1):
        result.append(sample_string[i])

    return "".join(result)


# print(reverse_a_string(""))
# print(reverse_a_string("d"))
# print(reverse_a_string("shsh"))
# print(reverse_a_string(demo_string))

## USING 2-POINTER APPROACH 

def reverse_a_string_1(sample_string):

    if len(sample_string) == 0:
        return "No string to reverse"

    if len(sample_string) == 1:
        return sample_string

    left = 0 
    right = len(sample_string) - 1 
    result = list(sample_string)
    print(result)

    while left < right:
        # SWAP
        left_hand = result[left]
        result[left] = result[right]
        result[right] = left_hand 
        left += 1 
        right -= 1

    return "".join(result)

# print(reverse_a_string_1("ab123"))
print(reverse_a_string_1("1234"))
print(reverse_a_string("abcde"))


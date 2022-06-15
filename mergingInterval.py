intervals = [(10, 13), (12, 25), (4, 32), (7, 15), (2, 8), (9, 35)]
sorted_intervals = [(2, 8), (4, 32), (7, 15), (9, 35), (10, 13), (12, 25)]

def merge_intervals(intervals):
    # 1) We sort the array
    # 2) Set initial output to the 1st interval of the sorted intervals
    # 3) Iterate over the remaining intervals and
    # .3.1). Merge when start of each item less than or equal to the end of the last interval in intervals
    #  3.2) Otherwise append the item to the list
    inputs = list(map(list, intervals))
    inputs.sort(key = lambda x: x[0])
    output = [list(inputs[0])]

    print(inputs)
    for start, end in inputs[1:]:
        left_end = output[-1][1] 
        
        if start <= left_end:
            output[-1][1] = max(left_end, end)
        else:
            output.append([start, end])

    return list(map(tuple, output))

print(merge_intervals(intervals))

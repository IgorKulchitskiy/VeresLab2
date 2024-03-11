def sorting(tuples):
    for i in range(len(tuples)):
        for j in range(i + 1, len(tuples)):
            if tuples[i][0] > tuples[j][0]:
                tuples[i], tuples[j] = tuples[j], tuples[i]

    merged = []
    for interval in sorted(tuples):
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

tuples = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
merged_intervals = sorting(tuples)
print(merged_intervals)

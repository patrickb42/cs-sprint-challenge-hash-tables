def intersection(arrays):
    counter = {}
    for arr in arrays:
        for item in arr:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
    return [key for (key, value) in counter.items() if value == len(arrays)]

def has_negatives(a):
    return intersection([
        [-item for item in a if item < 0],
        [item for item in a if item > 0],
    ])


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

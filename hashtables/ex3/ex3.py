def intersection(arrays):
    counter = {}
    for arr in arrays:
        for item in arr:
            if item in counter:
                counter[item] += 1
            else:
                counter[item] = 1
    return [key for (key, value) in counter.items() if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

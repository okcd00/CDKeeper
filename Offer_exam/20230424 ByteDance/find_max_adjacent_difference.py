def find_maximum_adjacent_difference(values):
    bucket_size = (max(values) - min(values)) / len(values)
    buckets = [[] for _ in range(len(values)+1)]
    for v in values:
        index = int(v // bucket_size)
        buckets[index].append(v)
    min_in_buckets = [min(items) if items else None for items in buckets]
    max_in_buckets = [max(items) if items else None for items in buckets]
    # print(min_in_buckets, max_in_buckets)
    ret = 0
    for i, b in enumerate(buckets):
        if i == len(buckets) - 1:
            continue
        if max_in_buckets[i] is None:
            continue
        pivot = i + 1
        while min_in_buckets[pivot] is None:
            pivot += 1
            if pivot == len(min_in_buckets):
                break
        diff = min_in_buckets[pivot] - max_in_buckets[i]
        if diff > ret:
            ret = diff
    return ret


if __name__ == "__main__":
    a = [1.1, 3.3, 8.8, 9.9, 5.5]
    ret = find_maximum_adjacent_difference(a)
    print(ret)

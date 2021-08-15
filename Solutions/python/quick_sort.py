def quick_sort_simple(data):
    # sort the list
    if len(data) >= 2:
        # any number is fine
        mid = data[0]  
        left, right = [], []
        for num in data[1:]:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data


def quick_sort(data_list, l=None, r=None):
    # from Weimin Yan's "Data Structure"
    if l is None and r is None:
        l, r = 0, len(data_list) - 1

    def paritition(data, low, high):
        pivot = data[low] + 0
        while low < high:
            while low < high and data[high] >= pivot:
                high -= 1
            # set data[low] as the right-most num < data[pivot]
            # print(f"data[{low}]: {data[low]} -> {data[high]}")
            data[low] = data[high]  
            while low < high and data[low] <= pivot:
                low += 1
            # set data[high] as the left-most num > pivot
            # print(f"data[{high}]: {data[high]} -> {data[low]}")
            data[high] = data[low]  
        # print(f"data[{low}]: {data[low]} -> {pivot}")
        data[low] = pivot          
        return low

    if l < r:
        p = paritition(data_list, l, r)
        quick_sort(data_list, l, p-1)
        quick_sort(data_list, p+1, r)
    
    return data_list


def quick_find(data, k):
    # find the k-th smallest number
    if len(data) >= 2:
        # any number is fine
        mid = data[0]
        left, right = [], []
        for num in data[1:]:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        if len(left) == k - 1:
            return mid
        elif len(left) < k - 1:
            return quick_find(right, k=k-len(left)-1)
        else:  # len(left) > k - 1
            return quick_find(left, k=k)
    else:
        return data[0]


if __name__ == "__main__":
    dat = [2,3,4,51,1,1,53,26,3,4,16]
    print(quick_sort(dat))
    print(quick_find(dat, k=3))

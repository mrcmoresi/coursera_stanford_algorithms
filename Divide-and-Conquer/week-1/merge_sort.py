def merge_sort(input_lst):
    if len(input_lst) <= 1:
        return input_lst
    else:
        middle_point = len(input_lst) // 2
        print(middle_point)
        left, right = input_lst[:middle_point], input_lst[middle_point:]
        print(left, right)
        left = merge_sort(left)
        right = merge_sort(right)

        return merge(left, right)

def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        print(left, right)
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res


if __name__=='__main__':
    unsorted_list = [3,5,1,6]
    print(unsorted_list)
    res = merge_sort(unsorted_list)
    print(res)
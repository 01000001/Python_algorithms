def merge_sort(input_to_sort):
    
    if len(input_to_sort) <=1:
        return input_to_sort
    
    length_middle = len(input_to_sort)//2
    left = input_to_sort[:length_middle]
    right = input_to_sort[length_middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left, right):
    result = []
    #assign the element of the sublists to 'result' variable until
    #there is no element to merge. 

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            #compare the first two element, which is the small one,
            #of each two sublists.
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]

    return result

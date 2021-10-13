def triple_and_filter(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.
    
        >>> triple_and_filter([1, 2, 3, 4])
        [12]
        
        >>> triple_and_filter([6, 8, 10, 12])
        [24, 36]
        
        >>> triple_and_filter([1, 2])
        []
    """
    # way 1: way too long
    list = []
    filter_nums = []
    for num in nums:
        if num % 4 == 0:
            filter_nums.append(num)
   
    for num in filter_nums:
        list.append(num*3)
    return list

    # # way 2: one-line-code (comprehension)
    # return[num*3 for num in nums if num % 4 == 0] 

print(triple_and_filter([1, 2, 3, 4]))
print(triple_and_filter([6, 8, 10, 12]))
print(triple_and_filter([1, 2]))
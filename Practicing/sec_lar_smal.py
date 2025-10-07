def sec_lar_smal(list):
    smallest=second_smallest=float("inf")
    largest=second_largest=float("-inf")
    for i in list:
        if i < smallest:
            second_smallest=smallest
            smallest=i
        elif smallest < i < second_smallest:
            second_smallest = i
        
        if i > largest:
            second_largest=largest
            largest=i
        elif largest > i > second_largest:
            second_largest = i
    if second_smallest == float("inf") or second_largest == float("-inf"):
        return None,None
    return second_smallest,second_largest
list =[1,12,9,5,10,20,14,20]
small,large=sec_lar_smal(list)
print("second smallest",small)
print("second largest",large)

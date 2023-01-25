# Implement a Python function that takes a list of integers and a target number as input, 
# and returns a tuple of two integers that add up to the target number.

def two_sum(arr, target):

    # If the length of array is already less than 2.
    if len(arr) < 2:
        return -1

    # initialising two pointers fro tracking high and low.
    l = 0
    h = len(arr)-1

    while l<h:
        if arr[l] + arr[h] == target:
            return (arr[l], arr[h])
        elif arr[l] + arr[h] > target:
            h -=1
        else:
            l +=1
    # returning -1 incase no possible combinations found
    return -1
def right_rotate(lst, k):
    # Write your code here
    k = 0 if len(lst) == 0 else k % len(lst)
    return lst[-k:] + lst[:-k] # First part: remove the last k numbers from the beginning, Second part: Remove the last k from the end

right_rotate([1, 2, 3, 4, 5], 2)

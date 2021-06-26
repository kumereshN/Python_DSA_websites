def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            if pos != i:
                nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1


# Alternative (Choose this as it's faster)
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    c=0 # Keep track of the index of 0.
    for i in range(len(nums)):
        if nums[i]!=0: # If the number is a non-zero
            nums[c],nums[i]=nums[i],nums[c] # Swap the number of index c, which is 0, with the number of index i with a non-zero number.
            c+=1 # Increment by 1 as it's swapped.
    return nums

moveZeroes([0,1,0,3,12])

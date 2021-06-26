def productExceptSelf(nums):
    # The length of the input array
    length = len(nums)

    # The left and right arrays as described in the algorithm
    L, R, answer = [0]*length, [0]*length, [0]*length

    # L[i] contains the product of all the elements to the left
    # Note: for the element at index '0', there are no elements to the left,
    # so the L[0] would be 1
    L[0] = 1
    for i in range(1, length):

        # L[i - 1] already contains the product of elements to the left of 'i - 1'
        # Simply multiplying it with nums[i - 1] would give the product of all
        # elements to the left of index 'i'
        L[i] = nums[i - 1] * L[i - 1]

    # R[i] contains the product of all the elements to the right
    # Note: for the element at index 'length - 1', there are no elements to the right,
    # so the R[length - 1] would be 1
    R[length - 1] = 1
    for i in reversed(range(length - 1)):

        # R[i + 1] already contains the product of elements to the right of 'i + 1'
        # Simply multiplying it with nums[i + 1] would give the product of all
        # elements to the right of index 'i'
        R[i] = nums[i + 1] * R[i + 1]

    # Constructing the answer array
    for i in range(length):
        # For the first element, R[i] would be product except self
        # For the last element of the array, product except self would be L[i]
        # Else, multiple product of all elements to the left and to the right
        answer[i] = L[i] * R[i]

    return answer

# Alternative

def productExceptSelf(nums):
    ## RC ##
    ## APPROACH ##
    ## Using division is simple ##
    # we can make use of the product of all the numbers to the left and all the numbers to the right of the index. Multiplying these two individual products would give us the desired result as well. ##
    # ==> left product [1,2,3,4] ==> [1,1,2,6] (left to right)
    # ==> right product [1,2,3,4] ==> [24,12,4,1] (right to left)
    # ==> multiplying these two will get answer.

	## TIME COMPLEXITY : O(N) ##
	## SPACE COMPLEXITY : O(N) ##

    size = len(nums)
    leftProduct = [0]*size
    rightProduct = [0]*size
    leftProduct[0] = 1
    rightProduct[size-1] = 1

    for i in range(1,size):
        leftProduct[i] = leftProduct[i-1] * nums[i-1]
        rightProduct[size-i-1] = rightProduct[size-i] * nums[size-i]

    ans = []
    for i in range(size):
        ans.append(leftProduct[i] * rightProduct[i])
    return ans

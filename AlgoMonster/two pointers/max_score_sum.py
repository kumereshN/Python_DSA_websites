def maxSum(arr1, arr2):
    i, j, m, n = 0, 0, len(arr1), len(arr2)
    curNums1Sum, curNums2Sum = 0, 0

    while i < m and j < n:
        # Find the smaller number for each array where the pointer is and add it to their respective curNumsSum
        if arr1[i] < arr2[j]:
            curNums1Sum += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            curNums2Sum += arr2[j]
            j += 1
        else:
            # Both pointers are pointing to the "Teleporter number" (Same number).
            # Find the curMaxSum and add the "Teleporter number" (Can be either arr1[i] or arr2[j])
            # Set the curNums1Sum and curNums1Sum to be curMaxSum
            curNums1Sum = curNums2Sum = max(curNums1Sum, curNums2Sum) + arr1[i]
            i += 1
            j += 1
    # Add the last numbers (if there is any) to the curNumsSum once any of the pointers reach the end (while loop ends)
    curNums1Sum += sum(arr1[i:])
    curNums2Sum += sum(arr2[j:])

    return max(curNums1Sum, curNums2Sum) % (10**9 + 7)

arr1 = [2, 4, 5, 8, 10]
arr2 = [4, 6, 8, 9]
maxSum(arr1, arr2)
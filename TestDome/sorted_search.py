def count_numbers(sorted_list, less_than):
    # If there is no elements in the list, return 0
    if len(sorted_list) == 0:
        return 0
    # Create variable totalCount, which is the length of the sorted_list
    totalCount = len(sorted_list)
    # If the last element in the sorted_list is less than less_than, return the totalCount
    if sorted_list[totalCount - 1] < less_than:
        return totalCount
    # Create variables low, high
    low, high = 0, totalCount - 1
    # As long as low is less than high
    while low <= high:
        # First number:  0 + (3 - 0) // 2 = 1
        mid = low + (high - low) // 2
        # if the middle number is equal to the less_than, return the middle number index
        if sorted_list[mid] == less_than:
            return mid
        # If the middle number is > less_than number,
        elif sorted_list[mid] > less_than:
            # If the mid number is > 1 and the less_than > previous number of mid
            if mid >= 1 and less_than > sorted_list[mid - 1]:
                return mid
            else:
                high = mid - 1

        elif sorted_list[mid] < less_than:
            if mid < totalCount - 1 and less_than <= sorted_list[mid + 1]:
                return mid + 1
            else:
                low = mid + 1

# Notes:
# mid is the index of the middle number
# If the middle number is > less_than number, return the middle number index OR high becomes mid - 1.

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print(count_numbers(sorted_list, 4)) # should print 2

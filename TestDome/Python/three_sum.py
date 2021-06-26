# lst = [1,2,3,4]
# target = 6
# target = 9
# target = 12
# target = 7
# Return True if any 3 numbers summed up in the lst matches one of the target, else False


# diff = 0
# count = 0
# diff = target - lst[i]
# count += 1
# if diff in lst and count == 2
# return True
# Need to have a count of 2

lst = [1,2,3,4,5]
target = 12


def total3sum(numberslst,tar):
    diff = 0
    count = 0
    for i in range(len(lst)):
        if not diff:
            diff = target - lst[i]
        elif diff in lst and count >= 2:
            return True
        else:
            diff = diff - lst[i]
        count += 1
    return False
total3sum(lst,target)
return False

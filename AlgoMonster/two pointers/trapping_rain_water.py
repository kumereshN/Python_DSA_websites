def trapping_rain_water(elevations): 
    possible_trapped = 0
    total_trapped = 0
    curr_highest = -float('inf')

    for e in elevations:
        # Find the current highest elevation
        # If a new higher elevation is found, set it as curr_highest
        # Add all of the elevations found so far (possible_trapped) to total_trapped
        if e >= curr_highest:
            curr_highest = e
            total_trapped += possible_trapped
        else:
            possible_trapped += curr_highest - e
    return total_trapped

def trapping_rain_water(elevations):
    l = 0
    r = len(elevations)-1
    maxl, maxr = 0, 0
    trapped_water = 0

    while l < r:
        if elevations[l] < elevations[r]:
            maxl = max(maxl, elevations[l])
            trapped_water += maxl - elevations[l]
            l += 1
        else:
            maxr = max(maxr, elevations[r])
            trapped_water += maxr - elevations[r]
            r -= 1
    return trapped_water

elevations = [3, 2, 1, 2, 2, 3, 2]
trapping_rain_water(elevations)
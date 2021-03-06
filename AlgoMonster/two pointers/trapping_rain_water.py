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
        # The smaller of the elevations between left and right has to be found
        # This is used to subtract the highest elevation of their respective side E.g: Highest elevation - Lowest elevation = trapped_water
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


from typing import List

def trapping_rain_water(elevations: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    """ My solution """
    left, right = 0, len(elevations) - 1
    trapped = 0
    boundary = 0
    
    while left < right:
        
        left_elevation = elevations[left]
        right_elevation = elevations[right]
        
        cur_boundary = max(left_elevation, right_elevation)
        boundary = max(cur_boundary, boundary)
        
        if left_elevation <= boundary:
            trapped += boundary - left_elevation
            left += 1
        
        if right_elevation <= boundary:
            trapped += boundary - right_elevation
            right -= 1 
    
    return trapped
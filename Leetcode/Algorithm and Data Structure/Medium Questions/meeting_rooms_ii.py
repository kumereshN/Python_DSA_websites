 # Very similar with what we do in real life. Whenever you want to start a meeting,
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).
 # After you finish the meeting, the room becomes available again ( available += 1 ).
 # Think about e as a pointer to the first available room. Then we do not need the 'available' variable.

def minMeetingRooms(intervals):
    e = ret = 0
    start = sorted(i[0] for i in intervals)
    end = sorted(i[1] for i in intervals)

    for s in range(len(start)):
        if start[s] < end[e]:
            ret += 1
        else:
            e += 1
    return ret
    
intervals = [[0,30],[5,10],[15,20]]
# intervals = [[7,10],[2,4]]
#intervals = [[1,5],[8,9],[8,9]]

minMeetingRooms(intervals)

# Alternative
def minMeetingRooms(intervals):
    peak, using = 0, 0
    meetings = []
    for s, e in intervals:
        meetings.append((s, 1))
        meetings.append((e, -1))
    meetings.sort()
    for _, i in meetings:
        using += i
        peak = max(using, peak)
    return peak


intervals = [[0,30],[5,10],[15,20]]
# intervals = [[7,10],[2,4]]

minMeetingRooms(intervals)

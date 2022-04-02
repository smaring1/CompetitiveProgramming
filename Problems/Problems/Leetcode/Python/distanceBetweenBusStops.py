class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockwise_dist, counter_clockwise_dist, n = 0, 0, len(distance)
        i = start
        while i != destination:
            clockwise_dist += distance[i]
            i = (i+1) % n
        
        i = destination
        while i != start:
            counter_clockwise_dist += distance[i]
            i = (i+1) % n
        
        return min(clockwise_dist, counter_clockwise_dist)
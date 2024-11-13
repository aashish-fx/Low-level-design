import math

from direction import Direction

def calc_distance(self, dir1: Direction, dir2: Direction, radius=6371):
        lat1, lon1 = dir1.get_lat(), dir1.get_long()
        lat2, lon2 = dir2.get_lat(), dir2.get_long()
        
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

        # Differences in coordinates
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        # Distance
        distance = radius * c
        return distance
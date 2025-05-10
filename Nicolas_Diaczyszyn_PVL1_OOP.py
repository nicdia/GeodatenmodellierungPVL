import math 

class Point():
    def __init__(self,x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor

    def get_euclidian_distance(self, other_x_cor, other_y_cor):
        distance_x = other_x_cor - self.x_cor
        distance_y = other_y_cor - self.y_cor
        eucl_distance = math.sqrt(distance_x**2 + distance_y**2)
        return eucl_distance

    def area(self):
        return 0

class GeographicPoint(Point):
    def __init__(self, lon, lat):
        super().__init__(lon, lat)
        self.lon = lon
        self.lat = lat

    def get_haversine_distance(self, other_lon, other_lat):
        lat1 = math.radians(self.lat)
        lon1 = math.radians(self.lon)
        lat2 = math.radians(other_lat)
        lon2 = math.radians(other_lon)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        r = 6371  
        d = r * c

        return d

print(GeographicPoint.mro())
point = Point(1,2)
eucl_distance = point.get_euclidian_distance(5,4)
print(f"this is euclidian distance {eucl_distance}")

geographic_point = GeographicPoint(55,10)
haversine_distance = geographic_point.get_haversine_distance(53,8)
print(f"this is haversine distance {haversine_distance}")
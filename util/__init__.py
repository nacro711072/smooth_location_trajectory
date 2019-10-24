from math import sin, cos, sqrt, atan2, radians


def latlon_distance_all(args):
    # approximate radius of earth in km
    distances = [latlon_distance(args[i][0], args[i][1], args[i + 1][0], args[i + 1][1]) for i in
                 range(0, len(args) - 1)]
    return distances


def latlon_distance(location1_lat, location1_lng, location2_lat, location2_lng):
    R = 6373.0

    lat1 = radians(location1_lat)
    lon1 = radians(location1_lng)
    lat2 = radians(location2_lat)
    lon2 = radians(location2_lng)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c * 1000


def calculate_ratio(points):
    return [latlon_distance(points[i][0],
                            points[i][1],
                            points[i + 1][0],
                            points[i + 1][1])
            for i in range(-1, len(points) - 1)]

# if __name__ == "__main__":
#     points = [(1, 1), (2, 2), (3, 3), (4, 4)]
#     for i in range(-1, len(points) - 1):
#         print(points[i], points[i + 1])

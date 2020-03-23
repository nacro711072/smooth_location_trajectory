from math import sin, cos, sqrt, atan2, radians, acos


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


def radian(x):
    """
    inner product a * b = |a| * |b| * cos(x)
    """
    a = [x[1][0] - x[0][0], x[1][1] - x[0][1]]
    b = [x[1][0] - x[2][0], x[1][1] - x[2][1]]
    abs_ab = ((a[0] ** 2 + a[1] ** 2) * (b[0] ** 2 + b[1] ** 2)) ** 0.5
    if abs_ab == 0:
        return 0
    ab = a[0] * b[0] + a[1] * b[1]
    ratio = ab / abs_ab
    if ratio > 1.0:
        return acos(1)
    elif ratio < -1.0:
        return acos(-1)
    return acos(ab / abs_ab)


if __name__ == "__main__":
    points = [(25.122605, 121.46332166666700), (25.137005, 121.49951666666700)]
    diff_t = (1572550444622 - 1572550324623) / 1000 / 60 / 60
    print(diff_t)
    speed = latlon_distance(25.122605, 121.46332166666700, 25.137005, 121.49951666666700) / 1000 / diff_t
    print(speed)

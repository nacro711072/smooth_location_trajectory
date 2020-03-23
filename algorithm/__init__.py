import util
import math


def min_distance(data_list, max_d=30.0):
    pre = data_list[0]
    new_points = [pre]
    for i in range(1, len(data_list)):
        curr = data_list[i]
        distance = util.latlon_distance(pre[0], pre[1], curr[0], curr[1])
        if distance < max_d:
            continue
        else:
            new_points.append(curr)
            pre = curr
    return new_points


def distance_and_triangle(data_list, max_dis=30.0, max_angle=30.0):
    new_points = [data_list[0]]
    buffer1 = data_list[0]
    buffer2 = [data_list[0]]
    for i in range(1, len(data_list)):
        target = data_list[i]
        distance = util.latlon_distance(buffer1[0], buffer1[1], target[0], target[1])
        if distance < max_dis:
            continue
        buffer1 = target
        buffer2.append(target)
        if len(buffer2) < 3:
            continue
        elif len(buffer2) > 3:
            raise Exception("len(buffer2) > 3 !!!")
        angle = util.radian(buffer2) * 180 / math.pi
        if angle < max_angle:
            buffer2 = buffer2[1:]
            continue
        new_points.append(buffer2[1])
        buffer2 = buffer2[1:]
    new_points.append(data_list[-1])
    return new_points


if __name__ == "__main__":
    test1 = [(0, 0), (0, 0), (0.0000001, 0.0000001), (1, 1), (2, 2)]
    assert (distance_and_triangle(test1) == [(0, 0), (1, 1), (2, 2)])

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


class Ration:
    def __init__(self, data_list, size=3, max_ratio=1.2):
        self.max_ratio = max_ratio
        new_points = [data_list[0]]
        buffer = data_list[:size]
        for i in range(1, len(data_list) - (size - 2)):
            ratio = util.calculate_ratio(buffer)
            if self.__any_ratio_too_big(ratio):
                next_end_index = i + size + (size - 2)
                if next_end_index < len(data_list):
                    buffer = [buffer[0], buffer[-1]] + [data_list[i + size + j] for j in range(size - 2)]
                else:
                    buffer = [buffer[0], buffer[-1]]
            else:
                new_points.append(data_list[i])
                buffer = data_list[i: i + size]
        new_points.extend(buffer)
        self.new_points = new_points

    def __any_ratio_too_big(self, ratio):
        if ratio[0] == 0.0:
            return True
        for r in ratio[1:]:
            if r / ratio[0] > self.max_ratio:
                return True
        return False


def radian_method(data_list, max_angle=30):
    size = 3
    new_points = [data_list[0]]
    buffer = data_list[:size]
    for i in range(1, len(data_list) - 1):
        angle = util.radian(buffer) * 180 / math.pi
        if angle < max_angle:
            next_end_index = i + size
            if next_end_index < len(data_list):
                buffer = [buffer[0], buffer[-1], data_list[i + size]]
            else:
                buffer = [buffer[0], buffer[-1]]
        else:
            new_points.append(data_list[i])
            buffer = data_list[i: i + size]
    new_points.extend(buffer)
    return new_points


def method1(data_list, max_dis=30.0, max_angle=30.0):
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
    assert (method1(test1) == [(0, 0), (1, 1), (2, 2)])

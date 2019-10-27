import util


class MinDistance:
    def __init__(self, data_list):
        pre = data_list[0]
        new_points = [pre]
        for i in range(1, len(data_list)):
            curr = data_list[i]
            distance = util.latlon_distance(pre[0], pre[1], curr[0], curr[1])
            if distance < 30.0:
                continue
            else:
                new_points.append(curr)
                pre = curr
        self.new_points = new_points


class Ration:
    def __init__(self, data_list, size=3):
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
        for r in ratio[1:]:
            if ratio[0] == 0.0:
                return True
            if r / ratio[0] > 1.2:
                return True
        return False

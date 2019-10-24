import csv
import os
import webbrowser

import gmplot

# User define
import algorithm

if __name__ == "__main__":

    with open('../data/258479.csv') as csv_file:
        rows = csv.reader(csv_file)
        data_latlng = [(float(x), float(y)) for time, x, y, b in rows]

    lats, lngs = zip(*data_latlng)

    # distances = util.latlon_distance_all(data_latlng)
    # print(distances)
    new_points1 = algorithm.MinDistance(data_latlng).new_points
    # print(new_points[1:3])
    # util.calculate_ratio(new_points[:4])
    new_points2 = algorithm.Ration(new_points1, 4).new_points

    print("ori: {}, new: {}".format(data_latlng.__len__(), new_points1.__len__()))
    print("ori: {}, new: {}".format(data_latlng.__len__(), new_points2.__len__()))

    new_lat1, new_lng1 = zip(*new_points1)
    new_lat2, new_lng2 = zip(*new_points2)
    url_path = os.path.expanduser("~/Desktop/new_258479.html")
    gmap = gmplot.GoogleMapPlotter(lats[0], lngs[0], 17)
    gmap.plot(lats, lngs, 'red')
    gmap.plot(new_lat1, new_lng1, 'blue')
    gmap.plot(new_lat2, new_lng2, 'y')
    # gmap.plot(new_lat[1:3], new_lng[1:3], 'red')

    gmap.draw(url_path)
    webbrowser.open("file://{}".format(url_path))

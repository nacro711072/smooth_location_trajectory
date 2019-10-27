import csv
import os
import webbrowser

import gmplot

# User define
import algorithm

if __name__ == "__main__":

    target_name = "260022"
    with open('../data/good/{}.csv'.format(target_name)) as csv_file:
        rows = csv.reader(csv_file)
        data_latlng = [(float(x[1]), float(x[2])) for x in rows]

    lats, lngs = zip(*data_latlng)

    # distances = util.latlon_distance_all(data_latlng)
    # print(distances)
    new_points1 = algorithm.MinDistance(data_latlng).new_points
    # print(new_points[1:3])
    # util.calculate_ratio(new_points[:4])
    new_points2 = algorithm.Ration(new_points1, 4).new_points
    new_points3 = algorithm.Ration(new_points2, 3).new_points

    print("ori: {}, new: {}".format(data_latlng.__len__(), new_points2.__len__()))
    print("ori: {}, new: {}".format(data_latlng.__len__(), new_points3.__len__()))

    new_lat2, new_lng2 = zip(*new_points2)
    new_lat3, new_lng3 = zip(*new_points3)
    url_path = os.path.expanduser("~/Desktop/new_{}.html".format(target_name))
    gmap = gmplot.GoogleMapPlotter(lats[0], lngs[0], 16)
    gmap.plot(lats, lngs, 'red')
    # gmap.plot(new_lat2, new_lng2, 'blue')
    gmap.plot(new_lat3, new_lng3, 'y')
    # gmap.plot(new_lat[1:3], new_lng[1:3], 'red')

    gmap.draw(url_path)
    webbrowser.open("file://{}".format(url_path))

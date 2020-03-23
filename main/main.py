import csv
import os
import webbrowser

import gmplot

# User define
import algorithm
import util

if __name__ == "__main__":

    target_name = "361520"
    with open('../data/bad/{}.csv'.format(target_name)) as csv_file:
        rows = csv.reader(csv_file)
        data_latlng = [(float(x[1]), float(x[2])) for x in rows]

    lats, lngs = zip(*data_latlng)

    new_points = algorithm.distance_and_triangle(data_latlng)
    ori_tot_dis = sum(util.latlon_distance_all(data_latlng))
    new_tot_dis = sum(util.latlon_distance_all(new_points))

    print("ori_points: {}, new_points: {}".format(data_latlng.__len__(), data_latlng.__len__()))
    print("ori_distance: {}, new_distance: {}".format(ori_tot_dis, new_tot_dis))

    new_lat, new_lng = zip(*new_points)
    gmap = gmplot.GoogleMapPlotter(lats[0], lngs[0], 16)
    gmap.plot(lats, lngs, 'red')
    gmap.plot(new_lat, new_lng, 'y')

    url_path = os.path.expanduser("~/Desktop/new_{}.html".format(target_name))
    gmap.draw(url_path)
    webbrowser.open("file://{}".format(url_path))

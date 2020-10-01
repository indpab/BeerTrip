import pandas as pd
import time
import tsp
from distance_matrix import DistanceMatrix
import os
import sys, getopt
import argparse

distance_lim = 2000
urls = {'Beers': 'https://raw.githubusercontent.com/brewdega/open-beer-database-dumps/master/dumps/beers.csv',
        'Breweries': 'https://raw.githubusercontent.com/brewdega/open-beer-database-dumps/master/dumps/breweries.csv',
        'Categories': 'https://raw.githubusercontent.com/brewdega/open-beer-database-dumps/master/dumps/categories.csv',
        'Geocodes': 'https://raw.githubusercontent.com/brewdega/open-beer-database-dumps/master/dumps/geocodes.csv',
        'Styles': 'https://raw.githubusercontent.com/brewdega/open-beer-database-dumps/master/dumps/styles.csv'}

files = {'Beers': 'Data/Beers.csv',
         'Breweries': 'Data/Breweries.csv',
         'Categories': 'Data/Categories.csv',
         'Geocodes': 'Data/Geocodes.csv',
         'Styles': 'Data/Styles.csv'}


def get_df(name):
    url = urls[name]
    df = pd.read_csv(url, error_bad_lines=False)
    return df


def get_local_df(name):
    file = files[name]
    df = pd.read_csv(file, error_bad_lines=False)
    return df


def main(argv):
    latitude = ''
    longitude = ''
    try:
        opts, args = getopt.getopt(argv, "hla:lo:", ["lat=", "lon="])
    except getopt.GetoptError:
        print('annotation.py -lat <latitude> -lon <longitude>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -lat <latitude> -lon <longitude>')
            sys.exit()
        elif opt in ("-lat", "--lat"):
            latitude = arg
        elif opt in ("-lon", "--lon"):
            longitude = arg
    print('Latitude is "', latitude)
    print('Longitude is "', longitude)

    return float(latitude), float(longitude)


def process_coordinates(lat, lon, dfs):
    new_row = pd.DataFrame({'latitude': lat, 'longitude': lon}, index=[0])
    dfs['Geocodes'] = pd.concat([new_row, dfs['Geocodes']]).reset_index(drop=True)
    return dfs


def get_data(lat, lon):
    dfs = {}
    for key in urls:
        dfs.update({key: get_local_df(key)})
    dfs = process_coordinates(lat, lon, dfs)
    return dfs


def update_distance_matrix(lat, lon):
    matrix = DistanceMatrix(os.path.dirname(os.path.abspath(__file__)))
    matrix.update_csv(lat, lon, os.path.dirname(os.path.abspath(__file__)))


def calculate_route(dfs):
    route, cost = tsp.min_distance_search(dfs['Geocodes'].shape[0])
    # route,cost = tsp.two_opt(10)
    return route, cost


def collect_beer(route, dfs):
    collected, breweries = tsp.collect_beer(route, dfs['Beers'], dfs['Geocodes'], dfs['Breweries'])
    return collected, breweries


def print_results(beers, breweries, route, cost):
    print("Found {} breweries:".format(len(breweries)))
    for brewery in breweries:
        print("{:4} {:55} : {:10f} , {:10f}, {:4d} km".format(brewery[0][1], brewery[0][0], brewery[1], brewery[2],
                                                              brewery[3]))

    print("Total distance travelled: {} km".format(cost))

    print("Collected {} types of beer:".format(len(beers)))
    for index, beer in enumerate(beers):
        print("{:2d}: {:30}".format(index, beer))


def execute(lat, lon):
    upd_start = time.time()
    print("Updating distance matrix...")
    update_distance_matrix(lat, lon)
    upd_finish = time.time()
    upd_time = upd_finish - upd_start
    print("Matrix update lasted: {:.2f} sec".format(upd_time))
    print("Planning route:")

    dfs = get_data(lat, lon)
    route, cost = calculate_route(dfs)
    print("Route planned. Collecting beer...")
    collected, breweries = collect_beer(route, dfs)
    print_results(collected, breweries, route, cost)
    sol_finish = time.time()
    print("Solution time: {:.2f} sec".format(sol_finish - upd_finish))
    print("Total time: {:.2f} sec".format(sol_finish - upd_start))


if __name__ == "__main__":
    lat = 0.
    lon = 0.
    parser = argparse.ArgumentParser()
    parser.add_argument('-lat', type=float)
    parser.add_argument('-lon', type=float)
    args = parser.parse_args()
    if args.lat is not None:
        lat = args.lat
        if args.lon is not None:
            lon = args.lon

    else:
        lat = 51.742503
        lon = 19.432956
    print('Latitude: ', lat)
    print('Longitude:', lon)
    execute(lat, lon)

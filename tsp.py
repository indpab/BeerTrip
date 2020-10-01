import numpy as np
from distance_matrix import DistanceMatrix
import random
import pandas as pd
import os

matrix = DistanceMatrix(os.path.dirname(os.path.abspath(__file__)))
limit = 2000


def __initialize__(size):
    random_list = random.sample(range(1, 1305), size)
    route = np.array([0] + random_list + [0])
    return route


def __initialize_empty__(size):
    route = np.zeros((size, 2))
    return route


def evaluate_distance():
    pass


def min_distance_search(size):
    # initialize values
    route = __initialize_empty__(size)  # route contains vertex id and distance to it from previous vertex
    cost = 0  # total distance
    vertex = 0  # current vertex
    read = {}  # read lines from distance matrix file (minimizes reading from file)
    i = 0  # vertices visited count
    visited = [0]  # visited vertices
    # while total distance less than limit and not all breweries visited
    while cost <= limit and i < size - 1:
        distances = matrix.get_row(i)  # get distances to other vertices from the current one
        read.update({i: distances})
        distances[distances < 0.02] = limit  # avoiding getting to the same location because of errors in data
        distances[visited] += limit  # avoiding coming back to visited breweries
        min_index = np.argmin(distances)  # nearest vertex index
        new_route = np.copy(route)
        new_route[vertex + 1][0] = int(min_index)  # adding the nearest vertex to the route
        this_cost = distances[min_index]
        new_route[vertex + 1][1] = this_cost
        this_cost2 = matrix.get_distance2(min_index, 0, read)
        new_cost = cost + this_cost + this_cost2
        visited.append(min_index)
        if new_cost <= limit:
            route = new_route
            cost = new_cost - this_cost2
            i = min_index
            vertex += 1
            print("Total distance travelled {:.2f} km".format(cost))
        else:
            break

    route = route[:vertex + 2][:]
    to_home = matrix.get_distance(route[vertex][0], 0)
    cost += to_home
    route[vertex + 1][1] = to_home
    "Total distance travelled {:4f} km".format(cost)
    return route.astype(int), cost


def collect_beer(route, beers: pd.DataFrame, geocodes: pd.DataFrame, breweries: pd.DataFrame):
    beers_collected = []
    breweries_collected = []

    for vertex, distance in route:
        brewery_coord = geocodes.iloc[vertex]
        brewery = brewery_coord['brewery_id']
        if vertex != 0:
            brewery_info = breweries.loc[breweries['id'] == brewery]
            breweries_collected.append((list(brewery_info['name'].array) + list(brewery_info['id'].array),
                                        brewery_coord['latitude'], brewery_coord['longitude'], distance))
            beer = beers.loc[beers['brewery_id'] == brewery]
            beer = list(beer['name'].array)
            beers_collected.append(beer)
        else:
            breweries_collected.append([['HOME', 0], brewery_coord['latitude'], brewery_coord['longitude'], distance])

    beers_collected = [item for sublist in beers_collected for item in sublist]
    beers_collected = np.unique(np.array([beers_collected]))
    return beers_collected, breweries_collected

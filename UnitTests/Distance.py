import unittest
import haversine
from distance_matrix import DistanceMatrix
import pandas as pd
import os
import tsp
import numpy as np


class TestDistanceCalculation(unittest.TestCase):
    def test_haversine(self):
        value = haversine.haversine(20.600300, 49.962200, 19.174200, 49.662201)
        self.assertLessEqual(abs(107.6 - value), 0.03)

    def test_distance_matrix(self):
        df = pd.read_csv(os.path.join(os.path.abspath(".."), r"Data\Geocodes.csv"), error_bad_lines=False)
        df = df.drop(columns=['id', 'brewery_id', 'accuracy'])
        df = df.head(30)
        matrix_instance = DistanceMatrix(os.path.dirname(os.path.abspath(".")))
        matrix = matrix_instance.test_disttance_matrix(30)
        for row_idx, row in enumerate(matrix):
            for val_idx, value in enumerate(row):
                actual_val = haversine.haversine(df.iloc[row_idx]['longitude'], df.iloc[row_idx]['latitude'],
                                                 df.iloc[val_idx]['longitude'], df.iloc[val_idx]['latitude'])
                self.assertEqual(value, actual_val)

    def test_route_steps_distance(self):
        matrix_instance = DistanceMatrix(os.path.dirname(os.path.abspath(".")))
        df = pd.read_csv(os.path.join(os.path.abspath(".."), r"Data\Geocodes.csv"), error_bad_lines=False)

        new_row = pd.DataFrame({'latitude': 51.742503, 'longitude': 19.432956}, index=[0])
        df = pd.concat([new_row, df]).reset_index(drop=True)
        matrix = matrix_instance.calculate_distance_matrix(df)
        self.assertEqual(matrix.shape[0], df.shape[0])
        route, cost = tsp.min_distance_search(df.shape[0])

        df_brews = pd.read_csv(os.path.join(os.path.abspath(".."), r"Data\Breweries.csv"), error_bad_lines=False)
        df_beers = pd.read_csv(os.path.join(os.path.abspath(".."), r"Data\Beers.csv"), error_bad_lines=False)
        collected, breweries = tsp.collect_beer(route, df_beers, df, df_brews)
        self.assertEqual(len(breweries), len(route))
        for index, brewery in enumerate(breweries):
            if index != 0:
                self.assertLessEqual(abs(brewery[3] - np.round(matrix[route[index - 1], route[index]], 0)[0]), 1)


if __name__ == '__main__':
    unittest.main()

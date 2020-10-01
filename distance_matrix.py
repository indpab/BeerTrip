import itertools
import pandas as pd
import haversine
import numpy as np
import csv
import os


class DistanceMatrix:
    def __init__(self, dir):
        self.dir = dir
        self.file = os.path.join(self.dir, r"distance_matrix2.csv")
        self.delimiter = ","

    def test_disttance_matrix(self, size):
        df = pd.read_csv(os.path.join(self.dir, r"Data\Geocodes.csv"), error_bad_lines=False)
        df = df.drop(columns=['id', 'brewery_id', 'accuracy'])
        df = df.head(size)
        return self.calculate_distance_matrix(df)

    def calculate_distance_matrix(self, df):

        matrix = np.zeros((df.shape[0], df.shape[0]))

        for (index1, pt1), (index2, pt2) in itertools.product(df.iterrows(), df.iterrows()):
            if index1 != index2:
                distance = haversine.haversine(pt1['longitude'], pt1['latitude'], pt2['longitude'], pt2['latitude'])
                matrix[index1, index2] = distance
                matrix[index2, index1] = distance
        return matrix

    def to_csv(self, lat, lon):
        df = pd.read_csv(os.path.join(self.dir, r"Data\Geocodes.csv"), error_bad_lines=False)
        df = df.drop(columns=['id', 'brewery_id', 'accuracy'])
        new_row = pd.DataFrame({'latitude': lat, 'longitude': lon}, index=[0])
        df = pd.concat([new_row, df]).reset_index(drop=True)
        matrix = self.calculate_distance_matrix(df)
        np.savetxt(self.file, matrix, delimiter=self.delimiter)

    def update_csv(self, lat, lon, work_dir):
        df = pd.read_csv(os.path.join(work_dir, "Data\Geocodes.csv"), error_bad_lines=False)
        df = df.drop(columns=['id', 'brewery_id', 'accuracy'])
        new_row = pd.DataFrame({'latitude': lat, 'longitude': lon}, index=[0])
        df = pd.concat([new_row, df]).reset_index(drop=True)
        row = np.zeros(df.shape[0])
        for index, pt in df.iterrows():
            if index != 0:
                distance = haversine.haversine(lon, lat, pt['longitude'], pt['latitude'])
                row[index] = distance

        with open('temp.csv', 'w', newline='') as temp:
            writer = csv.writer(temp, delimiter=',')
            first = True
            with open(self.file, 'r') as read:
                reader = csv.reader(read, delimiter=',')
                i = 0
                for line_list in reader:
                    if first:
                        line_list = row
                        first = False
                    else:
                        line_list[0] = row[i]
                    if i > 1300:
                        pass
                    i += 1

                    writer.writerow(line_list)

        os.remove(self.file)
        os.rename('temp.csv', "distance_matrix2.csv")

    def get_row(self, row_index):
        with open(self.file, 'r') as f:
            row = np.array(next(itertools.islice(csv.reader(f), int(row_index), None))).astype(float)
        f.close()
        return row

    def get_distance(self, row, column):
        with open(self.file, 'r') as f:
            return float(next(itertools.islice(csv.reader(f), int(column), None))[int(row)])

    def get_distance2(self, row, column, read_lines):
        try:
            distance = read_lines[row][column]
            return distance
        except KeyError:
            return self.get_distance(row, column)

        # with open(self.file, 'r') as f:
        #     return float(next(itertools.islice(csv.reader(f), int(column), None))[int(row)])

    def load_partial_matrix(self, route):
        matrix_rows = {}
        for vertex in route:
            matrix_rows.update({vertex: self.get_row(vertex)})
        return matrix_rows

    def cost(self, route, partial_matrix):
        sum = 0
        for pt1, pt2 in itertools.product(route, route):
            if pt1 != pt2:
                sum += partial_matrix[pt1][pt2]
        return sum

    def cost2(self, route, last_index):
        sum = 0
        for pt1, pt2 in itertools.product(route[:last_index], route[:last_index]):
            if pt1 != pt2:
                sum += self.get_distance(pt1, pt2)

        return sum


if __name__ == '__main__':
    matrix = DistanceMatrix()
    matrix.to_csv()

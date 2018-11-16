import math
import sys

import Cluster
import random


def chooseStartingClusterCenters(data_set):
    class_indexes = []

    current_class = data_set[0].get_class()
    i = 0
    for data in data_set:
        if data.get_class() != current_class:
            class_indexes.append(i)
            current_class = data.get_class()
        i += 1

    cluster_list = []

    cluster_index = random.randint(1, class_indexes[0])
    cluster_list.append(Cluster.ClusterCenter(data_set[cluster_index].get_x(), data_set[cluster_index].get_y(),
                                              data_set[cluster_index].get_z()))

    cluster_index = random.randint(class_indexes[0], class_indexes[1])
    cluster_list.append(Cluster.ClusterCenter(data_set[cluster_index].get_x(), data_set[cluster_index].get_y(),
                                              data_set[cluster_index].get_z()))

    cluster_index = random.randint(class_indexes[1], len(data_set) + 1)
    cluster_list.append(Cluster.ClusterCenter(data_set[cluster_index].get_x(), data_set[cluster_index].get_y(),
                                              data_set[cluster_index].get_z()))

    print("choose starting clusters")

    return newClusterForming(cluster_list, data_set)


def newClusterForming(clusters, data_set):
    for data in data_set:
        found = 0
        for cluster in clusters:
            if cluster.cluster_center_x == data.get_x() and cluster.cluster_center_y == data.get_y() \
                    and cluster.cluster_center_z == data.get_z():
                found = 1
        if found == 0:
            distance_to_closest = sys.maxsize
            closest_index = -1
            i = 0
            for cluster in clusters:
                euclidean_distance = math.sqrt(math.pow(float(data.get_x()) - float(cluster.get_x()), 2) +
                                                math.pow(float(data.get_y()) - float(cluster.get_y()), 2) +
                                                math.pow(float(data.get_z()) - float(cluster.get_z()), 2))
                if euclidean_distance < distance_to_closest:
                    distance_to_closest = euclidean_distance
                    closest_index = i
            clusters[closest_index].add_to_list(data)

    return newRefactorClusters(clusters)


def newRefactorClusters(clusters):
    new_clusters = []
    for cluster in clusters:
        num_of_data_points = 1
        x_total = float(cluster.get_x())
        y_total = float(cluster.get_y())
        z_total = float(cluster.get_z())

        for data_point in cluster.get_list():
            x_total += float(data_point.get_x())
            y_total += float(data_point.get_y())
            z_total += float(data_point.get_z())
            num_of_data_points += 1

        x_average = x_total / num_of_data_points
        y_average = y_total / num_of_data_points
        z_average = z_total / num_of_data_points
        new_clusters.append(Cluster.ClusterCenter(x_average, y_average, z_average))

    num_of_changes = 0
    for i in range(3):
        for data_point in clusters[i].get_list():
            closest_cluster = 0
            closest_distance = sys.maxsize
            for j in range(3):
                euclidean_distance = math.sqrt(math.pow(float(data_point.get_x()) - new_clusters[j].get_x(), 2) +
                                               math.pow(float(data_point.get_y()) - new_clusters[j].get_y(), 2) +
                                               math.pow(float(data_point.get_z()) - new_clusters[j].get_z(), 2))

                if euclidean_distance < closest_distance:
                    closest_distance = euclidean_distance
                    closest_cluster = j
            new_clusters[closest_cluster].add_to_list(data_point)
            if i != closest_cluster:
                num_of_changes += 1

    if num_of_changes >= 3:
        return newRefactorClusters(new_clusters)
    else:
        return new_clusters

def randomlySelectClusters(data_set, user_input):
    # change it so one of each class is the cluster
    cluster_centers = []
    min_index = 1
    max_index = 0
    for i in range(3):
        if i == 0:
            max_index = 50
        elif i == 1:
            min_index = 51
            max_index = 100
        elif i == 2:
            min_index = 101
            max_index = 150

        cluster_index = random.randint(min_index, max_index + 1)
        new_cluster = Cluster.ClusterCenter(data_set[cluster_index].Data[user_input[0] - 1],
                                            data_set[cluster_index].Data[user_input[1] - 1],
                                            data_set[cluster_index].Data[user_input[2] - 1])
        cluster_centers.append(new_cluster)

    print("Created 3 clusters")
    return cluster_centers


def formClusters(clusters, data_set, user_input):
    found = 0
    non_cluster_data = []
    for data in data_set:
        found = 0
        for cluster in clusters:
            if cluster.cluster_center_x == data.Data[user_input[0]] \
                    and cluster.cluster_center_y == data.Data[user_input[1]] \
                    and cluster.cluster_center_z == data.Data[user_input[2]]:
                found = 1
        if found == 0:
            non_cluster_data.append(data)
        # check if the cluster is the current data if so ignore
        # if not check which of the clusters is the closest

    for data in non_cluster_data:
        distance_to_closest = sys.maxsize
        closest_index = -1
        user_input_1 = (user_input[0] - 1)
        user_input_2 = (user_input[1] - 1)
        user_input_3 = (user_input[2] - 1)
        for i in range(3):
            distance_to_cluster = math.sqrt(
                math.pow((float(data.Data[user_input_1]) - float(clusters[i].cluster_center_x)), 2) +
                math.pow((float(data.Data[user_input_2]) - float(clusters[i].cluster_center_y)), 2) +
                math.pow((float(data.Data[user_input_3]) - float(clusters[i].cluster_center_z)), 2))
            if distance_to_cluster < distance_to_closest:
                distance_to_closest = distance_to_cluster
                closest_index = i
        clusters[closest_index].add_to_list(data)

    length_1 = len(clusters[0].list_of_points)
    length_2 = len(clusters[1].list_of_points)
    length_3 = len(clusters[2].list_of_points)
    print("cluster 1 length: ", length_1, ", cluster 2 length: ", length_2,
          ", cluster 3 length: ", length_3, ", total length", (length_1 + length_2 + length_3))

    return clusters


def recalculateClusters(clusters, user_input):
    new_clusters = []
    for cluster in clusters:
        num_of_data_points = 1
        x_total = float(cluster.get_x())
        y_total = float(cluster.get_y())
        z_total = float(cluster.get_z())

        for data_point in cluster.get_list():
            x_total += float(data_point.Data[user_input[0] - 1])
            y_total += float(data_point.Data[user_input[1] - 1])
            z_total += float(data_point.Data[user_input[2] - 1])
            num_of_data_points += 1

        x_average = (x_total / num_of_data_points)
        y_average = (y_total / num_of_data_points)
        z_average = (z_total / num_of_data_points)
        new_cluster = Cluster.ClusterCenter(x_average, y_average, z_average)
        new_clusters.append(new_cluster)

    num_of_changes = 0
    for i in range(3):
        for data_point in clusters[i].get_list():
            closest_cluster = 0
            closest_distance = sys.maxsize
            for j in range(3):
                distance_to_new_cluster = math.sqrt(
                    math.pow((float(data_point.Data[user_input[0] - 1]) - float(new_clusters[j].cluster_center_x)), 2) +
                    math.pow((float(data_point.Data[user_input[1] - 1]) - float(new_clusters[j].cluster_center_y)), 2) +
                    math.pow((float(data_point.Data[user_input[2] - 1]) - float(new_clusters[j].cluster_center_z)), 2))

                if distance_to_new_cluster < closest_distance:
                    closest_distance = distance_to_new_cluster
                    closest_cluster = j
            new_clusters[closest_cluster].add_to_list(data_point)
            if i != closest_cluster:
                num_of_changes += 1

    if num_of_changes >= 3:
        print("recursion: ")
        return recalculateClusters(new_clusters, user_input)
    else:
        print("finished")
        return new_clusters

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as ply


def newDrawGraph(data_set, labels):
    data_length = data_set[0].get_size()
    if data_length == 1:
        one_dimension_graph = 1
    elif data_length == 2:
        two_dimension_graph = 2
    elif data_length == 3:
        three_dimesnsion_graph = 3
        _newPlot3DGraph(data_set, labels)


def _newPlot3DGraph(data_set, labels):
    fig = ply.figure()
    ax = fig.add_subplot(111, projection='3d')

    for data in data_set:
        data_class = data.get_class()
        x = float(data.get_x())
        y = float(data.get_y())
        z = float(data.get_z())

        color = 'r'
        if 'Iris-versicolor' in data_class:
            color = 'g'
        elif 'Iris-virginica' in data_class:
            color = 'b'

        ax.scatter(x, y, z, c=color, marker='o')

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])

    ply.show()


def newPlot3DClustering(clusters, labels):
    fig = ply.figure()
    ax = fig.add_subplot(111, projection='3d')
    i = 0

    for cluster in clusters:
        color = 'r'
        if i == 1:
            color = 'g'
        elif i == 2:
            color = 'b'
        i += 1
        ax.scatter(float(cluster.get_original_x()), float(cluster.get_original_y()), float(cluster.get_original_z()),
                   c=color, marker='o')
        for data in cluster.get_list():
            x = float(data.get_x())
            y = float(data.get_y())
            z = float(data.get_z())
            ax.scatter(x, y, z, c=color, marker='o')

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])

    ply.show()


def _plot2DGraph(user_input, data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.Data[user_input[0] - 1]))
        # y.append(0)
        y.append(float(data.Data[user_input[1] - 1]))
        if 'Iris-setosa' in data.Data[4]:
            c.append('r')
        elif 'Iris-versicolor' in data.Data[4]:
            c.append('g')
        elif 'Iris-virginica' in data.Data[4]:
            c.append('b')

    ply.scatter(x, y, 3, c)
    ply.xlabel(labels[user_input[0] - 1])
    ply.ylabel(labels[user_input[1] - 1])
    ply.show()


def _plat1DGraph(user_input, data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.Data[user_input[0] - 1]))
        y.append(0)
        if 'Iris-setosa' in data.Data[4]:
            c.append('r')
        elif 'Iris-versicolor' in data.Data[4]:
            c.append('g')
        elif 'Iris-virginica' in data.Data[4]:
            c.append('b')

    ply.scatter(x, y, 3, c)
    ply.xlabel(labels[user_input[0] - 1])
    ply.show()

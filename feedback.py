from math import floor, sqrt

import operator

import numpy as np
from scipy.spatial import distance

import matplotlib.path as mplPath

from sklearn.decomposition import PCA

from data_import import json_import

from data_processing import (run_clustering,
                             data_gathering)

from data_visualization import (plot_PCA,
                                multi_plot_PCA)

def import_data(path, import_find):
    original_data = []

    # Gathering the data
    # If it's a list, then we have to import multiple people's data
    if isinstance(import_find[0], list):
        for to_import in import_find[0]:
            original_data.extend(json_import(path, to_import))
    # Else, it's just a name, so we import their data
    else:
        original_data = json_import(path, import_find)

    if not original_data:
        print('ERROR: no data found (check your names).')
        return

    return original_data

def feedback():
    path = r'C:/Users/quentin/Documents/Programmation/C++/MLA/Data/alldartsdescriptors/mixed'
    # Expert Data
    name = 'aurel'
    expert_data = import_data(path, name)
    # Student data
    name = 'me'
    student_data = import_data(path, name)

    # Setting the laterality
    for motion in expert_data:
        motion.laterality = 'Right'

    for motion in student_data:
        motion.laterality = 'Left'

    # List of datatypes and joint to process
    # default to check: {Descriptor: [{joint, laterality or not (check left for lefthanded and vice versa)},
    #                                  other joint, laterality or not}],
    #                    Other descriptor: [{joint, laterality or not}]
    #                   }
    datatype_joints_list =  []

    datatype_joints_list.append(['leaning', {'MeanSpeed': [{'joint': 'LeftShoulder', 'laterality': False},
                                                           {'joint': 'RightShoulder', 'laterality': False}]
                                }])

    datatype_joints_list.append(['elbow_move', {'MeanSpeed': [{'joint': 'LeftArm', 'laterality': True},
                                                              {'joint': 'LeftShoulder', 'laterality': True}]
                                }])

    datatype_joints_list.append(['javelin', {'PosX': [{'joint': 'LeftHand', 'laterality': True},
                                                      {'joint': 'Head',     'laterality': False}],
                                             'PosY': [{'joint': 'LeftHand', 'laterality': True},
                                                      {'joint': 'Head',     'laterality': False}],
                                             'PosZ': [{'joint': 'LeftHand', 'laterality': True},
                                                      {'joint': 'Head',     'laterality': False}]
                                            }])

    datatype_joints_list.append(['align_arm', {'BoundingBoxMinusX': [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}],
                                               'BoundingBoxPlusX':  [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}],
                                               'BoundingBoxMinusY': [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}],
                                               'BoundingBoxPlusY':  [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}],
                                               'BoundingBoxMinusZ': [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}],
                                               'BoundingBoxPlusZ':  [{'joint': 'RightShoulderRightArmRightForeArmRightHand', 'laterality': True}]
                                              }])



    # Scaling and normalisaing (nor not) the data
    # Useful for DBSCAN for example
    scale = False
    normalise = False

    # Setting the data repartition
    aurelien_data = {'good': [x+1 for x in range(10)],
                     'leaning': [x+1 for x in range(10,20)],
                     'javelin': [x+1 for x in range(20,30)],
                     'align_arm': [x+1 for x in range(30,40)],
                     'elbow_move': [x+1 for x in range(40,50)]}

    # Algorithm to test
    algos = {'k-means': {'n_clusters': 2}}

    distances_and_clusters = []
    results = []
    std_features_all = []

    for problem in datatype_joints_list:
        datatype_joints = problem[1]
        expert_sub_data = expert_data[:10] + expert_data[min(aurelien_data[problem[0]])-1:max(aurelien_data[problem[0]])]

        for algo, param in algos.items():
            print(problem[0])

            model = run_clustering(path, expert_sub_data, name, validate_data=False,
                                   datatype_joints=datatype_joints, algorithm=algo,
                                   parameters=param, scale_features=scale, normalise_features=normalise,
                                   true_labels=None, verbose=False, to_file=True, to_json=True, return_data=True)


        # Taking the student features
        std_features = data_gathering(student_data, datatype_joints)

        # If the expert data has been scaled, do the same for the student's ones
        if scale:
            from sklearn.preprocessing import RobustScaler
            scaler = RobustScaler()
            std_features = scaler.fit_transform(std_features)
        # Same for normalising
        if normalise:
            from sklearn.preprocessing import MinMaxScaler
            min_max_scaler = MinMaxScaler()
            std_features = min_max_scaler.fit_transform(std_features)

        # Compute the centroid of the student's features (Euclidean distance for now)
        std_centroid = get_centroid_student(std_features)

        # For the rest of the algorithm, if there are more than 2 features,
        # we run the data through a PCA for the next steps
        if len(model[0].cluster_centers_[0]) > 2:
            pca = PCA(n_components=2, copy=True)
            pca.fit(model[2])

            model[2] = pca.transform(model[2])
            model[0].cluster_centers_ = pca.transform(model[0].cluster_centers_)
            std_centroid = pca.transform(std_centroid.reshape(1, -1))[0]
            std_features = pca.transform(std_features)

        # Compute the distance from the student's centroid to the expert's ones
        distances_to_centroid = compute_distance(model[0].cluster_centers_, std_centroid)

        # Get the distance from the student's centroid to the line between the two expert's centroids
        distance_from_line = get_distance_from_expert_centoids_line(model[0].cluster_centers_, std_centroid)
        # Used to check if the student's centroid is between the expert centroids (diamond shape)
        distance_from_line /= (dst_pts(model[0].cluster_centers_[0], model[0].cluster_centers_[1]) / 2)

        # Normalise the distances to the centroids
        summ = sum(distances_to_centroid)
        for i, distance in enumerate(distances_to_centroid):
            distances_to_centroid[i] = distance/summ

        # Get the most probable cluster label for expert data
        clusters_label = get_cluster_label(expert_sub_data, aurelien_data, model[0].labels_)
        # Display the closeness of the student's data to each expert cluster
        distances_and_clusters.append(mix(distances_to_centroid, clusters_label, distance_from_line))

        results.append((model[0], model[2], model[0].labels_, model[1], problem[0], std_features, get_trapezoid(model, std_centroid), get_circle(model, std_centroid)))
        std_features_all.append(std_features)

    models = [x[0] for x in results]
    features = [x[1] for x in results]

    for i, feat in enumerate(features):
        features[i] = np.concatenate([feat, std_features_all[i]], axis=0)

    centroids = [x[0].cluster_centers_ for x in results]
    labels = [x[2] for x in results]

    for i, lab in enumerate(labels):
        max_val = max(lab)
        labels[i] = np.concatenate([lab, [max_val+1 for x in range(len(std_features))]], axis=0)

    trapezoids= [x[6] for x in results]
    circles = [x[7] for x in results]

    sss = [x[3]['ss'] for x in results]
    names = ['k-means ' + x[4] for x in results]
    title = 'None'

    multi_plot_PCA(features, labels, names, models, sss, title, trapezoids, circles)


def compute_distance(centroids, feature):
    return [np.linalg.norm(feature - centroid) for centroid in centroids]

def dst_pts(pt1, pt2):
    return sqrt(pow(pt2[0] - pt1[0], 2) + pow(pt2[1] - pt1[1], 2))

def get_trapezoid(result, point):
    centroids = result[0].cluster_centers_
    points = [result[2][np.where(result[0].labels_ == i)] for i in np.unique(result[0].labels_)]
    max_dst = [max(max(distance.cdist([centroids[i]], cluster, 'euclidean'))) for i, cluster in enumerate(points)]

    p1 = (centroids[0][0], centroids[0][1] + max_dst[0])
    p4 = (centroids[0][0], centroids[0][1] - max_dst[0])
    p2 = (centroids[1][0], centroids[1][1] + max_dst[1])
    p3 = (centroids[1][0], centroids[1][1] - max_dst[1])

    trapezoid = mplPath.Path(np.array([p1, p2, p3, p4]))
    print(f"Point is in trapezoid: {trapezoid.contains_point(point)}")
    return trapezoid

def get_circle(result, point):
    centroids = result[0].cluster_centers_
    points = [result[2][np.where(result[0].labels_ == i)] for i in np.unique(result[0].labels_)]
    max_dst = [max(max(distance.cdist([centroids[i]], cluster, 'euclidean'))) for i, cluster in enumerate(points)]


    is_in_cluster = np.linalg.norm(centroids[0]-point) < max_dst[0]
    if not is_in_cluster:
        is_in_cluster = np.linalg.norm(centroids[1]-point) < max_dst[1]

    print(f"Point is in a cluster: {is_in_cluster}")
    return ({'center': centroids[0], 'radius':max_dst[0]}, {'center': centroids[1], 'radius':max_dst[1]})

def get_cluster_label(original_data, original_labels, clustering_labels):

    labelled_cluster = {}
    labelled_data = []
    for data in original_data:
        # Get rid of the name + the Char00
        number = int(data.name.split('_')[1][:-6])

        for k,v in original_labels.items():
            if number in v:
                number = k
                break

        labelled_data.append(number)

    c_rep = []
    for cluster in set(clustering_labels):
        c_rep.append({x: 0 for x in original_labels.keys()})
        for i, elem in enumerate(clustering_labels):
            if elem == cluster:
                c_rep[-1][labelled_data[i]] += 1


    for i, cluster in enumerate(c_rep):
        labelled_cluster[f'c{i}'] = max(cluster.items(), key=operator.itemgetter(1))[0]

    return labelled_cluster

def get_centroid_student(std_data):
    return np.mean(std_data, axis=0)

def get_distance_from_expert_centoids_line(exp_centroids, std_centroid):
    pt1 = {'x': exp_centroids[0][0], 'y': exp_centroids[0][1]}
    pt2 = {'x': exp_centroids[1][0], 'y': exp_centroids[1][1]}

    pt_std = {'x': std_centroid[0], 'y': std_centroid[1]}

    A = pt2['y'] - pt1['y']
    B = pt2['x'] - pt1['x']
    C = (pt1['x'] * pt2['y']) - (pt2['x'] * pt1['y'])

    return abs((A*pt_std['x']) + (B*pt_std['y']) + C) / sqrt(pow(A, 2) + pow(B, 2))

def mix(distances, c_labels, distance_line_vs_distance_centroids):
    new_dict = {}
    for i, (k,v) in enumerate(c_labels.items()):
        new_dict[v] = distances[i]


    keys_to_display = list(new_dict.keys())
    if keys_to_display[0] != 'good':
        keys_to_display.reverse()

    size_display = 40
    char = '#'
    place = floor((size_display/100) * (100 * new_dict['good']))

    print(f"{keys_to_display[0]} [", end='')
    for i in range(size_display):
        if i == place:
            print(char, end='')
        else:
            print('-',end='')
    print(f"] {keys_to_display[1]} ({distance_line_vs_distance_centroids:.2f})")



if __name__ == '__main__':
    feedback()
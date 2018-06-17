import numpy as np
import cv2
import os
import copy


def load_data():
    path="../data/"
    data = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            f = cv2.imread(path+filename)
            data.append(f)
    return data


def resize_data(data, width=300, height=300):
    data_resized = []
    for pict in data:
        pict_resized = cv2.resize(pict, (width, height))
        data_resized.append(pict_resized)
    data_resized = np.array(data_resized)
    return data_resized


def enrich_data(data):
    data = horizontal_sym(data)
    data = vertical_sym(data)
    #data = swap_colors(data)
    return data


def horizontal_sym(data):
    data_sym = data[:, ::-1, :, :]
    return np.concatenate((data, data_sym), axis = 0)


def vertical_sym(data):
    data_sym = data[:, :, ::-1, :]
    return np.concatenate((data, data_sym), axis = 0)


def swap_colors(data):
    data_swap1 = copy.deepcopy(data)
    data_swap1[:,:,:, 0] = data[:,:,:, 1];  data_swap1[:,:,:, 1] = data[:,:,:, 0]

    data_swap2 = copy.deepcopy(data)
    data_swap2[:,:,:, 0] = data[:,:,:, 2];  data_swap1[:,:,:, 2] = data[:,:,:, 0]

    data_swap3 = copy.deepcopy(data)
    data_swap3[:,:,:, 1] = data[:,:,:, 2];  data_swap1[:,:,:, 2] = data[:,:,:, 1]

    data = np.concatenate((data, data_swap1, data_swap2, data_swap3), axis = 0)
    return data


if __name__ == "__main__":
    data = load_data()
    data = resize_data(data)
    data = enrich_data(data)
    data = swap_colors(data)
    import pdb; pdb.set_trace()

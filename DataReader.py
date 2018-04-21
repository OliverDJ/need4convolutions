
import random
import numpy as np
import cv2
import os
from sklearn.model_selection import train_test_split


class DataReader:
    def __init__(self, source_folder, val_split=0.3, test_split=0.3,
                 random_seed=10, img_width=None, img_height=None, one_hot_vec_size=4):
        self.key_to_label_dict = {'w': 0, 's': 1, 'a': 2, 'd': 3}
        random.seed(random_seed)
        self.one_hot_vec_size = one_hot_vec_size
        all_image_paths = self.fetch_all_file_paths(source_folder)
        total_image_count = len(all_image_paths)

        draw_options = np.arange(0, total_image_count)
        train_id, val_id, test_id = self.generate_train_val_test_ids(draw_options,
                                                                     total_image_count,
                                                                     val_split,
                                                                     test_split)

        self.train_images, self.train_labels = self.generate_data_set(all_image_paths, train_id)
        self.val_images, self.val_labels = self.generate_data_set(all_image_paths, val_id)
        self.test_images, self.test_labels = self.generate_data_set(all_image_paths, test_id)

    def generate_train_val_test_ids(self, draw_options,
                                    total_image_count, val_split, test_split):
        full_train_id, test_id = self.generate_x_y_ids(draw_options, test_split)
        train_id, validation_id = self.generate_x_y_ids(full_train_id, val_split)
        return train_id, validation_id, test_id

    def generate_x_y_ids(self, draw_options, split_size_x):
        x_ids, y_ids = train_test_split(draw_options, test_size=split_size_x)
        return (x_ids, y_ids)

    def fetch_all_file_paths(self, directory):
        file_list = []
        for subdir, dirs, files in os.walk(directory):
            for file in files:
                filepath = subdir + os.sep + file
                if filepath[-4:] == '.jpg' or filepath[-4:] == '.png':
                    file_list.append(filepath)
        return file_list

    def generate_data_set(self, all_image_paths, id_list):
        img_list = []
        label_list = []
        for id in id_list:
            path_name = all_image_paths[id]
            key_list = path_name.split('-')[1].split('.')[0].split('_')
            label_list.append((self.create_one_hot_vector_from_key_list(key_list)))
            img = cv2.imread(path_name, 0)

            reshaped = img.reshape(img.shape[0], img.shape[1], 1) / 255
            #print(reshaped.shape)
            img_list.append(reshaped)
        return np.array(img_list), label_list

    def create_one_hot_vector_from_key_list(self, key_list):
        one_hot_vec = np.zeros(shape=(self.one_hot_vec_size,))
        if key_list[0] == 'none':
            return one_hot_vec
        for key in key_list:
            one_hot_vec[self.key_to_label_dict[key]] = 1
        return one_hot_vec

    def get_train_data(self):
        return self.train_images, self.train_labels

    def get_val_data(self):
        return self.val_images, self.val_labels

    def get_test_data(self):
        return self.test_images, self.test_labels

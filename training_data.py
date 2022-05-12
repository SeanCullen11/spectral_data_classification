import os
from pathlib import Path
import tensorflow as tf
import pandas as pd
import numpy as np
import random
from typing import List, Union, Tuple
from utilities.dataloader import load_file_list_from_filesystem

VALIDATION_SPLIT = 0.1  # todo: change this to 0.2?


class TrainingData:
    def __init__(self, random_seed: int):
        self.seed: int = random_seed
        random.seed(self.seed)
        self.training_data_set: List[tf.data.Dataset] = [tf.data.Dataset.from_tensor_slices([0])]
        self.validation_data_set: List[tf.data.Dataset] = [tf.data.Dataset.from_tensor_slices([0])]
        self.csv_dimensions: tuple = (0, 0)
        self.class_labels: list = []
        self.n_folds: int = 1
        self.test_data_set: tf.data.Dataset = tf.data.Dataset.from_tensor_slices([0])
        self.test_data_names: list = list()
        self.test_features: list = list()
        self.test_labels: list = list()

    def load_training_data(self, training_images_location: Union[str, Path],
                           # image_size: Union[int, Tuple[int, int]],
                           shuffle=True,
                           n_folds=1, ) -> None:
        self.csv_dimensions = (100, 100)
        self.n_folds = n_folds

        print('Fetching labels based on folder names.')
        self._load_data_based_on_directory_structure(training_images_location)

        self.training_data_set[0] = self.training_data_set[0].cache().prefetch(buffer_size=tf.data.AUTOTUNE)
        self.validation_data_set[0] = self.validation_data_set[0].cache().prefetch(buffer_size=tf.data.AUTOTUNE)

    def _load_data_based_on_directory_structure(self, training_data_location):
        path = str(training_data_location)
        self.training_data_set = [
            tf.data.experimental.CsvDataset(
                path,
                tf.float32,
                compression_type=None,
                buffer_size=None,
                header=True,
                field_delim=',',
                na_value='',
                select_cols=None,
                exclude_cols=None
            )]

        self.validation_data_set = [
            tf.data.experimental.CsvDataset(
                path,
                tf.float32,
                compression_type=None,
                buffer_size=None,
                header=True,
                field_delim=',',
                na_value='',
                select_cols=None,
                exclude_cols=None
            )]

        self.class_labels = self.training_data_set[0].class_names

        # images = os.walk(training_images_location)
        #
        # for d in images:
        #     files = [Path(f) for f in d[2]]
        #     image_files = [i for i in files if i.suffix in ['.jpeg', '.jpg', '.gif', '.png', '.bmp']]
        #     self.img_count += len(image_files)

    # def load_testing_images(self, testing_image_folder: str, image_size: int):
    #     self.csv_dimensions = (image_size, image_size)
    #     self.test_data_set = tf.keras.preprocessing.image_dataset_from_directory(testing_image_folder,
    #                                                                              # color_mode=self.color_mode.name,
    #                                                                              image_size=self.csv_dimensions,
    #                                                                              shuffle=False)
    #     self.test_data_names = self.test_data_set.file_paths
    #     self.class_labels = self.test_data_set.class_names
    #     self.test_labels = list()
    #     self.test_features = list()
    #     for feature_class_pair in self.test_data_set.as_numpy_iterator():
    #         self.test_features = self.test_features + list(feature_class_pair[0])
    #         self.test_labels = self.test_labels + list(feature_class_pair[1])

import os
import random
import numpy as np
import tensorflow as tf
import matplotlib
from training_data import TrainingData
from models.cnnstructure import CNNStructure
from models.model_training import ModelTrainer
# from utilities.timer import Timer
from models.modeltrainingarguments import ModelTrainingArguments

matplotlib.use('Agg')  # required when running on server


def main() -> None:

    cnn_arguments = ModelTrainingArguments()
    training_data = TrainingData(SEED)

    training_data.load_training_data(cnn_arguments.training_image_folder,
                                    shuffle=True, n_folds=cnn_arguments.n_folds)

    architecture = CNNStructure(SEED, cnn_arguments.lr, [], 2)
    trainer = ModelTrainer(cnn_arguments.n_epochs, cnn_arguments.n_folds, architecture, SEED)

    #change function in training__data.py
    trainer.train_and_save_all_models(training_data)


if __name__ == '__main__':
    # set up random seeds
    SEED = 1
    np.random.seed(SEED)
    tf.random.set_seed(SEED)
    random.seed(SEED)

    main()

from models import CNNModel
import tensorflow as tf
from tensorflow.python.keras import layers
from models.modeltrainingarguments import ModelTrainingArguments


class CNNStructure(CNNModel):

    def add_convolutional_layers(self):

        # Output shape: 40 x 61 x 61
        self.model.add(layers.Flatten())
        self.model.add(layers.Dropout(0.5, seed=self.seed))  # drop out 50% and then * 2 (same # of layers)

    def add_hidden_layers(self):
        self.model.add(layers.Dense(500, activation='linear'))
        self.model.add(layers.Dense(500, activation='relu'))

    def add_output_layers(self):
        cnn_arguments = ModelTrainingArguments()

        self.model.add(layers.Dense(cnn_arguments.num_output_classes, activation='linear'))
        self.model.add(layers.Dense(cnn_arguments.num_output_classes, activation=tf.keras.activations.softmax))
        self.model.add(layers.Dense(2, activation='linear'))
        self.model.add(layers.Dense(2, activation=tf.keras.activations.softmax))
        print(self.model.summary())

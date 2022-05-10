import argparse
import os
from pathlib import Path
from typing import Tuple


class ModelTrainingArguments:
    def __init__(self):
        self._parser = argparse.ArgumentParser('Create and train NNs for image classification.')
        self._args: argparse.Namespace = self.set_up_parser_arguments()
        self.training_image_folder: Path = self._validate_training_folder()
        self.dataframe_dim: Tuple[int, int] = self._validate_dataframe_dim()
        self.lr: float = self._validate_learning_rate()
        self.n_folds: int = self._validate_n_folds()
        self.n_epochs: int = self._validate_n_epochs()
        self.num_output_classes: int = self._validate_num_output_classes()

    def set_up_parser_arguments(self):

        # folder argument
        self._parser.add_argument('training_set', help='Directory containing training images.')

        # model training arguments
        self._parser.add_argument('-lr', '--learning_rate', type=float,
                                  default=0.001, help='Learning rate for training. (Default = 0.001)')
        self._parser.add_argument('-f', '--n_folds', type=int, default=1,
                                  help='Number of folds (minimum 1) for cross validation. (Default = 1)')
        self._parser.add_argument('-e', '--n_epochs', type=int, default=25,
                                  help='Number of epochs (minimum 5) per fold. (Default = 25)')
        self._parser.add_argument('-cls', '--num_output_classes', default=2, type=int,
                                  help='Class size minimum 2, no max. (Default = 2)')

        return self._parser.parse_args()

    def _validate_dataframe_dim(self) -> (int, int):
        pass

    # Stay the same
    def _validate_training_folder(self) -> Path:
        training_path = Path(self._args.training_set)
        assert os.path.isdir(training_path), f'{self._args.training_set} is not a valid directory path.'
        return training_path

    # Stay the same
    def _validate_learning_rate(self) -> float:
        lr = self._args.learning_rate
        assert 0 < lr < 1, f'Learning rate {lr:.6f} is not valid. Must be in range (0, 1).'
        return lr

    # Stay the same
    def _validate_n_folds(self) -> int:
        n_folds = self._args.n_folds
        assert n_folds <= 1, f'Number of folds {n_folds} is not valid. Value must be >= 1.'
        return n_folds

    # Stay the same
    def _validate_n_epochs(self) -> int:
        n_epochs = self._args.n_epochs
        assert n_epochs >= 5, f'{n_epochs} is not a valid number of epochs. Must be >= 5.'
        return n_epochs

    # Stay the same
    def _validate_num_output_classes(self) -> int:
        num_output_classes = self._args.num_output_classes
        assert num_output_classes >= 2, f'{num_output_classes} is not a valid number of classes. Must be >= 2.'
        return num_output_classes

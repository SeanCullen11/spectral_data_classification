# Spectral Classification Neural Network
#### _spectral_data_classification_ repository


The code in this repository uses Convolutional Neural Networks (CNN) in Tensorflow/Keras to classify CSV files containing
spectral readings from plants in the Genus Rhododendron.
---

## Setup
1. Clone the repository to your local machine.
1. Confirm you have the necessary Python version and packages installed (see Environment section below).
1. Prepare two sets of CSV files, each within a directory that indicates the class name.  These folders should be put 
   together in a directory, with no other files. e.g.,
```
training_data_folder
└───species_a
└───species_b
```
   

4. You should prepare a separate group of test images, either manually, or you can use the available utility script: 
   `utilities\divide_training_testing.py`.
    - This script defaults to creates a split of 90% for training/validation and 10% for testing. It creates copies of 
      the images in four new CSV files  -- *species1_testing, species1_training, species2_testing, species2_training*.

### Environment
This code has been tested in Python 3.9.4 in Windows and Ubuntu, using Anaconda 
for virtual environments.  Please consult `requirements.txt` or the list below 
for necessary Python packages.

#### Tested Package Versions (For now):
- pandas~=1.4.1
- numpy~=1.21.5
- tensorflow~=2.5.0
- opencv-python~=4.5.5.64
- requests~=2.27.1

### Structure basis
This repo is largely based off the field_classification repo developed by Beth McDonald (emcdona1, Field Museum, former NEIU), Sean Cullen (SeanCullen11, NEIU) and Allison Chen (allisonchen23, UCLA).

Field classification repo is also a CNN structure, but it is used to classify leaf image 

Link to field_classification repo:
https://github.com/emcdona1/field_classification 


## Workflow
1. Run `train_models_image_classification.py`, using arguments to specify image sets and hyper-parameters.

- **Arguments**: (`-h` flag for full details)
    - `training_set` (positional, required) - file path of the directory that contains the training CSV files 
      (e.g. `training_data_folder` as described in the Setup section.)
    - `-lr` - learning rate value (*decimal number*, default = 0.001)
    - `-f` - number of folds (1 for single-model, 2+ for cross-fold validation) (*integer <= 1*, default=1)
        - *Note*: Currently, cross-fold validation is not implemented.
    - `-e` - number of epochs per fold (*integer >= 5*, default=25)
    - `-cls` - number of classes (*integer >= 2*, default=2)
 
- **Output**:
    - Directory `saved_models` is created in current working directory, which will contain one model file per fold (file name format: `CNN_#.model`).

- **Example execution (CNN)**: `python train_models_classification.py Model_1_intric_thym\training -lr 0.005 -f 1 -e 50 -cls 2`

2. Classifying images after the model has been trained has not been implemented yet

## Todo
1. Finish converting repo to fit new data sets
   1. `training_data.py` - define csv dimensions variable by getting the actual csv dimensions, load in csv files as the data sets and get class labels
   2. `train_models_classification.py` - implement new train_and_save_all_models function for the new data set
2. Remove hardcoded arguments 
   1. `train_models_classification.py` - change CNN structure function call to take in the inputted arguments 
   2. `cnnmodel.py` - uncomment input shape and make the shape the dimensions of the CSV
   3. `modeltrainingarguments.py` - uncomment dataframe_dim and make the shape the dimensions of the CSV and complete the validate method
3. Implement testing models after they are trained by using `classify_images_by_vote.py` as a reference 
4. Visualization
   1. The functionality to add graphs exists in the `model_training.py` and is currently commented out in validate_model_at_epoch_end. This can be added later using the graph script from field_classification


## Contributors and licensing
This code has been developed by Sean Cullen ([SeanCullen11](https://github.com/SeanCullen11), NEIU)
and Beth McDonald ([emcdona1](https://github.com/emcdona1), *Field Museum, former NEIU*), 



This code was developed under the guidance of Dr. Matt von Konrat (Field Museum),

This project was made possible thanks to [the Grainger Bioinformatics Center](https://www.fieldmuseum.org/science/labs/grainger-bioinformatics-center) at the Field Museum.

This project has been created for use in the Field Museum Gantz Family Collections Center, 
under the direction of [Dr. Matt von Konrat](https://www.fieldmuseum.org/about/staff/profile/16), Head of Botanical Collections at the Field.

Please contact Dr. von Konrat for licensing inquiries.
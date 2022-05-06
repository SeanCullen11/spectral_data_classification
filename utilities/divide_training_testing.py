# modified version of create_test_group.py from field_classification repo
import os
import argparse
import time
import pandas as pd

SPLIT = .1  # 10% of the images will be reserved for testing

def process_input_arguments():
    ''' Parse command line arguments
    PARAMETERS:
    -----
    none (reads arguments from the command line)

    OUTPUT:
    -----
    @directory - file folder in working directory containing 2 CSV files

    @categories - list of size 2, containing the CSV file names

    '''

    parser = argparse.ArgumentParser('data to be imported')
    parser.add_argument('-d', '--directory', default='', help='Folder holding category folders')
    parser.add_argument('-c1', '--category1', default='', help='1st folder')
    parser.add_argument('-c2', '--category2', default='', help='2nd folder')
    args = parser.parse_args()
    categories = [args.category1.replace('\\', '').replace('/', ''),
                  args.category2.replace('\\', '').replace('/', '')]
    return args.directory, categories


def split_images(directory, categories):
    """ Split the CSV file into training and testing dataframes

   PARAMETERS:
   -----
    @directory - file folder in working directory containing 2 CSV files

    @categories - list of size 2, containing the CSV file names

   OUTPUT:
   -----
   @data_groups - a nested list of dictionaries, each list item is either the training or testing set of each category
                  this structure is easily translated into a dataframe later on
   """

    data_groups = []
    category_index = 0
    for category in categories:
        path = os.path.join(directory, category)
        file = pd.read_csv(path)
        file = file.sample(frac=1).reset_index(drop=True)

        train = []
        test = []

        for index, row in file.iterrows():
            if index < round(file.shape[0] * SPLIT):
                row = dict(row)
                test.append(row)
            else:
                row = dict(row)
                train.append(row)

        data_groups.append(test)
        data_groups.append(train)
        print(str(categories[category_index]) + ' split into ' + str(len(train)) + ' training images and ' + str(len(test)) + ' testing images.')
        category_index += 1

    return data_groups


def copy_images_to_new_directories(directory, categories, data_groups):
    """ Save the training and testing folders to the root directory

   PARAMETERS:
   -----
    @directory - file folder in working directory containing 2 CSV files

    @categories - list of size 2, containing the CSV file names

   @data_groups - a nested list of dictionaries, each list item is either the training or testing set of each category
                  this structure is easily translated into a dataframe here

   OUTPUT:
   -----
   nothing in Python (copies of images are saved in filesystem)
   """

    for d in range(0, len(data_groups)):
        data_df = pd.DataFrame(data_groups[d])
        data_df = data_df.drop(['Unnamed: 0', 'file_names', 'accession', 'type'], axis=1)
        if d % 2 == 0:
            if d < 2:
                name = categories[0].replace(".csv", "")
                data_df.to_csv(directory + "\\" + name + "_testing.csv")
            else:
                name = categories[1].replace(".csv", "")
                data_df.to_csv(directory + "\\" + name + "_testing.csv")
        else:
            if d >= 2:
                name = categories[1].replace(".csv", "")
                data_df.to_csv(directory + "\\" + name + "_training.csv")
            else:
                name = categories[0].replace(".csv", "")
                data_df.to_csv(directory + "\\" + name + "_training.csv")


if __name__ == '__main__':
    # Start execution and parse arguments
    start_time = time.time()

    directory, categories = process_input_arguments()
    data_groups = split_images(directory, categories)
    copy_images_to_new_directories(directory, categories, data_groups)

    # Finish execution
    end_time = time.time()
    print('Task completed in %.1f seconds' % (end_time - start_time))

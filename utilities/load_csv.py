import os
import sys
import pandas as pd
import numpy as np


def divide_classes(data):
    labels = get_labels_and_groups(data)
    folder = data.replace('.csv', "")
    spectral_data = pd.read_csv(data)

    species = []
    count = 1
    for l in labels:
        for line in range(len(spectral_data)):
            if spectral_data.loc[line]['species'] == l:
                specimen = dict(spectral_data.loc[line])
                species.append(specimen)

        species_df = pd.DataFrame(species)
        species_df.to_csv(folder + '\\' + l + '.csv')
        print("Saving", str(count) + "/" + str(len(labels)))
        count += 1
        species.clear()


def get_labels_and_groups(data):
    spectral_data = pd.read_csv(data)
    spectral_species = spectral_data.pop("species")

    spectral_species = np.array(spectral_species)
    labels = set(spectral_species)
    labels = sorted(labels)
    print("There are", len(spectral_species), "samples, divided into", len(labels), "different groups")

    species_dic = {}
    for i in range(len(labels)):
        species_dic.update({labels[i] : 0})

    for x in range(len(spectral_species)):
        for y in species_dic.items():
            if spectral_species[x] == y[0]:
                species_dic[spectral_species[x]] += 1

    ordered_species = sorted(species_dic.items(), reverse=True, key=lambda x: x[1])
    print("The top 5 groups are", end = " ")

    for s in range(0,5):
        print(ordered_species[s], end = " ")

    print("")
    return labels


def generate_folder(data):
    spec = data.split('\\')
    folder = spec[len(spec) - 1]
    folder = folder.replace(".csv", "")

    path = spec[:len(spec) - 1]
    path = '\\'.join(path)

    total_path = os.path.join(path, folder)
    if not os.path.exists(total_path):
        os.mkdir(total_path)


def main():
    user_input = sys.argv
    data = str(user_input[1])
    generate_folder(data)
    divide_classes(data)


if __name__ == '__main__':
    main()
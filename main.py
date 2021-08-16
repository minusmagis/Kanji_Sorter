import pandas as pd
from collections import Counter
import pprint
import csv


def list_delete_nan(list_to_delete):
    flat_list = flatten_list(list_to_delete)
    return [item for item in flat_list if item != 'nan']


def flatten_list(non_flat_list):
    flat_list = list()
    for item in non_flat_list:
        if ';' in str(item):
            for subitem in item.split(';'):
                flat_list.append(str(subitem.strip()))
        else: flat_list.append(str(item))
    return flat_list


def save_data(new_rows, file_path):
    with open(file_path, 'w', encoding='UTF8',newline='') as CSV_File:
        writer = csv.writer(CSV_File)
        writer.writerows(new_rows)
        CSV_File.close()


kanji_list = pd.read_csv('heisig-kanjis.csv')

component_list = list_delete_nan(kanji_list['components'])

ordered_component_dict = [item for item in Counter(component_list).items()]

sorted_by_second = sorted(ordered_component_dict, key=lambda tup: tup[1], reverse=True)

sorted_dataframe = list()

# pprint.pprint(sorted_by_second)
for index, sorted in enumerate(sorted_by_second):
    component, apperarance = sorted
    print(str(index) + ' of ' + str(len(sorted_by_second)))
    for index, row in kanji_list.iterrows():
        key_5th = str(row['keyword_5th_ed'])
        if component in key_5th and len(component) == len(key_5th):
            # print(row['kanji'])
            # print(type(row['kanji']))

            sorted_dataframe.append([row['kanji'],row['keyword_5th_ed'],row['id_5th_ed']])

save_data(sorted_dataframe,r'sorted_kanjis.csv')

print(sorted_dataframe, "\n")
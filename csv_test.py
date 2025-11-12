import csv

# format
# scenename, set_name, page, index

# TODO: generate automatically via obsidian text stuff
# add input for adding scene name and set name


data = [['scene', 'en', 'pt-br'], ["prologue_start_1_1", 'Hello', "Olá"], ["prologue_start_1_2", 'Testing', "Testando"]]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
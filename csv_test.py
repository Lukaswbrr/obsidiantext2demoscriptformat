import csv

# format
# scenename, set_name, page, index

# TODO: generate automatically via obsidian text stuff
# add input for adding scene name and set name

def add_to_csv(lines):
    # NOTE: temporary data, will be appended to existing csv next update
    initial_data = [['scene', 'en', 'pt-br']]

    for key, value in lines.items():
        split_key = key.split("_")
        set_name = "start"
        scene_name = "prologue"
        page = split_key[1]
        index = split_key[3]

        initial_data.append([f"{scene_name}_{set_name}_{page}_{index}", value, ""])
    
    print(initial_data)

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(initial_data)

# TODO: add mode for appending to existant csv files, replace existant files, make it so
# it doesnt overwrite others columns, etc
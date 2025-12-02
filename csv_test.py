import csv

# format
# scenename, set_name, page, index

# TODO: generate automatically via obsidian text stuff
# add input for adding scene name and set name

def add_to_csv(lines, setname: str, scenename: str, filename: str = 'output/output.csv'):
    # NOTE: temporary data, will be appended to existing csv next update
    initial_data = [['scene', 'en', 'pt-br']]

    for key, value in lines.items():
        split_key = key.split("_")
        set_name = setname
        scene_name = scenename
        page = split_key[1]
        index = split_key[3]

        initial_data.append([f"{scene_name}_{set_name}_{page}_{index}", value, ""])
    
    print(initial_data)
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(initial_data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def append_to_csv(lines, scenename: str, setname: str, filename: str = "output/output.csv"):
    data = []

    for key, value in lines.items():
        split_key = key.split("_")
        set_name = setname
        scene_name = scenename
        page = split_key[1]
        index = split_key[3]

        data.append([f"{scene_name}_{set_name}_{page}_{index}", value, ""])
    
    print(data)

    try:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except Exception as e:
        print(f"Error writing to CSV: {e}")

def continue_to_nextline_csv(lines, scene_name_csv: str = "prologue", set_name_csv: str = "start", filename: str = "output/output.csv"):
    data = []
    page = ""
    dict_rows = []

    try:
        with open(filename, 'r+') as file:
            reader_dict = csv.DictReader(file)

            dict_rows = list(reader_dict)

    except Exception as e:
        print(f"Error writing to CSV: {e}")
    
    last_page_found = 0

    # NOTE: this is for finding the last set name index position,
    # to be able to continue from there
    insert_index = 0

    for k in dict_rows:
        scene_name = k["scene"].split("_")[0]
        set_name = k["scene"].split("_")[1]
        page_found = k["scene"].split("_")[2]
        
        if set_name == set_name_csv and scene_name == scene_name_csv:
            insert_index += 1
            last_page_found = int(page_found)


    for key, value in lines.items():
        split_key = key.split("_")
        set_name = set_name_csv
        scene_name = scene_name_csv
        page = str(int(split_key[1]) + last_page_found)
        index = split_key[3]

        new_row_dict = {
            'scene': f"{scene_name}_{set_name}_{page}_{index}",
            'en': value,
            'pt-br': ""
        }

        dict_rows.insert(insert_index, new_row_dict)
        insert_index += 1
    

    fieldnames = dict_rows[0].keys()

    print(dict_rows)

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()

            writer.writerows(dict_rows)
    except Exception as e:
        print(f"Error writing to CSV: {e}")


# this adds value to existant fields, like prologue_start_1_1
# which is going to be used to fill the pt-br column
def add_existant_to_csv(lines, filename: str = 'output.csv'):
    pass

# replaces existant fields values of a specific column
# maybe this can work as a add too?
def replace_existent_csv(lines, scene_name_csv: str, set_name_csv: str, page_csv: str, index_csv: str, lang: str, filename: str = 'output/output.csv'):
    data = []
    page = ""
    dict_rows = []

    try:
        with open(filename, 'r+') as file:
            reader_dict = csv.DictReader(file)

            dict_rows = list(reader_dict)

    except Exception as e:
        print(f"Error writing to CSV: {e}")
    
    if not lang in dict_rows[0]:
        print(f"Language column '{lang}' does not exist in the CSV.")
        return

    index = 0


    for k in dict_rows:
        scene_name = k["scene"].split("_")[0]
        set_name = k["scene"].split("_")[1]
        page_found = k["scene"].split("_")[2]
        index_found = k["scene"].split("_")[3]
        
        print(scene_name == scene_name_csv)
        print(page_found == page_csv)
        print(index_found == index_csv)
        if scene_name == scene_name_csv and page_found == page_csv and index_found == index_csv:
            print(scene_name)
            print(index)
            break

        index += 1
    
    for k in range(len(lines)):
        index_replace = index + k

        if index_replace >= len(dict_rows):
            print("Index out of range, stopping replacement.")
            break

        scene_name = dict_rows[index_replace]["scene"].split("_")[0]
        set_name = dict_rows[index_replace]["scene"].split("_")[1]

        if scene_name != scene_name_csv or set_name != set_name_csv:
            print("Scene name or set name mismatch, stopping replacement.")
            break

        dict_rows[index_replace][lang] = list(lines.values())[k]
        print(f"Replaced line at index {index_replace}: {dict_rows[index_replace]}")
    
    fieldnames = dict_rows[0].keys()

    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()

            writer.writerows(dict_rows)
    except Exception as e:
        print(f"Error writing to CSV: {e}")


# TODO: add mode for appending to existant csv files, replace existant files, make it so
# it doesnt overwrite others columns, etc
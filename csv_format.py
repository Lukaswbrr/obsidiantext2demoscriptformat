import csv

def _add_dialogue_format(scene_name, lang):
    split = scene_name.split("_")

    set_name = split[1]
    page = split[2]
    index = split[3]

    dialogue_func = ""

    if page == "1" and index == "1":
        dialogue_func = f"add_dialogue_start(tr(\"{scene_name}\"), \"{set_name}\")"
    elif index == "1":
        dialogue_func = f"add_dialogue_next(tr(\"{scene_name}\"), \"{set_name}\")"
    else:
        dialogue_func = f"add_dialogue(tr(\"{scene_name}\"))"

    return dialogue_func

def format_test(csv_file, lang):
    # NOTE: format
    # add_dialogue(scene_csv_key) (first page is add_dialogue_start)
    # if next page, use add_dialogue_next

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # TODO: get only rows that match the language input, like en
            # skip en as value

            if not lang in row:
                print(f"Language {lang} not found in CSV.")
                return
            
            #print(f"{row["scene"]}: {row[lang]}")
            
            print(_add_dialogue_format(row["scene"], row[lang]) )


    pass
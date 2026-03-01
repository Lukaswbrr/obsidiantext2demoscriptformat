import csv
import os

def _add_dialogue_format(scene_name, lang, filename=""):
    split = scene_name.split("_")
    continues = {}

    if filename:
        filename = filename.split("/")[-1]
        filename = filename.replace(".csv", "")
        if os.path.exists(f"cache/continue/{filename}.txt"):
            with open(f"cache/continue/{filename}.txt", "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        continues[line] = True
    
    set_name = split[1]
    page = split[2]
    index = split[3]

    dialogue_func = ""
    
    if page == "1" and index == "1":
        dialogue_func = f"\nadd_dialogue_start(tr(\"{scene_name}\"), \"{set_name}\")"
    elif continues.get(f"{page}_{index}", False):
        dialogue_func = f"add_dialogue_continue_no_space(tr(\"{scene_name}\"))"
    elif index == "1":
        dialogue_func = f"\nadd_dialogue_next(tr(\"{scene_name}\"))"
    else:
        dialogue_func = f"add_dialogue(tr(\"{scene_name}\"))"

    return dialogue_func

def format_css(csv_file, lang, scene: str = "", setname: str = ""):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            # TODO: get only rows that match the language input, like en
            # skip en as value

            if not lang in row:
                print(f"Language {lang} not found in CSV.")
                return
            
            
            if not setname and not scene:
                print(_add_dialogue_format(row["scene"], row[lang], csv_file) )
                continue

            row_scene = row["scene"].split("_")[0]
            row_setname = row["scene"].split("_")[1]

            if row_scene == scene and row_setname == setname:
                print(_add_dialogue_format(row["scene"], row[lang], csv_file) )
                

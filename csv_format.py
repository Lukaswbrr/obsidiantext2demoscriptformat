import csv

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
            
            print(f"{row["scene"]}: {row[lang]}")


    pass
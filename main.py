import pyperclip as pc
from csv_test import add_to_csv, append_to_csv, continue_to_nextline_csv, replace_existent_csv
from format import format_text
from csv_format import format_css

print("Welcome to the Obsidian Text to Demo Script Format CSV Tool!")

confirm_input = input("When text is copied to clipboard, press Enter to continue...")
clipboard_text = pc.paste()

instructions = """Instructions:
1 - Append to CSV: Appends the formatted text to an existing CSV file.
2 - Continue to Next Line in CSV: Finds the next available line in the CSV based on
   scene and set names, and adds the formatted text there.
3 - Replace Existent in CSV: Replaces existing lines in the CSV based on scene,
   set names, page, and index with the formatted text.
4 - Print clipboard text: Displays the current text in the clipboard.
5 - Change clipboard text: Allows you to change the clipboard text.
6 - Print clipboard formatted text: Displays the text after formatting.
7 - Print format to DemoScripter syntax: Displays the text in DemoScripter format of a specific csv file.
10 - Exit: Exits the program.
help - Displays these instructions again."""

print(instructions)

while True:
    print("-------------------------------")
    user_input = input("Select an option (1-10): ")

    match user_input:
        case '1':
            print("Appending to CSV...")
            filename = input("Enter filename (default: output/output.csv): ") or "output/output.csv"
            
            if ".csv" not in filename:
                print("Invalid filename. Must end with .csv")
                continue

            scenename = input("Enter scene name: ")

            if scenename.strip() == "":
                print("Scene name cannot be empty.")
                continue
            
            if "_" in scenename:
                print("Scene name cannot contain underscores (_).")
                continue

            setname = input("Enter set name: ")
            
            if setname.strip() == "":
                print("Set name cannot be empty.")
                continue
            
            if "_" in setname:
                print("Set name cannot contain underscores (_).")
                continue

            append_to_csv(format_text(clipboard_text), scenename, setname, filename)
        case '2':
            print("Contiuning to CSV...")
            filename = input("Enter filename (default: output/output.csv): ") or "output/output.csv"
            
            if ".csv" not in filename:
                print("Invalid filename. Must end with .csv")
                continue

            scenename = input("Enter scene name: ")

            if scenename.strip() == "":
                print("Scene name cannot be empty.")
                continue
            
            if "_" in scenename:
                print("Scene name cannot contain underscores (_).")
                continue

            setname = input("Enter set name: ")
            
            if setname.strip() == "":
                print("Set name cannot be empty.")
                continue
            
            if "_" in setname:
                print("Set name cannot contain underscores (_).")
                continue

            continue_to_nextline_csv(format_text(clipboard_text), scenename, setname, filename)
        case '3':
            print("Replacing to CSV...")
            filename = input("Enter filename (default: output/output.csv): ") or "output/output.csv"
            
            if ".csv" not in filename:
                print("Invalid filename. Must end with .csv")
                continue

            scenename = input("Enter scene name: ")

            if scenename.strip() == "":
                print("Scene name cannot be empty.")
                continue
            
            if "_" in scenename:
                print("Scene name cannot contain underscores (_).")
                continue

            setname = input("Enter set name: ")
            
            if setname.strip() == "":
                print("Set name cannot be empty.")
                continue
            
            if "_" in setname:
                print("Set name cannot contain underscores (_).")
                continue

            lang = input("Enter language code to replace (e.g., 'pt-br'): ")

            if lang.strip() == "":
                print("Language code cannot be empty.")
                continue
        
            try:
                page = int(input("Enter page number: "))
                index = int(input("Enter index number: "))
            except ValueError:
                print("Page and index must be integers.")
                continue

            page = str(page)
            index = str(index)
            
            replace_existent_csv(format_text(clipboard_text), scenename, setname, page, index, lang, filename)
        case '4':
            print(f"Clipboard text: {clipboard_text}")
        case '5':
            input("When ready, copy the new text to clipboard and press Enter...")
            clipboard_text = pc.paste()
            print("Clipboard text updated.")
        case '6':
            formatted_lines = format_text(clipboard_text)
            print("Formatted text:")
            
            for key, value in formatted_lines.items():
                print(f"{key}: {value}")
        case '7':
            filepath = input("Type the csv file path: ")
            input_scene = input("Type the scene name to filter (or press Enter to skip): ")
            input_setname = input("Type the set name to filter (or press Enter to skip): ")
            
            format_css(filepath, "en", input_scene, input_setname)
        case '10':
            print("Exiting program.")
            break
        case 'help':
            print(instructions)
        case _:
            print("Invalid choice.")
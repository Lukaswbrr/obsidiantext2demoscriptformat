import pyperclip as pc
from csv_test import add_to_csv, append_to_csv, continue_to_nextline_csv, replace_existent_csv
from format import test_format
from csv_format import format_test

# NOTE: r makes the text raw, so it doesn't escape characters

test_text = r""">It was a single decision.
>It's scary how much a single decision can change one's life so much.
>The decision in that day really changed me. \Comparing that day and the yesterday, it was like a window, where both sides are extremely different.
>One side was the normal me.
>But the other, was no longer in the realms of normality.
>
>
>test new line

>That day, I decided to follow my heart.
>To chase after what I truly wanted.
>And so, I left everything behind.
>Family, friends, everything.
>It was a tough decision, but I knew it was the right one.
>As I walked away from my old life, I felt a mix of fear and excitement.
>But deep down, I knew that this was the start of something new.
"""

test_text2 = r""">Foi uma decisão única.
>É assustador o quanto uma única decisão pode mudar tanto a vida de alguém.
>A decisão daquele dia realmente me mudou. \Comparando aquele dia e o ontem, era como uma janela, onde ambos os lados são extremamente diferentes.
>Um lado era o eu normal.
>Mas o outro, já não estava mais nos domínios da normalidade.
>
>
>teste nova linha

>Naquele dia, decidi seguir meu coração.
>Perseguir o que eu realmente queria.
>E assim, deixei tudo para trás.
>Família, amigos, tudo.
>Foi uma decisão difícil, mas eu sabia que era a certa.
>Enquanto eu me afastava da minha vida antiga, senti uma mistura de medo e excitação.
>Mas lá no fundo, eu sabia que aquele era o começo de algo novo.
"""

test_text3 = r""">Foi uma decisão única.
>É assustador o quanto uma única decisão pode mudar tanto a vida de alguém.
>A decisão daquele dia realmente me mudou. \Comparando aquele dia e o ontem, era como uma janela, onde ambos os lados são extremamente diferentes.
>Um lado era o eu normal.
>Mas o outro, já não estava mais nos domínios da normalidade.

>Naquele dia, decidi seguir meu coração.
>Perseguir o que eu realmente queria.
>E assim, deixei tudo para trás.
>Família, amigos, tudo.
>Foi uma decisão difícil, mas eu sabia que era a certa.
>Enquanto eu me afastava da minha vida antiga, senti uma mistura de medo e excitação.
>Mas lá no fundo, eu sabia que aquele era o começo de algo novo.
"""

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
10 - Exit: Exits the program."""

print(instructions)

while True:
    print("-------------------------------")
    user_input = input("Select an option (1-10): ")

    match user_input:
        # case '1':
        #     print("Adding to CSV...")
        #     filename = input("Enter filename (default: output/output.csv): ") or "output/output.csv"
            
        #     if ".csv" not in filename:
        #         print("Invalid filename. Must end with .csv")
        #         continue

        #     scenename = input("Enter scene name: ")

        #     if scenename.strip() == "":
        #         print("Scene name cannot be empty.")
        #         continue
            
        #     if "_" in scenename:
        #         print("Scene name cannot contain underscores (_).")
        #         continue

        #     setname = input("Enter set name: ")
            
        #     if setname.strip() == "":
        #         print("Set name cannot be empty.")
        #         continue
            
        #     if "_" in setname:
        #         print("Set name cannot contain underscores (_).")
        #         continue
            
        #     print("Added to CSV.")
            
        #     add_to_csv(test_format(test_text), scenename, setname, filename)
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

            append_to_csv(test_format(clipboard_text), scenename, setname, filename)
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

            continue_to_nextline_csv(test_format(clipboard_text), scenename, setname, filename)
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
            
            replace_existent_csv(test_format(clipboard_text), scenename, setname, page, index, lang, filename)
        case '4':
            print(f"Clipboard text: {clipboard_text}")
        case '5':
            input("When ready, copy the new text to clipboard and press Enter...")
            clipboard_text = pc.paste()
            print("Clipboard text updated.")
        case '6':
            formatted_lines = test_format(clipboard_text)
            print("Formatted text:")
            
            for key, value in formatted_lines.items():
                print(f"{key}: {value}")
        case '7':
            filepath = input("Type the csv file path: ")
            input_scene = input("Type the scene name to filter (or press Enter to skip): ")
            input_setname = input("Type the set name to filter (or press Enter to skip): ")
            
            format_test(filepath, "en", input_scene, input_setname)
        case '10':
            print("Exiting program.")
            break
        case _:
            print("Invalid choice.")
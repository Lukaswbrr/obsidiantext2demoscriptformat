clipboard_text = ">Hello, World!"

start = input("Once ready with text on clipboard, press Enter to start...")

print("yey")

def _add_dialogue_format(text: str) -> str:
    if text[0] == ">":
        new_text = text.replace(">", "")
        text = new_text

    print(text)

_add_dialogue_format(clipboard_text)
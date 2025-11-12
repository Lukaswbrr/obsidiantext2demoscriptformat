import pyperclip as pc

clipboard_text = pc.paste()

test_text = """
>It was a single decision.
>It's scary how much a single decision can change one's life so much.
>The decision in that day really changed me. Comparing that day and the yesterday, it was like a window, where both sides are extremely different.
>One side was the normal me.
>But the other, was no longer in the realms of normality.
"""

#start = input("Once ready with text on clipboard, press Enter to start...")

#print("yey")

# TODO: add support for special characters
# for example, \ makes a continue in the same line, without going to the next line
# like NScripter.
# add support for when it's more than the same special character (@@, \\, etc), it types
# the actual character instead of interpreting it as a special character

def test_format(text: str) -> str:
    new_text = text.replace(">", "")
    text = new_text

    split_line = text.splitlines()
    current_index = 1

    lines = []
    
    for k in split_line:
        if k.count(".") > 1:
            print("more than one!")
            print(k)
        
        current_index += 1


test_format(test_text)
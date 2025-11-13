import pyperclip as pc


# NOTE: r makes the text raw, so it doesn't escape characters
test_text = r""">It was a single decision.
>It's scary how much a single decision can change one's life so much.
>The decision in that day really changed me. \Comparing that day and the yesterday, it was like a window, where both sides are extremely different.
>One side was the normal me.
>But the other, was no longer in the realms of normality.

>That day, I decided to follow my heart.
>To chase after what I truly wanted.
>And so, I left everything behind.
>Family, friends, everything.
>It was a tough decision, but I knew it was the right one.
>As I walked away from my old life, I felt a mix of fear and excitement.
>But deep down, I knew that this was the start of something new.
"""

#start = input("Once ready with text on clipboard, press Enter to start...")

#print("yey")

# TODO: add support for special characters
# for example, \ makes a continue in the same line, without going to the next line
# like NScripter.
# add support for when it's more than the same special character (@@, \\, etc), it types
# the actual character instead of interpreting it as a special character

def test_format(text: str) -> str:
    #new_text = text.replace(">", "")
    #text = new_text

    split_line = text.splitlines()
    current_index = 1
    current_page = 1
    newline_count = 0

    lines = {}
    
    for k in split_line:
        newline_string = ""

        # TODO: instead of replacing > at start, when it detects a empty line with >,
        # add \n to the next line, depending on how much spaces there are after >
        if k == "":
            current_index = 1
            current_page += 1
            newline_count = 0
            continue

        if k == ">":
            newline_count += 1
            continue
        
        k = k.replace(">", "")

        # NOTE: needs testing
        if newline_count > 0:
            for m in range(newline_count):
                newline_string += "\n"
            
            #k = newline_string + k
            new_text = newline_string + k
            k = new_text
            newline_count = 0


        if k.count("\\") > 0:
            continue_split = k.split("\\")

            for cont in continue_split:
                if "\\" in cont:
                    cont = cont.replace("\\", "")

                lines[f"page_{current_page}_line_{current_index}"] = cont
                current_index += 1
                
            continue
        
        if k in lines.values():
            continue

        lines[f"page_{current_page}_line_{current_index}"] = k
        current_index += 1
    
    return lines

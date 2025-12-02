import pyperclip as pc
import re

# TODO: add support for special characters
# for example, \ makes a continue in the same line, without going to the next line
# like NScripter.
# add support for when it's more than the same special character (@@, \\, etc), it types
# the actual character instead of interpreting it as a special character

def _split_with_escapes(line: str):
    """
    Split on standalone continuation backslashes:
    - Collapse '\\' -> '\'
    - Keep '\n', '\t', '\r' as literal pairs (do not split)
    - Split on '\' followed by any other char or end-of-line (drop that '\')
    """
    parts = []
    buf = []
    i = 0
    L = len(line)
    while i < L:
        ch = line[i]
        if ch == "\\":
            if i + 1 < L:
                nxt = line[i + 1]
                if nxt == "\\":           # literal backslash
                    test = "\\"
                    buf.append(test[0])
                    print(buf)
                    i += 2
                    continue
                if nxt in ("t", "r"):  # keep escape as literal
                    buf.append("\\")
                    buf.append(nxt)
                    i += 2
                    continue
                # continuation split (drop '\')
                if buf:
                    parts.append("".join(buf))
                    buf = []
                i += 1
                continue
            else:
                # trailing '\' acts like a continuation split
                if buf:
                    parts.append("".join(buf))
                    buf = []
                i += 1
                continue
        else:
            buf.append(ch)
            i += 1
    if buf:
        parts.append("".join(buf))
    return parts

def format_text(text: str) -> str:
    #new_text = text.replace(">", "")
    #text = new_text

    split_line = text.splitlines()
    current_index = 1
    current_page = 1
    newline_count = 0
    already_empty_line = False

    lines = {}
    
    for k in split_line:
        newline_string = ""

        # TODO: instead of replacing > at start, when it detects a empty line with >,
        # add \n to the next line, depending on how much spaces there are after >
        if k == "":
            if already_empty_line:
                continue
            
            current_index = 1
            current_page += 1
            newline_count = 0
            already_empty_line = True
            continue

        if k == ">":
            newline_count += 1
            continue

        already_empty_line = False
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
            # TODO: make it not split special characters, like
            # [\, \n, etc]

            continue_split = k.split("\\")

            # if "\\" in k:
            #     # Split only on standalone continuation backslashes:
            #     # A continuation backslash = '\' not followed by n,t,r or '\'
            #     # Pattern explanation:
            #     # \\(?=[^tr\\]|$)  -> a backslash with next char NOT in t r \ OR end of string
            #     parts = re.split(r'\\(?=[^tr\\]|$)', k)

            #     for part in parts:
            #         if not part:
            #             continue
            #         lines[f"page_{current_page}_line_{current_index}"] = part
            #         current_index += 1
            #     continue

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

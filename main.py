import pyperclip as pc
from csv_test import add_to_csv, append_to_csv, continue_to_nextline_csv
from format import test_format
from csv_format import format_test

# NOTE: r makes the text raw, so it doesn't escape characters
clipboard_text = pc.paste()


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

#print( test_format(test_text) )

#add_to_csv(test_format(test_text))

#append_to_csv(test_format(test_text), "output_test.csv")

continue_to_nextline_csv(test_format(test_text), "output_test copy.csv")

#format_test('output.csv', "en")
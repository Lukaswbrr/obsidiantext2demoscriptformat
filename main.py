import pyperclip as pc
from csv_test import add_to_csv, append_to_csv, continue_to_nextline_csv, replace_existent_csv
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

#print( test_format(test_text) )

#add_to_csv(test_format(test_text))

#append_to_csv(test_format(test_text), "output_test.csv")

#continue_to_nextline_csv(test_format(test_text), "output_test copy.csv")

replace_existent_csv(test_format(test_text3), "prologue", "start", "1", "1", "pt-br")

#format_test('output/output_test copy.csv', "en")
>[!WARNING]
>This is a temporary solution and not meant to be used as a permament solution for making CSV files for DemoScripter!
>In the future, DemoScripter will have a proper addon menu that you can create CSV files automatically!

Script for transforming normal text to DemoScripter syntax.

Saves files to CSV for easy translation for DemoScripter.

The syntax of obsidian is the way I write for visual novels, thats why theres is a > at the start, which gets replaced by nothing.

## Instructions
Before running this script, make sure you have a text on your clipboard!

Run the main.py file. It will print the instructions for the usage.

To create a file with CSV, run the first instruction. It will create a file with the parameters you specified. 

When the file is created, make sure to add a new row on the first line for scene and language.


### Example of first intrusction
scene,en,pt-br
prologue_start_1_1,test1,
prologue_start_1_2,test2,
prologue_start_1_3,test3,
prologue_start_1_4,test4 ,
prologue_start_1_5,test5 ,
prologue_start_1_6,test6,
prologue_start_1_7,test7,
prologue_start_2_1,test8 ,
prologue_start_2_2,Test9 ,
prologue_start_2_3,Test10 ,
prologue_start_2_4,Test11,

### Add text to a second language
If you want to add text to a second language in the same csv file (assuming you're still on the script), type 5 and press enter.

Copy the text that will be used for the second language and then press enter.

### Print DemoScripter syntax


## Obsidian Syntax
\> does nothing. It's just a way I write visual novel scripts on obsidian, which gets replaced.
\ is a line break, making the text go to the next line.

### Example
In the example below, > gets ignored and replaced.

\>test1
\>test2
\>test3
\>test4 \test5 \test6
\>test7

\>test8 \Test9 \Test10 \Test11
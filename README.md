>[!WARNING]
>This is a temporary solution and not meant to be used as a permament solution for making CSV files for DemoScripter!
>In the future, DemoScripter will have a proper addon menu that you can create CSV files automatically!

Script for transforming normal text to [DemoScripter](https://github.com/Lukaswbrr/Demo-Scripter) syntax, including saving to CSV files for easy translation.

The syntax of obsidian is the way I write for visual novels, thats why theres is a > at the start, which gets replaced by nothing.

## Instructions
Before running this script, make sure you have a text on your clipboard!

Run the main.py file. It will print the instructions for the usage.

To create a file with CSV, run the first instruction. It will create a file with the parameters you specified. 

When the file is created, make sure to add a new row on the first line for scene and language.

When creating CSV files with this program, I recommend creating seperate CSV files for each scene before merging all together to one big CSV file for your visual novel project.

### Example of first intrusction
```
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
```

### Add text to a second language
If you want to add text to a second language in the same csv file (assuming you're still on the script), type 5 and press enter.

Copy the text that will be used for the second language and then press enter.

Then type 3 and press enter.

Type the filename where your csv is located on, scene name and set name to where you want to add the contents to second language.

If you have the entire text, start to finish, then type for page number and index number both to 1.

### Example of third instruction
```
scene,en,pt-br
prologue_start_1_1,test1,teste1
prologue_start_1_2,test2,teste2
prologue_start_1_3,test3,teste3
prologue_start_1_4,test4 ,teste4 
prologue_start_1_5,test5 ,teste5 
prologue_start_1_6,test6,teste6
prologue_start_1_7,test7,teste7
prologue_start_2_1,test8 ,teste8 
prologue_start_2_2,Test9 ,Teste9 
prologue_start_2_3,Test10 ,Teste10 
prologue_start_2_4,Test11,Teste11
```

### Print DemoScripter syntax
After creating the CSV file, press the instruction 7.

Type where your CSV file is located.

If you want for all the file to be printed as DemoScripter syntax, just press enter without any arguments.

#### Example (using the CSV file from third instruction example)
```
add_dialogue_start(tr("prologue_start_1_1"), "start")
add_dialogue(tr("prologue_start_1_2"))
add_dialogue(tr("prologue_start_1_3"))
add_dialogue(tr("prologue_start_1_4"))
add_dialogue(tr("prologue_start_1_5"))
add_dialogue(tr("prologue_start_1_6"))
add_dialogue(tr("prologue_start_1_7"))

add_dialogue_next(tr("prologue_start_2_1"))
add_dialogue(tr("prologue_start_2_2"))
add_dialogue(tr("prologue_start_2_3"))
add_dialogue(tr("prologue_start_2_4"))
```

Then, you can add this to your DemoScripter project!

>[!WARNING]
>This does NOT automatically use add_dialogue_continue on lines that contains \\.
>I'm only planning on adding this functionality on DemoScripter addon menu.

### All Instructions
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

## Obsidian Syntax
\> does nothing. It's just a way I write visual novel scripts on obsidian, which gets replaced.
\ is a line break, making the text go to the next line.

### Example
In the example below, > gets ignored and replaced.

```
>test1
>test2
>test3
>test4 \test5 \test6
>test7

>test8 \Test9 \Test10 \Test11
```
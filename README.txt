idoc_split
 
Created by Eric Hyatt
Last updated: 11/30/2018
_______________________________________________________________________________

This tool will seperate the lines of idocs that are placed in a specified 
folder (should be C:\Program Files\idoc_split\uploaded-docs), which will open 
in an explorer window at runtime.

To install:
Everythinhg should be in the 'idoc_search-dist' directory.

1) Create a folder under 'C:\Program Files\' named 'idoc_split'

2) Place the 'idoc_split-dist' in the new 'idoc_split' folder 

3) Copy the 'Output' and 'uploaded-docs' folders from the 'idoc_split-dist' folder and place them in the 'idoc_split' folder

4) Place the 'idoc_split - Shortcut' where ever you would like. This is what will be used to run the program

5) You're all set! Run the program by double clicking the shortcut. 

_______________________________________________________________________________
To change the output file location:
You must edit the FILE_PATH.json file.
DO NOT UPDATE 'base_dir' OR 'output_dir' UNLESS YOU KNOW WHAT YOU'RE DOING
To have the program output to somewhere other that the output_dir, 
enter an absolute path to a directory in the quotations next to the
'alt_output' option bellow. 
If there is an issue with the path you've entered the program will place
the output file in the 'output_dir' directory
PLEASE CHANGE THE 'alt_output' OPTION BACK WHEN YOU'RE DONE 
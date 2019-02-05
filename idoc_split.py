# Last update: 12/3/18

import os
import sys
import subprocess
import json
from datetime import date


if __name__ == "__main__":

    file_count = 0
    # change cwd to location script was opened from
    os.chdir(sys.path[0])
    cwd = os.getcwd()

    try:
        with open('.\\FILE_PATH.json') as path_file:
            path_data = json.load(path_file)

            # assign input path
            if path_data["input_dir"] != "" and os.path.isdir(path_data["input_dir"]):
                input_path = path_data["input_dir"]
            else:
                input_path = os.path.join(cwd, "Imported-docs")
                if os.path.isdir(os.path.join(cwd, "Imported-docs")):
                    pass
                else:
                    os.mkdir(input_path)

            # assign path
            if path_data["alt_output"] != "" and os.path.isdir(path_data["alt_output"]):
                output_path = path_data["alt_output"]
            else:
                output_path = path_data["output_dir"]

            path_file.close()
    except FileNotFoundError:
        if os.path.isdir(os.path.join(cwd, "Imported-docs")):
            pass
        else:
            os.mkdir(".\\Imported-docs\\")
     
        input_path = ".\\Imported-docs\\"
        output_path = ".\\Imported-docs\\"

    if os.path.isdir(input_path) is False:
        # create the directory
        os.mkdir(input_path)

    # open Imported-docs foler in explorer
    subprocess.call('explorer {}'.format(input_path))

    os.system('cls')
    print("Place the idocs you would like formted in the 'Imported-docs' folder.")
    os.system('pause')

    # directory already exists
    file_list = []
    for fname in os.listdir(input_path):
        path = os.path.join(input_path, fname)
        if os.path.isdir(path):
            # skip directories
            continue
        else:
            file_list.append(fname)

    if len(file_list) == 0:
        print("No files found in {}\\".format(input_path))
    else:
        print('Documents found:')
        for file in file_list:
            print(file)

            file_path = os.path.join(input_path, file)

            # check that this is a txt doc
            if file_path[-3:].lower() == 'txt' or file_path[-3:].lower() == 'int':
                file_count += 1

                with open(file_path, 'r') as myfile:
                    data = myfile.read()

                string = data

                formated_doc = ''
                idoc = string.split('~')

                for x in idoc:
                    # remove trailing blanks
                    try:
                        while x[-1] == ' ':
                            x = x[:-1]
                    except IndexError:
                        pass

                    # check for blank lines
                    if x != '':
                        x = x + '~' + '\n'
                        formated_doc = formated_doc + x

            # export new file
                if os.path.isdir(output_path) is False:
                    output_path = cwd + "\\Imported-docs\\"

                #PROMPT FOR OUTPUT NAME
                default_name = date.today()
                if file_count <= 1:
                    default_name = "idoc_split_" + default_name.strftime('%m-%d-%Y')
                else:
                    default_name = "idoc_split_" + default_name.strftime('%m-%d-%Y') + ("_") + str(file_count)
                print('\n[{}]'.format(default_name))

                file_name = input("Enter a name for your file,\n"
                                  "or use the [default] shown above.\n") or default_name
                # check file extrnsion
                file, file_ext = os.path.splitext(file_name)
                if file_ext != ".txt":
                    file_name = file + ".txt"

                text_file = open(os.path.join(output_path, file_name), "w")
                text_file.write(formated_doc)
                text_file.close()

            else:
                print("There was an issue reading the file. Make sure the file extension is either .txt or .int.")

        print("\nYour formated idocs will be in the '{}' folder.".format(output_path))
        print("Please remove the idocs from the 'Imported-docs' folder.")
        os.system("pause")

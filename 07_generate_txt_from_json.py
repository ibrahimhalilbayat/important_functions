'''
Converting json files to txt files in YOLO format 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
Steps:
    1- Save this python file 
    2- Change 'my_path' variable 
    3- Change the label names and label IDs
'''

import json
from os import listdir, chdir
from os.path import isfile, join

my_path = ""

chdir(my_path)
onlyfiles = [f for f in listdir(my_path) if isfile(join(my_path, f))]

for file_name in onlyfiles:
    if file_name.endswith(".json"):
        with open(file_name) as f:
            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError as e:
                print(f"Error reading JSON from {file_name}: {e}")
                continue  

        save_name = file_name.split(".json")[0] + ".txt"

        save_file = open(save_name, "w")

        print(save_name)
        im_h = data["imageHeight"]
        im_w = data["imageWidth"]
        shapes = data["shapes"]
        for shape in shapes:
            label = shape["label"]
            p1, p2 = shape["points"]

            if label == "lotr":
                etiquette = 0
            elif label == "frodo":
                etiquette = 1
            else:
                etiquette = -1

            x1, y1 = p1
            x2, y2 = p2

            w = abs(x1 - x2)
            h = abs(y1 - y2)
            x_c = abs((x1 + x2) / 2)
            y_c = abs((y1 + y2) / 2)

            w = w / im_w
            h = h / im_h
            x_c = x_c / im_w
            y_c = y_c / im_h

            print(etiquette, x_c, y_c, w, h, file=save_file)

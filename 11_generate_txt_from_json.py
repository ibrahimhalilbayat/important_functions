'''
Converting json files to txt files in YOLO format 
by 
Dark Lord İbrahim Halil BAYAT
Fearless, Nameless, Formless and other -less stuff

-----------------------------------------------------
Steps:
    1- Save this python file 
    2- Change 'THE_PATH' variable 
    3- Change the label names based on IDs
    4- Go and have a happy life
'''

import json
import os
import base64
from PIL import Image

def convert_txt_to_json(txt_file_path):
    with open(txt_file_path, 'r') as txt_file:
        lines = txt_file.readlines()

    image_path = txt_file_path.split('.')[0] + ".png"
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Get image dimensions
    with Image.open(image_path) as img:
        image_width, image_height = img.size

    data = {
        "version": "3.16.7",
        "flags": {},
        "shapes": [],
        "imagePath": os.path.basename(image_path),
        "imageData": image_data,
        "imageHeight": image_height,
        "imageWidth": image_width,
        "lineColor": [0, 255, 0, 128],
        "fillColor": [255, 0, 0, 128]
    }

    for line in lines:
        values = line.strip().split()

        if len(values) < 5:
            print(f"Skipping invalid line: {line}")
            continue

        try:
            label_id = int(values[0])
            x_c = float(values[1])
            y_c = float(values[2])
            w = float(values[3])
            h = float(values[4])
        except ValueError as e:
            print(f"Error processing line: {line}\n{e}")
            continue

        x1 = int((x_c - w / 2) * data["imageWidth"])
        y1 = int((y_c - h / 2) * data["imageHeight"])
        x2 = int((x_c + w / 2) * data["imageWidth"])
        y2 = int((y_c + h / 2) * data["imageHeight"])

        shape = {
            "label": "elf" if label_id == 0 else None,
            "line_color": None,
            "fill_color": None,
            "points": [[x1, y1], [x2, y2]],
            "shape_type": "rectangle",
            "flags": {}
        }

        data["shapes"].append(shape)

    json_file_path = txt_file_path.split('.')[0] + ".json"
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)

if __name__ == "__main__":
    THE_PATH = ''
    for txt_file in os.listdir(THE_PATH):
        if txt_file.endswith('.txt'):
            if txt_file.replace('.txt', '.png') in os.listdir(THE_PATH):
                txt_file_path = os.path.join(THE_PATH, txt_file)
                convert_txt_to_json(txt_file_path)

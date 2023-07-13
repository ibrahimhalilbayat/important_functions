import json
import base64
from PIL import Image
import os

def get_image_info(image_path):
	with Image.open(image_path) as image:
		width, heigth =image.size
	with open(image_path, "rb") as image_file:
		encoded_image_data = base64.b64encode(image_file.read()).decode("utf-8")
	return width, heigth, encoded_image_data

def parse_txt_line(line):
	tokens=line.strip().split()
	return {
		'etiquette': int(tokens[0]),
		'x_c' : float(tokens[1]),
		'y_c' : float(tokens[2]),
		'w' : float(tokens[3]),
		'h' : float(tokens[4])
	}

def read_txt_file(input_txt_path):
	data = []
	with open(input_txt_path,'r') as file:
		for line in file:
			if line.strip():
				parsed_data = parse_txt_line(line)
				data.append(parsed_data)
	return data

def convert_data_to_shapes(data,im_w, im_h):
	shapes = []
	labels = ['class_1', 'class_2', 'class_3', 'class_4', 'class_5', 'class_6']

	for item in data:
		x_c, y_c, w, h= item['x_c']*im_w, item['y_c']*im_h, item['w']*im_w, item['h']*im_h
		x1 = x_c - w / 2
		y1 = y_c - h / 2
		x2 = x_c + w / 2
		y2 = y_c + h /2

		shape = {
			"label": labels[item['etiquette']],
			"points": [[x1,y1], [x2,y2]],
			"group_id" :None,
			"shape_type": "rectangle",
			"flags":{}
		}			
		shapes.append(shape)
	return shapes

def create_json_file (output_json_path, shapes,image_path,image_data,image_width,image_heigth):
	json_data = {
		"version":"4.6.0",
		"flags":{},
		"shapes":shapes,
		"imagePath":image_path,
		"imageData":image_data,
		"imageHeigth": image_width,
		"imageWidth": image_heigth
	}
	with open(output_json_path, 'w') as file:
		json.dump(json_data, file, indent=4)


for file in os.listdir('detect'):
	if file.split('.')[1] == 'txt':
		input_txt_path="detect/" + file

		output_json_path='detect/' + file.split('.')[0] + '.json'
		print("FILE: ", file)

		if file.split('.')[0] + '.jpeg' in os.listdir('detect'):
			image_path='detect/' +  file.split('.')[0] + '.jpeg'
		
		elif file.split('.')[0] + '.jpg' in os.listdir('detect'):
			image_path='detect/' +  file.split('.')[0] + '.jpg'
		
		else:
			image_path='detect/' +  file.split('.')[0] + '.png'



		#gets image information
		image_width, image_heigth, image_data = get_image_info(image_path)

		#read data from txt file
		data = read_txt_file(input_txt_path)

		#convert data to shapes
		shapes=convert_data_to_shapes(data,image_width,image_heigth)

		#create json file 
		create_json_file(output_json_path,shapes,image_path,image_data,image_width,image_heigth)

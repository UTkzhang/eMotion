from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json

models = {}

def clarifai_init():
	global app	
	app = ClarifaiApp(api_key="d1b1f196d1c547b3bef7bddfde297042")

def train_model(model_id, train_data, classifiers):
	global app	
	global models
	
	if model_id in models.keys():
		app.models.delete(model_id=model_id)

	for data in train_data:
		if data["type"] == "url":
			app.inputs.create_image_from_url(url=data["image"], concepts=data["concepts"], not_concepts=data["not_concepts"], allow_duplicate_url=True)
		elif data["type"] == "file":
			app.inputs.create_image_from_filename(filename=data["image"], concepts=data["concepts"], not_concepts=data["not_concepts"], allow_duplicate_url=True)
	model = app.models.create(model_id=model_id, concepts=classifiers)
	model = model.train()

	models[model_id] = model

def clarifai_predict(model_id, query):
	global models
	if model_id not in models.keys():
		models[model_id] = app.models.get(model_id)
	if query["type"] == "url":
		return models[model_id].predict_by_url(url=query["image"])
	elif query["type"] == "file":
		return models[model_id].predict_by_filename(filename=query["image"])
	return None


def clarifai_wipe():
	global app
	app.models.delete_all()

if __name__ == "__main__":
	clarifai_init()
	clarifai_wipe()
	
	#import a few labelled images
	train_data = []

	for i in range(18, 39):
		train_data.append({
			"type" : "file",
			"image": "/home/linaro/Desktop/Googo/training-data/s1/opencv_frame_{}.jpg".format(i),
			"concepts": ["crush"],
			"not_concepts": ["root beer", "sprite"]
		})
	
	for i in range(9, 23):
		train_data.append({
			"type" : "file",
			"image": "/home/linaro/Desktop/Googo/training-data/s2/opencv_frame_{}.jpg".format(i),
			"concepts": ["root beer"],
			"not_concepts": ["crush", "sprite"]
		})
	
	for i in range(0, 18):
		train_data.append({
			"type" : "file",
			"image": "/home/linaro/Desktop/Googo/training-data/s3/opencv_frame_{}.jpg".format(i),
			"concepts": ["sprite"],
			"not_concepts": ["root beer", "crush"]
		})
	
	
	classifiers = ["crush", "root beer", "sprite"]

	train_model("drinks", train_data, classifiers)

	print json.dumps(clarifai_predict("drinks", {"type": "file", "image": "/home/linaro/Desktop/Googo/opencv_frame_0.jpg"}), indent=2)
	

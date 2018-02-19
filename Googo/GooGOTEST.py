from flask import Flask
from flask_assistant import Assistant, ask, tell
from imageRecog import *

import serial
import cv2
import time
import requests
import json
import ast

inHand = "Nothing"

#camera functions
def save_image():
	camera_port=0
	ramp_frames = 30
	camera = cv2.VideoCapture(camera_port)

	for i in xrange(ramp_frames):
		temp = get_image(camera)
	camera_capture = get_image(camera)
	file = "/home/linaro/Desktop/image.jpg"
	cv2.imwrite(file, camera_capture)

	del(camera)

def get_image(cam):
	retval, im = cam.read()
	return im

#start of flask app
app = Flask(__name__)

assist = Assistant(app, '/')


@assist.action("Default Welcome Intent")
def default():
	inHand = "Nothing"
	return ask("Hi, I am Google E motion!")

@assist.action("bringObject", mapping={'Object': 'Object'})
def bringObject(Object):
	global inHand
	time.sleep(5)
	inHand = str(Object)
	return ask("The" + inHand + " has been picked up.")

@assist.action("putObject", mapping={'Object': 'Object'})
def putObject(Object):
	global inHand
	if (Object == inHand):
		inHand = "Nothing"	
	else: return ask("I am not holding " + str(Object))
	return ask("The " + str(Object) + " has been put down.")

@assist.action("turnAround")
def turnAround():
	time.sleep(1)
	return ask("Oh, hello there.")

@assist.action("comeBack")
def comeBack():
	time.sleep(2)
	return ask("Don't worry, I am right here.")

@assist.action("backward")
def backward():
	time.sleep(1)
	return ask("Done")

@assist.action("forward")
def forward():
	time.sleep(1)
	return ask("Done")

@assist.action("turnLeft")
def turnLeft():
	time.sleep(1)
	return ask("Done")

@assist.action("turnRight")
def turnRight():
	time.sleep(1)
	return ask("Done")

@assist.action("patMe")
def patMe():
	time.sleep(2)
	return ask("There, there, are you alright?")

@assist.action("captureImage")
def captureImage():
	save_image()
	r = clarifai_predict("drinks", {"type": "file", "image": "/home/linaro/Desktop/image.jpg"})
	print (json.dumps(r, indent = 2))
	return ask("I see " + r["outputs"][0]["data"]["concepts"][0]["name"] + " in front of me!")

if __name__ == "__main__":
	clarifai_init()
	app.run(debug=True)


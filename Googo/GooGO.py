from flask import Flask
from flask_assistant import Assistant, ask, tell, event
from imageRecog import *

import serial
import cv2
import time
import requests
import json

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

ser = serial.Serial("/dev/ttyUSB1", 9600)

@assist.action("Default Welcome Intent")
def default():
	inHand = "Nothing"
	ser.write(b'i') #initialize
	return ask("Hi, I am Google E motion!")

@assist.action("bringObject", mapping={'Object': 'Object'})
def bringObject(Object):
	global inHand
	ser.write(b'f')	#move forward
	time.sleep(5)
	save_image()
	r = clarifai_predict("drinks", {"type": "file", "image": "/home/linaro/Desktop/image.jpg"})
	inHand = str(Object)

	if r["outputs"][0]["data"]["concepts"][0]["name"] != Object.lower():
		ser.write(b'l') #turn right
		time.sleep(5)
		save_image()
	else: 
		ser.write(b't') #pick up
		time.sleep(5)
		return ask("picked up")
		
	print(inHand)
	ser.write(b't')
	return ask("picked up")
	
@assist.action("putObject", mapping={'Object': 'Object'})
def putObject(Object):
	global inHand
	if (Object == inHand):
		ser.write('d') #put down
		inHand = "Nothing"	
	else: return ask("I am not holding " + str(Object))
	time.sleep(3)
	return ask("The " + str(Object) + " has been put down.")

@assist.action("turnAround")
def turnAround():
	ser.write("o") #turn 180 degrees
	time.sleep(1)
	return ask("Oh, hello there.")

@assist.action("comeBack")
def comeBack():
	ser.write("q") #turn and move back to origin
	time.sleep(2)
	return ask("Don't worry, I am right here.")

@assist.action("backward")
def backward():
	ser.write("y") #move backwards a bit
	time.sleep(1)
	return ask("Done")

@assist.action("forward")
def forward():
	ser.write("x") #move forwards a bit
	time.sleep(1)
	return ask("Done")

@assist.action("turnLeft")
def turnLeft():
	ser.write("l") #turn left 90 degrees
	time.sleep(1)
	return ask("Done")

@assist.action("turnRight")
def turnRight():
	ser.write("r") #turn right 90 degrees
	time.sleep(1)
	return ask("Done")

@assist.action("patMe")
def patMe():
	ser.write(b'p') #pat me
	time.sleep(2)
	return ask("There, there, are you alright?")

@assist.action("captureImage")
def captureImage():
	save_image()
	r = clarifai_predict("drinks", {"type": "file", "image": "/home/linaro/Desktop/image.jpg"})
	print (json.dumps(r, indent = 2))
	return ask("I see " + r["outputs"][0]["data"]["concepts"][0]["name"] + " in front of me!")

@assist.action("userDead")
def userDead():
	ser.write(b'5')
	time.sleep(2)
	return ask('Rest in peace')

@assist.action("userLove")
def userLove():
	ser.write(b'h')
	time.sleep(2)
	return ask('I love you too')

@assist.action("resetMe")
def resetMe():
	ser.write("i") #reset
	return ask("Done reset")


if __name__ == "__main__":
	clarifai_init()
	app.run(debug=True)

'''
@assist.action("captureImage")
def captureImage():
	r = ""
	save_image()
	r = json.loads(post(r).text)["data"]
	print(r[0]["name"])
	if (r[0]["name"] == "Coca Cola" or r[0]["name"] == "cup" or r[0]["name"] == "bottle" or r[0]["name"] == "orange soda"):
		box = r[0]["box"]
		x_diff = box[3] - box[1]
		x_center = box[1] + x_diff/2
		x_offset = x_center - 320
		if (x_diff < 0):
			ser.write(b'x')
			x_diff = -x_diff
			ser.write(x_diff)
		else:
			ser.write(b'y')
		
		if (x_offset >= 0):
			ser.write(b'l')
			ser.write(x_offset/5)
		else:
			ser.write(b'r')
			x_offset = -x_offset
			ser.write(x_offset/5)
		
	return question("image has been captured and uploaded")

#POST function
def post(r):
	with open("/home/linaro/Desktop/image.jpg", "rb") as f:
		data = f.read()
		image = data.encode("base64")
		r = requests.post("http://34.201.113.132:3000/post_data", data={"img":image})
		return r
'''

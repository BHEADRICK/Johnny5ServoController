#!/usr/bin/env python3

from adafruit_servokit import ServoKit
from time import sleep
import numpy as np
from multiprocessing import Process
from munch import *
import sys

kit = ServoKit(channels=16)

servos = {

	'rightBrowTilt': {
	'id':15,
	'home': 80,
	'max': 80,
	'min': 0,
	'counter': False,
	'current': 80

	},
	'leftBrowTilt': {
	'id':14,
	'home': 60,
	'min': 60,
	'max': 150,
	'counter': True,
	'current': 60
	},
	'rightBrowRotate': {
	'id':13,
	'home': 80,
	'counter': True,
	'current': 80,
	'min':0,
	'max': 100

	},
	'leftBrowRotate': {
	'id':10,
	'home': 20,
	'counter': False,
	'current': 20,
	'min': 15,
	'max': 130
	},
	'noseRotate': {
	'id':12,
	'home': 30,
	'current':30,
	'counter': False,
	'min':0,
	'max':80,

	},
	'nosePivot': {
	'id':11,
	'counter': True,
	'home': 80,
	'current': 80,
	'min': 60,
	'max': 110
	},
	'leftEyeX': {
	'id': 0,
	'home': 80,
	'current': 80,
	'min':0 ,
	'max': 160,
	'counter': True
	},
	'leftEyeY': {
	'id': 1,
	'home': 30,
	'current': 30,
	'min': 0,
	'max': 60,
	'counter': False
	},
	'leftEyeIris':{
	'id':2,
	'home':0,
	'current':0,
	'counter':True,
	'min':0,
	'max':50
	},
	'rightLowerEyeFlap': {
	'id':9,
	'home': 180,
	'current': 180,
	'min': 70,
	'max':180,
	'counter': True
	},
	'leftLowerEyeFlap': {
	'id':8,
	'home': 0,
	'current': 0,
	'min': 0,
	'max':90
	}
}



def homeAll():
	print('homing...')
	for key in servos:
		kit.servo[servos[key]['id']].angle = servos[key]['home']
		sleep(.1)
def setAngle(servo, angle, steps):
	control = np.arange(0, angle, angle/steps)
	for x in range(len(control)):
		kit.servo[servo].angle = control[x]
		sleep(0.01)


def smoothAngle(servo, targetPosition, currentPosition =0):
	r = targetPosition - currentPosition
	angles = np.array( (range(80)) [0::10]) - 90
	m = ( np.sin( angles * np.pi/ 180. ) + 1 ) /2

	for mi in np.nditer(m):
		pos = currentPosition + mi*r
		# print “pos: “, pos
		kit.servo[servo].angle = pos
		sleep(0.05)

def moveServo(servoKey, angle, smooth = False):
	servo = DefaultMunch.fromDict(servos[servoKey])
	if(servo.counter):
		dest = servo.current - angle
	else:
		dest = servo.current + angle

	if dest<servo.min:
		dest = servo.min
	if dest>servo.max:
		dest = servo.max
	print("moving servo" + servoKey + " to " + str(dest))
	if smooth:
		smoothAngle(servo.id, dest, servo.current)
	else:
		kit.servo[servo.id].angle = dest
	servos[servoKey]['current'] = dest
def blinkWink():

	moveServo('rightBrowTilt', -90)
	moveServo('leftBrowTilt', -90)
	moveServo('rightLowerEyeFlap', 90)
	moveServo('leftLowerEyeFlap', 90)

	sleep(1)
	moveServo('rightBrowTilt', 90)
	moveServo('leftBrowTilt', 90)
	moveServo('rightLowerEyeFlap', -90)
	moveServo('leftLowerEyeFlap', -90)
	sleep(1)

	moveServo('rightBrowTilt', -90)
	moveServo('rightLowerEyeFlap', 90)

	sleep(1)
	moveServo('rightBrowTilt', 90)
	moveServo('rightLowerEyeFlap', -90)

	sleep(1)
	moveServo('leftLowerEyeFlap', 90)
	moveServo('leftBrowTilt', -90)
	sleep(1)

	moveServo('leftBrowTilt', 90)
	moveServo('leftLowerEyeFlap', -90)
	sleep(2)

def testRange(srv, start, inc=5):

	angle = start
	kit.servo[srv].angle = angle
	sleep(1)
	# kit.continuous_servo[servo].throttle = 1
	# try:
	while angle >=0 and angle <= 180:

		print("moving to angle: " + str( angle))
		kit.servo[srv].angle = angle
		angle +=inc
		sleep(1)


homeAll()
# testRange(2,80,5)
sleep(1)
moveServo('leftBrowTilt',30)
moveServo('rightBrowTilt',30)
moveServo('nosePivot',10)
moveServo('leftEyeY',60)
moveServo('noseRotate',30)
moveServo('leftLowerEyeFlap',30)
moveServo('rightLowerEyeFlap',30)

# moveServo('leftBrowRotate', 0, True)

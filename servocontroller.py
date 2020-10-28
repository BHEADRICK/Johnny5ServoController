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
	'home': 80,
	'counter': False,
	'current': 80,
	'min': 60,
	'max': 160
	},
	'noseRotate': {
	'id':12,
	'home': 80,
	'counter': False
	},
	'nosePivot': {
	'id':11,
	'counter': True,
	'home': 80,
	'current': 80,
	'min': 60,
	'max': 110
	},
	'rightEyeX': {
	'id': 0,
	'home': 80,
	'current': 80,
	'min': 45,
	'max': 125,
	'counter': True
	},
	'rightEyeY': {
	'id': 1,
	'home': 45,
	'current': 45,
	'min': 0,
	'max': 110,
	'counter': False
	},
	'rightEyeIris':{
	'id':2,
	'home':0,
	'current':0,
	'counter':True
	}
}


# kit.servo[servo].angle = 60
# sleep(1)
# kit.servo[servo].angle = 80
# sleep(1)
	# kit.servo[servo].angle = 60
#
# kit.servo[4].angle = 80
# kit.servo[5].angle = 80
#
# kit.servo[6].angle = 80
# kit.servo[7].angle = 80

def homeAll():
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
	print("moving servo to " + str(dest))
	if smooth:
		smoothAngle(servo.id, dest, servo.current)
	else:
		kit.servo[servo.id].angle = dest
	servos[servoKey]['current'] = dest

# import rospy
# from std_msgs.msg import Float32

homeAll()
# sleep(3)
# moveServo('nosePivot', 30)
# sleep(1)
# moveServo('rightEyeX', 40)
# sleep(1)
# moveServo('rightEyeX', -80)
# sleep(1)
# moveServo('rightEyeY', 50)
# sleep(1)
# moveServo('rightEyeY', -100)
# sleep(1)
# moveServo('rightBrowRotate',15)
# moveServo('leftBrowRotate',15)
# sleep(.2)
# moveServo('rightBrowRotate',-15)
# moveServo('leftBrowRotate',-15)
# sleep(.2)
# moveServo('rightBrowRotate',15)
# moveServo('leftBrowRotate',15)
# sleep(.2)
# moveServo('rightBrowRotate',-15)
# moveServo('leftBrowRotate',-15)
# # #
# sleep(3)
# homeAll()

# kit.servo[1].angle = 80
#
# servo = 1
# angle = 80
# try:
# 	while angle >0:
# 		angle -=5
# 		print("moving to angle: " + str( angle))
# 		kit.servo[servo].angle = angle
#
# 		sleep(1)
# #
# except KeyboardInterrupt:
# 	kit.continuous_servo[servo].throttle = 0

# def func1():
# 	smoothAngle(6,120,60)

# def func2():
# 	smoothAngle(7,120,60)

# p1 = Process(target = func1)
# p2 = Process(target = func2)
# p1.start()
# p2.start()

#
#

# print("jerky movement")
# sleep(1)
# kit.servo[1].angle=60
# sleep(1)
# kit.servo[1].angle=0
# sleep(2)

# print("slow movement")
# setAngle(1,60, 50)
# sleep(1)
# kit.servo[1].angle=0
# sleep(2)

# print("smooth movement")
# smoothAngle(1,60)
# sleep(1)
# smoothAngle(1,0,60)

# sleep(3)
# smoothAngle(2,50,80)
# smoothAngle(3, 110, 80)

# sleep(2)
# smoothAngle(4,60,80)
# smoothAngle(5,60,80)

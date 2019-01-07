#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 02:14:09 2018

@author: kia
"""
import pyscreenshot as ImageGrab
from PIL import ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
	replayBtn = (342,398)
	dinosaur = (171,402)
	
	
def restartGame():
	pyautogui.click(Cordinates.replayBtn)
	
	
def pressSpace():
	pyautogui.keyDown('space')
	time.sleep(0.05)
	print("Jump")
	pyautogui.keyUp('space')
	
	
def imageGrab():
	box = (Cordinates.dinosaur[0]+60,Cordinates.dinosaur[1],Cordinates.dinosaur[0]+100,Cordinates.dinosaur[1]+30)
	image = ImageGrab.grab(box)
	grayImage = ImageOps.grayscale(image)
	a = array(grayImage.getcolors())
	return a.sum()
	
def main():
	restartGame()
	while True:
		if (str(imageGrab()) != "1447"):
			pressSpace()
			#print("Jump")
			time.sleep(0.1)
			



main()
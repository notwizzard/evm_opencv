import cv2
from datetime import datetime
import numpy as np
from enum import Enum
from effects import *
import time


class Effect(Enum):
    NORMAL = normal
    GRAY = gray
    SQUARES = squares


class Capturer:

    def __init__(self, channel: int, width: int = 1280, height: int = 720):
        self.capture = cv2.VideoCapture(channel)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    @staticmethod
    def check_channels():
        for i in range(10):
            print(cv2.VideoCapture(i).isOpened(), i)

    def display(self, fps: int = 30, effect: Effect = Effect.NORMAL) -> None:
        if not self.capture.isOpened():
            print("No camera available")
            return 
        
        frames = 0
        ftime = time.time()
        while(True):
            frames += 1
            if frames == 100:
                with open('fps.log', 'a') as file:
                    file.write(str(frames / float(time.time() - ftime)) + '\n')
                frames = 0
                ftime = time.time()
            rt0 = time.time()
            pt0 = time.process_time()
            result, image = self.capture.read()

            if not result:
                print("Error while capturing frame")
                break
            image = self.effect_image(image, effect)
            cv2.imshow('Default camera', image)
            if cv2.waitKey(1) == ord('q'):
                break
            rt1 = time.time()
            pt1 = time.process_time()

            self.write_time(rt0, rt1, pt0, pt1)


    def effect_image(self, image, effect: Effect):
        return effect(image)

    
    def write_time(self, rt0, rt1, pt0, pt1):
        with open('time.log', 'a') as file:
            file.write(str(rt1 - rt0) + ' ' + str(pt1 - pt0) + '\n')

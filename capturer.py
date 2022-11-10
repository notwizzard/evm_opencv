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
            pt0 = time.process_time_ns()
            result, image = self.capture.read()
            pt1 = time.process_time_ns()
            rt1 = time.time()
            if not result:
                print("Error while capturing frame")
                break
            rt2 = time.time()
            pt2 = time.process_time_ns()
            image = self.effect_image(image, effect)
            pt3 = time.process_time_ns()
            rt3 = time.time()
            cv2.imshow('Default camera', image)
            pt4 = time.process_time_ns()
            rt4 = time.time()
            if cv2.waitKey(1) == ord('q'):
                break
            pt5 = time.process_time_ns()
            rt5 = time.time()

            self.write_time(rt0, rt1, rt2, rt3, rt4, rt5, pt0, pt1, pt2, pt3, pt4, pt5)

            


    def effect_image(self, image, effect: Effect):
        return effect(image)

    
    def write_time(self, rt0, rt1, rt2, rt3, rt4, rt5, pt0, pt1, pt2, pt3, pt4, pt5):
        with open('get_real.log', 'a') as file:
            file.write(str(rt1 - rt0) + '\n')
            
        with open('effect_real.log', 'a') as file:
            file.write(str(rt3 - rt2) + '\n')

        with open('display_real.log', 'a') as file:
            file.write(str(rt4 - rt3) + '\n')
        
        with open('wait_real.log', 'a') as file:
            file.write(str(rt5 - rt4) + '\n')

        with open('all_real.log', 'a') as file:
            file.write(str(rt5 - rt0) + '\n')

        
        with open('get_proc.log', 'a') as file:
            file.write(str(pt1 - pt0) + '\n')
            
        with open('effect_proc.log', 'a') as file:
            file.write(str(pt3 - pt2) + '\n')

        with open('display_proc.log', 'a') as file:
            file.write(str(pt4 - pt3) + '\n')
        
        with open('wait_proc.log', 'a') as file:
            file.write(str(pt5 - pt4) + '\n')

        with open('all_proc.log', 'a') as file:
            file.write(str(pt5 - pt0) + '\n')

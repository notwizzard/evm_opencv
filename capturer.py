import cv2
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
        read_process_time = 0
        read_real_time = 0
        effect_process_time = 0
        effect_real_time = 0
        display_process_time = 0
        display_real_time = 0
        while(True):
            frames += 1
            if frames == 2000:
                print("READ:", read_process_time, " ", read_real_time)
                print("EFFECT:", effect_process_time, " ", effect_real_time)
                print("DISPLAY:",display_process_time, " ", display_real_time)
                frames = 0
                print("FPS", frames / float(time.time() - ftime))
            rt0 = time.time()
            pt0 = time.process_time()
            result, image = self.capture.read()
            rt1 = time.time()
            pt1 = time.process_time()
            read_process_time += pt1 - pt0
            read_real_time += rt1 - rt0
            if not result:
                print("Error while capturing frame")
                break
            image = self.effect_image(image, effect)
            rt2 = time.time()
            pt2 = time.process_time()
            effect_process_time += pt2 - pt1
            effect_real_time += rt2 - rt1
            cv2.imshow('Default camera', image)
            rt3 = time.time()
            pt3 = time.process_time()
            display_process_time += pt3 - pt2
            display_real_time += rt3 - rt2
            if cv2.waitKey(1) == ord('q'):
                break



    def effect_image(self, image, effect: Effect):
        return effect(image)

    
    def write_time(self, fps, read_p, read_r, effect_p, effect_r, display_p, display_r):
        with open('read.log', 'a') as file:
            file.write(str(read_r) + ' ' + str(read_p) + '\n')
        with open('effect.log', 'a') as file:
            file.write(str(effect_r) + ' ' + str(effect_p) + '\n')
        with open('display.log', 'a') as file:
            file.write(str(display_r) + ' ' + str(display_p) + '\n')
        with open('fps.log', 'a') as file:
            file.write(str(fps) + ' ' + str(display_p) + '\n')

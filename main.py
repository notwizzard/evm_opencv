import cv2
from capturer import Capturer, Effect
from time import sleep


Capturer.check_channels()
capturer = Capturer(0)
sleep(2)
capturer.display(fps=1000, effect=Effect.SQUARES)

cv2.destroyAllWindows()

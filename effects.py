import cv2
import numpy as np

def normal(image):
    return image

def gray(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def squares(image):
    cell_size = 8
    width, height = 720, 1280
    black_background = np.zeros((height, width, 3), np.uint8)
    smaller_image = cv2.resize(image, (height // cell_size, width // cell_size))

    for i in range(width // cell_size):
        for j in range(height // cell_size):
            color = smaller_image[i, j]
            R = int(color[0])
            G = int(color[1])
            B = int(color[2])

            current_position = (j * cell_size + cell_size, i * cell_size)

            cv2.circle(black_background, current_position, 5, (R, G, B), 2)

    return black_background


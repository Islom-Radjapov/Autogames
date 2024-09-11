import pyautogui
import time
from PIL import Image
image = pyautogui.screenshot(r"C:\Users\islom\PycharmProjects\gameHamster\res.png")
im = Image.open(r"C:\Users\islom\PycharmProjects\gameHamster\res.png")

def img_crop():
    box = {
            'x0': 1111,
            'x1': 1115,
            'y0': 764,
            'y1': 800
    }
    img = Image.open(r"C:\Users\islom\PycharmProjects\gameHamster\res.png")
    h, w = img.size
    print(img.size)
    return img.crop((box['x1']*h, box['y1']*w, box['x0']*h, box['y0']*w))

im = img_crop()
im.save(r"C:\Users\islom\PycharmProjects\gameHamster\res.png")
im.show(r"C:\Users\islom\PycharmProjects\gameHamster\res.png")
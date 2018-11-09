import sys
from time import sleep

import keyboard
from PIL import Image, ImageGrab

from baidu import BaiDuAPI


def screenShot():
    # 监听按压
    # key = keyboard.read_hotkey()
    if keyboard.wait(hotkey='f1') == None:
        if keyboard.wait(hotkey='ctrl+c') == None:
            sleep(0.01)
            im = ImageGrab.grabclipboard()
            im.save(
                r'imageGrab.png')
    else:
        print('请按F1, Ctrl+C实现识别')


if __name__ == '__main__':

    baiduapi = BaiDuAPI(r'password.ini')

    for _ in range(sys.maxsize):

        screenShot()

        allTexts = baiduapi.picture2Text(r'imageGrab.png')

        print(allTexts)

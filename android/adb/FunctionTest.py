import os
import time


def runADB(cmd, wait_time=1):
    os.system(cmd)
    time.sleep(wait_time)


def listDev():
    runADB("adb devices", 0)


def putFile(local_path, remote_path):
    cmd = "adb push {local_path} /sdcard/{remote_path}"
    runADB(cmd.format(**locals()))


def getFile(remote_path, local_path):
    cmd = "adb pull /sdcard/{remote_path} {local_path}"
    runADB(cmd.format(**locals()))


def installApk(local_apk_path):
    cmd = "adb install {local_apk_path}"
    runADB(cmd.format(**locals()))


def tap(x, y,  wait_time=1):
    cmd = "adb shell input tap {x} {y}"
    runADB(cmd.format(**locals()), wait_time)


def longTap(x, y):
    swipe(x, y, x, y, 1000)


def swipe(startX, endX, startY, endY, timeToSwipe):
    cmd = "adb shell input swipe {startX} {startY} {endX} {endY} {timeToSwipe}"
    runADB(cmd.format(**locals()))


def swipeUp():
    swipe(100, 400, 100, 100, 300)


def swipeDown():
    swipe(100, 100, 100, 400, 300)


def keyevent(num):
    cmd = "adb shell input keyevent {num}"
    runADB(cmd.format(**locals()))


def back():
    keyevent(4)


def home():
    keyevent(3)


def enter():
    keyevent(66)


def esc():
    keyevent(111)


def intent(intent_name, paras):
    cmd = "adb shell am start -a {intent_name} -d {paras}"
    runADB(cmd.format(**locals()))


def call(phone):
    intent("android.intent.action.CALL", phone)


def web(url):
    intent("android.intent.action.VIEW", url)


# {包名}/.{主Activity名}
def launch(app):
    cmd = "adb shell am start -n {app} "
    runADB(cmd.format(**locals()))


def listPkg():
    cmd = "adb shell pm list package "
    runADB(cmd)


def screenshot(filename):
    cmd = "adb shell screencap /sdcard/{filename}.png "
    runADB(cmd.format(**locals()))


def screenshotToPC(local_path, filename):
    screenshot(filename)
    getFile("/sdcard/"+filename+".png", local_path)
    cmd = "adb shell rm /sdcard/{filename}.png"
    runADB(cmd.format(**locals()))


def ershida():
    # tap(360, 930)  # 人机
    # loop
    tap(360, 980, 6)  # 开始

    tap(360, 710, 6)  # A
    tap(360, 840, 6)  # B
    tap(360, 710, 6)  # A
    tap(360, 840, 6)  # B
    tap(360, 710, 6)  # A
    tap(360, 930, 6)  # 继续挑战

    # tap(360, 710, 5)  # A
    # tap(360, 840, 5)  # B
    # tap(360, 980, 5)  # C
    # tap(360, 1120, 5)  # D


def ershida10():
    # tap(360, 930, 3)  # 人机
    for i in range(4):
        print(i)
        ershida()


if __name__ == '__main__':
    runADB("adb version", 0)
    runADB("adb connect 127.0.0.1:62001")
    ershida10()

# from PhoneADB import *
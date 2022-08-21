import pyautogui
import time
import pyperclip


def get_the_estimate(adress):
    refresh_page()
    time.sleep(1)
    pyperclip.copy("1234567890")
    pyautogui.scroll(1000)
    click_text_box()
    pyautogui.write(adress)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(0.5)
    copy_value()
    estimate = pyperclip.paste()

    return estimate


def click_text_box():
    text_box_position = (565, 465)
    pyautogui.moveTo(text_box_position)
    pyautogui.click()


def copy_value():
    pyautogui.moveTo(965, 456)
    pyautogui.drag(-200, 0, 0.25, button="left")
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    time.sleep(0.1)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')


def close_estimate_window():
    window_x_position = (940, 187)
    pyautogui.moveTo(window_x_position)
    pyautogui.click()


def refresh_page():
    pyautogui.keyDown('F5')
    time.sleep(0.1)
    pyautogui.keyUp('F5')

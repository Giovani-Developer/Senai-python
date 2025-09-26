import pyautogui
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE =True

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')


pyautogui.click(x=679, y=418)

pyautogui.click(x=298, y=59)
pyautogui.write('https://meutimao.com.br')
pyautogui.press('enter')


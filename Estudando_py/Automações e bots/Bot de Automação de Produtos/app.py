import pyautogui as pg
import time
import pandas as pd, openpyxl

#Entrando no sistema
pg.press('win')
pg.write("edge")
pg.press('enter')
time.sleep(1)
pg.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pg.press('enter')


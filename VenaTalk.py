import pyautogui
import time
import cv2
import keyboard
import pytesseract
from PIL import Image
import re
import numpy as np
import pythonbible as bible
import random
import ctypes
from ctypes import wintypes

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def GetVerse():
    holyId = 0

    #book
    holyId = random.randint(1, 20)

    chapter = random.randint(1, 15)
    schapter = str(chapter)
    if len(schapter) == 1:
        holyId = int(str(holyId) + "00" + schapter)
    elif len(schapter) == 2:
        holyId = int(str(holyId) + "0" + schapter)
    else:
        holyId = int(str(holyId) + schapter)


    verse = random.randint(1, 15)
    sverse = str(verse)
    if len(sverse) == 1:
        holyId = int(str(holyId) + "00" + sverse)
    elif len(sverse) == 2:
        holyId = int(str(holyId) + "0" + sverse)
    else:
        holyId = int(str(holyId) + sverse)
    
    verse_text = ""

    try:
        verse_text = bible.get_verse_text(holyId)
        finId = holyId
    except bible.InvalidVerseError:
        JesusTakeTheBackup = random.randint(1, 3)
        if JesusTakeTheBackup == 1:
            chapter = 1
            verse = 1
            verse_text = bible.get_verse_text(1001001)
            finId = 1001001
        if JesusTakeTheBackup == 2:
            chapter = 1
            verse = 1
            verse_text = bible.get_verse_text(2001001)
            finId = 2001001
        if JesusTakeTheBackup == 3:
            chapter = 1
            verse = 1
            verse_text = bible.get_verse_text(3001001)
            finId = 3001001


    references = bible.convert_verse_ids_to_references( [finId] )
    book = references[0].book

    print(book)

    book = str(book).strip("Book.")
    book = str(book).strip("_2")
    book = str(book).strip("_1")

    return str(book) + " " + str(chapter) + ":" + str(verse) + " " + verse_text
    
def GotAKill(location):

    #Keybord block 
    for i in range(150):
        keyboard.block_key(i)
        
    for i in range(150):
        keyboard.release(i)

    #endregion

    #region Picking a random bible verse
    verse = GetVerse()
    #endregion

    #region Typing in words
    
    for i in range(150):
            keyboard.release(i)

    time.sleep(0.5)

    pyautogui.keyDown('shift')
    pyautogui.press('enter') 
    time.sleep(0.1)
    pyautogui.keyUp('shift')

    keyboard.release("shift")
    pyautogui.keyUp('shift')
    pyautogui.write(verse)  
    pyautogui.press('enter') 

    time.sleep(0.5)
    
    #endregion 

    #keyboard unblock
    keyboard.unhook_all()

    print(verse)


print("Genesis 1:1 - In the beginning God created the heavens and the earth")

ascii = ""
for i in open(r"ascii.txt").readlines():
    ascii += i
print(ascii)

print("\n")

print("Vena-Talk - by Meeyatta ")
print("Python bible verse library - pythonbible ")

print("\n")

keyboard.unhook_all()
while (True):
    time.sleep(0.6)

    img = cv2.imread(r"ILIKEMEN.png") 
    location = pyautogui.locateOnScreen(img)

    if (location != None):
        GotAKill(location)
    
    keyboard.unhook_all()





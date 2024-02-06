import random as rand
import pyautogui
import time


import pyautogui
import pytesseract


def scan(left, top, width, height):
   screenshot = pyautogui.screenshot(region=(left, top, width, height))
   screenshot = screenshot.convert('RGB')
   screenshot.save('p.jpg')

   extracted_text = pytesseract.image_to_string(screenshot)
   extracted_text = extracted_text.replace("\n", " ")
   return extracted_text

def type_text(text, delay=0):
    print(f'Typing the extracted text: {text}')
    i = 0  
    while i < len(text):
        temp = rand.randint(0,40)
        if i + temp > len(text):
           temp = len(text)-i
        while rand.randint(0,1):
           continue
        pyautogui.typewrite(text[i:i+temp])
        i = i + temp
        

time.sleep(4)
text = scan(100, 350, 1200, 200)

while 1:
   type_text(text)
   text = scan(100, 420, 1200, 50)


from os import startfile
from pyautogui import click, sleep
from keyboard import press
from keyboard import write,press_and_release




def whatsappmsg(name,message):
    
    startfile('C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    sleep(30)

   
    press_and_release('Ctrl + f')
    sleep(2)

    write(name)          # write name
    sleep(2)

    press('enter')    # click name
    sleep(2)

   
    write(message)      # write msg
    
    press('enter')   # enter

def whatscall(name):
   
    startfile('C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    
    sleep(5)

    press_and_release('Ctrl + f')
    sleep(2)

    write(name)          # write name
    sleep(2)

    press('enter')    # click name
    sleep(2)
    
    click(x=1675, y=100)   # voice call
    
    sleep(1)



def whatsVcall(name):
    
    startfile('C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe')
    
    sleep(25)

    press_and_release('Ctrl + f')
    sleep(2)

    write(name)          # write name
    sleep(2)

    press('enter')    # click name
    sleep(2)
    
    click(x=1613, y=95)   #video call
    
    

def whatschat(name):  

    startfile('C:\\Users\\dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe')

    
    sleep(25)

    
    press_and_release('Ctrl + f')
    sleep(5)

    write(name)          # write name
    sleep(2)

    press('enter')    # click name
    sleep(1)

    
  
    
    
    
    

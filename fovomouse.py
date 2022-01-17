import imp
from re import T
import time
from pynput import mouse
import pyautogui
import random
def mouse_log(x , y , button , pressed):
    if pressed == True:
        print(x , y , button , pressed)
        f=str(x)+" " +str(y)+" " +str(button)+" "+str(pressed)
        
        x=random.randint(0,100000)
        screenshot = pyautogui.screenshot( "pic/"+str(x)+'.png')
        

        file = open("file.html", "a")
        file.write (f+" "+time.ctime(time.time()) +"<br>"+ "\n""<img src=pic/{x}.png><br>" .format(x=x))
        file.close()
def mouse_start():
    with mouse.Listener(on_click = mouse_log) as lstn:
        lstn.join()


mouse_start()
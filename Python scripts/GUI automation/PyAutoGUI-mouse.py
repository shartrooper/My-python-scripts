Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.size()
Size(width=1680, height=1050)
>>> width,height=pyautogui.size()
>>> pyautogui.position() #current mouse coordinates
Point(x=1045, y=299)
>>> pyautogui.position() #current mouse coordinates
Point(x=0, y=0)
>>> pyautogui.moveTo(10,10)
>>> pyautogui.moveTo(50,20) #move the mouse to coord
>>> pyautogui.moveTo(100,120,duration=1.5) #move the mouse to coord
>>> pyautogui.moveTo(1000,120,duration=1.5) #move the mouse to coordinates with a delay
>>> pyautogui.moveRel(150,120,duration=1.5) #move the mouse relative to current position
>>> pyautogui.moveRel(0,-120) #negative also applies
>>> pyautogui.position()
Point(x=287, y=30)
>>> pyautogui.click(287,30)
>>> #The cursor clicked over the element in (287,30)
>>> pyautogui.click()
>>> #Auto click on current pos
>>> 
============================================================ RESTART: C:\Users\MARKO\Documents\Varios\Python scripts\GUI automation\spiralDraw.py ============================================================
5 second til it starts
>>> #forcing the mouse towards the upper left corner of screen will trigger FAILSAFE and stop script.
>>> pyautogui.displayMousePosition()# update current mouse position in real time on command line
Press Ctrl-C to quit.
X:  629 Y:  266 RGB: (255, 255, 255)
X:  629 Y:  266 RGB: (255, 255, 255)
X:  629 Y:  266 RGB: (255, 255, 255)
X:  629 Y:  266 RGB: (255, 255, 255)
X:  854 Y:  781 RGB: (255, 255, 255)
X: 1009 Y:  514 RGB: (255, 255, 255)

>>> 
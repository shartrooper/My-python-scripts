Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> pyautogui.screenshot()
<PIL.Image.Image image mode=RGB size=1680x1050 at 0x209A298>
>>> pyautogui.screenshot('c:\\scrnshot_example.png')
<PIL.Image.Image image mode=RGB size=1680x1050 at 0x20DB3E8>
>>> pyautogui.locateOnScreen('c\\filename.png') #Return a tuple coordinate of 4 points
>>> pyautogui.moveTo((932,336),duration=1)
>>> pyautogui.click(932,336) #got image's coordinates and click on the element
>>> '''The passed image has to perfectly represent figure dimensions otherwise wouldn't be able to find anything'''
"The passed image has to perfectly represent figure dimensions otherwise wouldn't be able to find anything"
>>> 
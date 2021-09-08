# url : https://www.coolmathgames.com/0-color-memory#immersiveModal

import pyautogui
import keyboard
import time,win32api,win32con

# Get rgb values

# while 1:
#     pyautogui.displayMousePosition()
# X:  595 Y:  554 RGB: (177, 170,36) | yellow  - 1
# X:  584 Y:  789 RGB: (177, 37, 37) | red     - 2
# X:  368 Y:  784 RGB: (40, 40, 180) | blue    - 3
# X:  371 Y:  565 RGB: (33, 103, 33) | green   - 4
#rgb value of white used in the game is greater than 190 (near the centre of the 'blink')



def check_colour_blink():
    
    global colour_count,colours,read
    
    if (pyautogui.pixel(595,554)[1]) > 190:  #yellow
        
        while (pyautogui.pixel(595,554)[1] > 190):      # while loops are used so that the list is not appended incorrectly (the function is called many times in 1 second)
            time.sleep(0.05)
        print("yellow")
        colour_count=colour_count+1
        if colour_count > len(colours):
            colours.append(1)
            # print("appended")
            read=False
    
    if (pyautogui.pixel(584,789)[1] > 190):   #red
        
        while (pyautogui.pixel(584,789)[1] > 190) :
            time.sleep(0.05)
        print("red")
        colour_count=colour_count+1
        if colour_count > len(colours):
            colours.append(2)
            # print("appended")
            read=False

    if (pyautogui.pixel(368,784)[1] > 190) :  #blue
        
        while (pyautogui.pixel(368,784)[1] > 190):
            time.sleep(0.05)
        print("blue")
        colour_count=colour_count+1
        if colour_count > len(colours):
            colours.append(3)
            # print("appended")
            read=False
    
    if (pyautogui.pixel(371,565)[1] > 150) :   #green
        
        while (pyautogui.pixel(371,565)[1] > 150):
            time.sleep(0.05)
        print("green")
        colour_count=colour_count+1
        if colour_count > len(colours):
            colours.append(4)
            # print("appended")
            read=False
    # print("return")
    return


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def clickstart():
    if (pyautogui.pixel(499,626)[0]) < 100:
        click(499,626)
    return

clickstart()
colour_count=0
read=True
colours=[]

while keyboard.is_pressed('q')==False:
        # print("started")
        if read==True:
            # print("r true")
            check_colour_blink()
            time.sleep(0.1)
        else:
            # print("r false")
            # time.sleep(1)
            for colour_num in colours:
                if colour_num==1:
                    click(595,554)
                    time.sleep(0.1)
                if colour_num==2:
                    click(584,789)
                    time.sleep(0.1)
                if colour_num==3:
                    click(368,784)
                    time.sleep(0.1)
                if colour_num==4:
                    click(371,565)
                    time.sleep(0.1)
            # print("clicked")
            time.sleep(0.1)
            read = True
            colour_count=0
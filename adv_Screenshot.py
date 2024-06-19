import pyautogui
import time
import tkinter as tk

def SS():
    time.sleep(1)
    name = time.time()
    name = 'G:/ex_py/new/ADv/ss/{}.png'.format(name)
    img = pyautogui.screenshot()
    img.save(name)
    img.show()
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,text="Take ScreenShot",command=SS)
button.pack(side=tk.LEFT)

close = tk.Button(frame,text="Quit",command=quit)
close.pack(side=tk.LEFT)


root.mainloop()
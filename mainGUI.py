import tkinter as tk
from win32api import GetSystemMetrics
import main as bot

def helloCallBack():
    print("urfjied")

main = tk.Tk()
main.title("Elena")

screen_width = GetSystemMetrics(0)
screen_height =  GetSystemMetrics(1)
root_width = 500
root_height = 700

x = (screen_width/2) - (root_width/2)
y = (screen_height/2) - (root_height/2)
main.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

button = tk.Button(main, text ="Speak", command = bot.run_bot)
button.pack()

main.iconbitmap("test.png")
main.mainloop()
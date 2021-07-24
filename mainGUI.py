import tkinter as tk
from win32api import GetSystemMetrics
import main as bot

def changeListeningLabel(updatedText):
    print("yes i come")
    listeningLabel.config(text = updatedText)

main = tk.Tk()
main.title("Elena")

screen_width = GetSystemMetrics(0)
screen_height =  GetSystemMetrics(1)
root_width = 500
root_height = 700

x = (screen_width/2) - (root_width/2)
y = (screen_height/2) - (root_height/2)
main.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

tk.Label(main, height = 8).grid(row = 0, column = 0)
tk.Label(main, height = 7, width = 60, text = "LOGO", bg = "purple").grid(row = 1, column = 0)
tk.Label(main, height = 3).grid(row = 2, column = 0)
button = tk.Button(main, text ="Speak", command = bot.run_bot).grid(row = 3, column = 0)
listeningLabel = tk.Label(main, height = 4, width = 60, text = "4")
listeningLabel.grid(row = 2, column = 0)

main.iconbitmap("test.png")
main.mainloop()
import tkinter as tk
from PIL import ImageTk, Image
from win32api import GetSystemMetrics
import main as bot
import ctypes
from time import sleep

def onEnter(event):
    buttonToSpeak.config(image=buttonCircleHover)

def onLeave(event):
    buttonToSpeak.config(image=buttonCircleAwaiting)

print("Initialising Elena.exe... Please wait - do not close this window, please.")
print("Elena is ready! Preparation ready in...", end = '')
for i in range(5):
    sleep(1)
    print(str(i) + "...", end = '')

ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 ) # Hide the console.
main = tk.Tk()
main.title("")
main.configure(bg='white')


screen_width = GetSystemMetrics(0)
screen_height =  GetSystemMetrics(1)
root_width = 500
root_height = 700

x = (screen_width/2) - (root_width/2)
y = (screen_height/2) - (root_height/2)
main.geometry('%dx%d+%d+%d' % (root_width, root_height, x, y))

logo = ImageTk.PhotoImage(Image.open("../virtual-assistant/resources/elena.png"))


buttonCircleAwaiting = ImageTk.PhotoImage(Image.open("../virtual-assistant/resources/button_waiting.png"))
buttonCircleHover = ImageTk.PhotoImage(Image.open("../virtual-assistant/resources/button_hover.png"))

tk.Label(main, height = 5,bg='white').grid(row = 0, column = 0)
tk.Label(main, image = logo,bg='white').grid(row = 1, column = 0)
tk.Label(main, height = 5,bg='white').grid(row = 2, column = 0)
buttonToSpeak = tk.Button(main,image = buttonCircleAwaiting,bg='white', command = bot.run_bot,highlightthickness = 0, bd = 0)
buttonToSpeak.grid(row = 3, column = 0)
buttonToSpeak.focus()


buttonToSpeak.bind('<Enter>',  onEnter)
buttonToSpeak.bind('<Leave>',  onLeave)


# file = r'taskbar_icon.png'
# img = Image.open(file)
# img.save('taskbar_icon.ico',format = 'ICO', sizes=[(32,32)])
main.iconbitmap("../virtual-assistant/resources/taskbar_icon.ico")

main.mainloop()

if __name__ == "__main__":
   main()
# GUIwinget python source file , by alireza138812

# importing modules
import os
try:
    from tkinter import *
finally:
    import sys
    print("Tkinter is not installed")
    sys.exit()
    

# define funcetions

class app():

    def installappname():
        installing(enter.get())
        name = enter.get()
        os.system(f"winget install --name {name}")

    def installappid():
        app.installing(enter.get())
        id = enter.get()
        os.system(f"winget install --id {id}")

    def installing(appname):
        text = (f"Installing {appname} , check opened console")
        Label(window, text=text).pack()



# window settings

window = Tk()
window.geometry("250x100")
window.title("GUIwinget")
# Entry
enter = Entry(window)
enter.pack()

# Buttons

Install = Button(window, text="Install", command=app.installappname).place(x=5, y=50)
Installid = Button(window, text="Install with ID", command=app.installappid).place(x=160, y=50)

# Main loop

window.mainloop()
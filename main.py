from customtkinter import *
from screeninfo import get_monitors
from prompt_engine import update_current_thread

# CONFIGURE WINDOWS
set_appearance_mode('dark')
set_default_color_theme('dark-blue')

HEIGHT: str = ""
WIDTH: str = ""

for m in get_monitors():
    HEIGHT = m.height
    WIDTH = m.width


root = CTk()
root.title("Minion AI")
root.geometry(f'{WIDTH}x{HEIGHT}')



root.mainloop()

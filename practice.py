from customtkinter import *
from dotenv import load_dotenv
import os

load_dotenv()
set_appearance_mode(os.getenv("APPEARANCE_MODE"))

root = CTk()

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()

root.geometry(f"{WIDTH}x{HEIGHT}")

thread_frame = CTkFrame(master=root, width=WIDTH, height=HEIGHT * 0.75)
thread_frame.configure(border_color="blue")

background_label = CTkLabel(master=thread_frame)
background_label.pack(side="left", pady=20, padx=20)

thread_frame.place(x=0, y=0)

prompt = CTkEntry(master=root, placeholder_text="Message Minion AI", width=WIDTH, height=60)
prompt.place(x=0, y=HEIGHT * 0.9)

root.mainloop()

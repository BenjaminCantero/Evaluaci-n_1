import customtkinter as ctk
from restorant import App

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  
    root = ctk.CTk()
    app = App(root)
    root.mainloop()

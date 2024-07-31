from home_page import show_home_page
import tkinter as tk
from config import save_and_exit

def main():
    root = tk.Tk()
    root.title("Soccer Field Click Tracker")
    
    show_home_page(root, "images/Pitch_Transparent_50.png")
    
    # Bind the window close event
    root.protocol("WM_DELETE_WINDOW", save_and_exit)
    
    root.mainloop()

if __name__ == "__main__":
    main()
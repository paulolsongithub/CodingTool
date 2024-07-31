import tkinter as tk
from interface_setup import setup_initial_interface
from player_selector import show_player_selector
from config import AppConfig

def show_home_page(root, image_path):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Game ID entry
    game_id_label = tk.Label(root, text="Game ID:", font=('Helvetica', 16))
    game_id_label.pack(pady=(10, 5))
    game_id_entry = tk.Entry(root, font=('Helvetica', 16))
    game_id_entry.pack(pady=(0, 20))

    def on_continue():
        # Capture and store the game_id from the user's input
        AppConfig.game_id = game_id_entry.get()
        # Proceed to the player selector interface
        show_player_selector(root, image_path)

    # Continue button with command that transitions to the player selector when clicked
    continue_button = tk.Button(root, text="Continue", command=on_continue, height=2, width=10, font=('Helvetica', 20))
    continue_button.pack(pady=20)
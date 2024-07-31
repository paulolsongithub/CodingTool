import tkinter as tk
from tkinter import font
from config import AppConfig
from PIL import Image, ImageTk
from interface_setup import setup_initial_interface

def show_player_selector(root, image_path):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Frame for the canvas
    canvas_frame = tk.Frame(main_frame)
    canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Frame for the continue button, positioned to fill the remaining space
    button_frame = tk.Frame(main_frame)
    button_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Open the original image using PIL and resize it
    original_image = Image.open("images/lineup_selector.png")
    resized_image = original_image.resize((797, 865), Image.Resampling.LANCZOS)
    
    # Create a PhotoImage object using ImageTk, not Tkinter's PhotoImage
    field_image = ImageTk.PhotoImage(resized_image)
    
    # Create the canvas and place the image on it
    canvas = tk.Canvas(canvas_frame, width=797, height=865)
    canvas.create_image(0, 0, anchor='nw', image=field_image)
    canvas.pack()
    
    # Keep a reference to the image to prevent garbage collection
    root.field_image = field_image

    # Define positions for the player entries on the canvas
    player_positions = {
        'GK': (390, 751),
        'LB': (166, 644),
        'LCB': (279, 644),
        'CB': (389, 644),
        'RCB': (501, 644),
        'RB': (613, 644),
        'LWB': (166, 537),
        'LDM': (279, 537),
        'CDM': (389, 537),
        'RDM': (501, 537),
        'RWB': (613, 537),
        'LM': (166, 427),
        'LCM': (279, 427),
        'CM': (389, 427),
        'RCM': (501, 427),
        'RM': (613, 427),
        'LW': (166, 315),
        'LAM': (279, 315),
        'CAM': (389, 315),
        'RAM': (501, 315),
        'RW': (613, 315),
        'SS': (391, 207),
        'CF': (320, 112),
        'ST': (463, 112),
        'S1': (739, 76),
        'S2': (739, 190),
        'S3': (739, 299),
        'S4': (739, 406),
        'S5': (739, 522),
        'S6': (739, 646),
        'S7': (739, 766),
    }

    # Dictionary to store the player entry widgets
    player_entries = {}
    
    # Create an entry widget for each player position
    for position, (x, y) in player_positions.items():
        bold_font = font.Font(family="Helvetica", size = 10, weight="bold")
        entry = tk.Entry(canvas, width=4, font=bold_font)
        canvas.create_window(x, y, window=entry)
        player_entries[position] = entry

    def store_player_numbers_and_continue():
        # Iterate through player_entries to store both the player number and the coordinates
        player_data = {
            pos: {'number': entry.get(), 'coords': player_positions[pos]} 
            for pos, entry in player_entries.items() 
            if entry.get().isdigit()  # Ensure we only store data for entries with valid numbers
        }
        AppConfig.player_numbers = player_data
        setup_initial_interface(root, image_path)

    # Button to store player numbers and continue
    continue_button = tk.Button(button_frame, text="Continue", command=store_player_numbers_and_continue, height=2, width=10, font=('Helvetica', 20))
    continue_button.pack(pady=20)
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk
from config import AppConfig
from action_handlers import player_selected

action_type = None
entered_time = ""
type_type = None

def setup_initial_interface(root, image_path):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    # Create and display the label and entry for time input
    time_label = tk.Label(root, text="What time did this happen?", font=('Helvetica', 16))
    time_label.pack(pady=(10, 5))
    time_entry = tk.Entry(root, font=('Helvetica', 16))
    time_entry.pack(pady=(0, 20))

    # Period selector setup
    period_label = tk.Label(root, text="Period:", font=('Helvetica', 16))
    period_label.pack(pady=(10, 5))
    period_frame = tk.Frame(root)
    period_frame.pack(pady=10)

    # Function to update the period and button styles
    def update_period(new_period):
        AppConfig.period = new_period
        # Update button styles to reflect the current selection
        for button in period_buttons:
            if button['text'] == str(new_period):
                button.config(bg='lightblue')  # Highlight the selected button
            else:
                button.config(bg='SystemButtonFace')  # Reset other buttons to default

    # Create and store a list of period buttons for easy access
    period_buttons = []
    for period in range(1, 5):  # Assuming periods 1 through 4
        button = tk.Button(period_frame, text=str(period),
                           command=lambda p=period: update_period(p),
                           height=1, width=2)
        button.pack(side='left', padx=5)
        period_buttons.append(button)

    # Initialize the first period as selected
    update_period(AppConfig.period)

    # Instructions label
    action_label = tk.Label(root, text="Choose your Action type:", font=('Helvetica', 16))
    action_label.pack(pady=(10, 20))

    # Action buttons
    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)  # Adjust padding as needed

    shot_button = tk.Button(frame, text="Shot", command=lambda: type_question("Shot", root, image_path, time_entry.get()),
                            height=2, width=10, font=('Helvetica', 20))
    pass_button = tk.Button(frame, text="Pass", command=lambda: type_question("Pass", root, image_path, time_entry.get()),
                            height=2, width=10, font=('Helvetica', 20))
    possession_button = tk.Button(frame, text="Possession", command=lambda: type_question("Possession", root, image_path, time_entry.get()),
                            height=2, width=10, font=('Helvetica', 20))
    # through_button = tk.Button(frame, text="Through Ball", command=lambda: type_question("Through Ball", root, image_path, time_entry.get()),
    #                         height=2, width=10, font=('Helvetica', 20))
    setpiece_button = tk.Button(frame, text="Set Piece", command=lambda: type_question("Set Piece", root, image_path, time_entry.get()),
                            height=2, width=10, font=('Helvetica', 20))

    # Configure the grid to have 6 columns for finer control over button sizing
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.columnconfigure(4, weight=1)
    frame.columnconfigure(5, weight=1)

    # Top buttons spanning 3 columns each
    shot_button.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    pass_button.grid(row=0, column=3, columnspan=3, padx=10, pady=10)

    # Bottom buttons, each spanning 2 columns to fit evenly below the top buttons
    possession_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    # through_button.grid(row=1, column=2, columnspan=2, padx=10, pady=10)
    setpiece_button.grid(row=1, column=3, columnspan=2, padx=10, pady=10) 

def type_question(selected_action, root, image_path, time):

    for widget in root.winfo_children():
        widget.destroy()

    type_label = tk.Label(root, text=f"What type of {selected_action} was it?", font=('Helvetica', 16))
    type_label.pack(pady=(10, 20))    

    global action_type, entered_time
    action_type = selected_action
    entered_time = time  # Capture the time right after an action is selected

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)  # Adjust padding as needed

    if action_type == "Shot":
        header_button = tk.Button(frame, text="Header", command=lambda: result_question(root, image_path, "Header"),
                            height=2, width=10, font=('Helvetica', 20))
        shot_type_button = tk.Button(frame, text="Shot", command=lambda: result_question(root, image_path, "Shot"),
                            height=2, width=10, font=('Helvetica', 20))
        volley_button = tk.Button(frame, text="Volley", command=lambda: result_question(root, image_path, "Volley"),
                            height=2, width=10, font=('Helvetica', 20))
        freekick_button = tk.Button(frame, text="Free Kick", command=lambda: result_question(root, image_path, "Free Kick"),
                            height=2, width=10, font=('Helvetica', 20))
        

        header_button.grid(row=0, column=0, padx=10, pady=10)    
        shot_type_button.grid(row=1, column=0, padx=10, pady=10)    
        volley_button.grid(row=0, column=1, padx=10, pady=10)    
        freekick_button.grid(row=1, column=1, padx=10, pady=10)

    elif action_type == "Pass":
        cross_button = tk.Button(frame, text="Cross", command=lambda: result_question(root, image_path, "Cross"),
                            height=2, width=10, font=('Helvetica', 20))
        pass_button = tk.Button(frame, text="Key Pass", command=lambda: result_question(root, image_path, "Pass"),
                            height=2, width=10, font=('Helvetica', 20))
        through_button = tk.Button(frame, text="Through Ball", command=lambda:result_question (root, image_path, "Through Ball"),
                            height=2, width=10, font=('Helvetica', 20))
        

        cross_button.grid(row=0, column=2, padx=10, pady=10)    
        pass_button.grid(row=0, column=0, padx=10, pady=10)    
        through_button.grid(row=0, column=1, padx=10, pady=10)

    elif action_type == "Possession":
        offensive_button = tk.Button(frame, text="Offensive", command=lambda: result_question(root, image_path, "Offensive"),
                            height=2, width=10, font=('Helvetica', 20))
        defensive_button = tk.Button(frame, text="Defensive", command=lambda: result_question(root, image_path, "Defensive"),
                            height=2, width=10, font=('Helvetica', 20))
        
   
        offensive_button.grid(row=0, column=0, padx=10, pady=10)    
        defensive_button.grid(row=0, column=1, padx=10, pady=10)

    elif action_type == "Through Ball":
        pass_button = tk.Button(frame, text="Pass", command=lambda: result_question(root, image_path, "Pass"),
                            height=2, width=10, font=('Helvetica', 20))

        pass_button.grid(row=0, column=0, padx=10, pady=10)

    elif action_type == "Set Piece":
        freekick_button = tk.Button(frame, text="Free Kick", command=lambda: result_question(root, image_path, "Free Kick"),
                            height=2, width=10, font=('Helvetica', 20))
        corner_button = tk.Button(frame, text="Corner", command=lambda: result_question(root, image_path, "Corner"),
                            height=2, width=10, font=('Helvetica', 20))
        
   
        corner_button.grid(row=0, column=1, padx=10, pady=10)    
        freekick_button.grid(row=0, column=0, padx=10, pady=10)

    else:
        header_button = tk.Button(frame, text="Header", command=lambda: result_question(root, image_path, "Header"),
                            height=2, width=10, font=('Helvetica', 20))

        header_button.grid(row=0, column=0, padx=10, pady=10)    # Top-left

    back_button = tk.Button(root, text="Back", command=lambda: setup_initial_interface(root, image_path), font=('Helvetica', 16))
    back_button.pack(pady=(10, 20))
        
def setup_player_picker(root, image_path):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Instructions label
    instruction_label = tk.Label(root, text="Select the player:", font=('Helvetica', 16))
    instruction_label.pack(pady=(10, 20))

    # Create a canvas for the field
    canvas = tk.Canvas(root, width=797, height=865)  # Adjust size as needed
    canvas.pack()

    # Load and set the pitch background image
    pitch_image = Image.open("images/Pitch_Tall.png")  # Make sure the path is correct
    pitch_resized_image = pitch_image.resize((797, 865), Image.Resampling.LANCZOS)
    pitch_photo_image = ImageTk.PhotoImage(pitch_resized_image)
    canvas.create_image(0, 0, anchor='nw', image=pitch_photo_image)
    canvas.pitch_photo_image = pitch_photo_image  # Explicitly store a reference

    # Load and resize the jersey image
    original_image = Image.open("images/Jersey_back_transparent.png")
    resized_image = original_image.resize((75, 75), Image.Resampling.LANCZOS)
    jersey_image = ImageTk.PhotoImage(resized_image)

    # Keep a reference to prevent garbage collection
    canvas.jersey_images = []

    for position, info in AppConfig.player_numbers.items():
        x, y = info['coords']
        player_number = info['number']
        
        # Create an image with the jersey at each position
        image_id = canvas.create_image(x, y, image=jersey_image)
        
        # Create a text widget on the canvas for the player number
        text_id = canvas.create_text(x, y, text=str(player_number), font=('Helvetica', 16, 'bold'), fill="white")
        
        # Group the image and text under a common tag
        common_tag = f"player_{position}"
        canvas.addtag_withtag(common_tag, image_id)
        canvas.addtag_withtag(common_tag, text_id)
        
        # Bind a click event to the common tag
        canvas.tag_bind(common_tag, "<Button-1>", lambda event, pn=player_number: player_selected(pn, root, image_path))

        # Keep a reference to the jersey images
        canvas.jersey_images.append(jersey_image)
    
    # Load and resize the opponent jersey image
    opponent_image = Image.open("images/Jersey_back_transparent_orange.png")
    resized_opponent_image = opponent_image.resize((75, 75), Image.Resampling.LANCZOS)
    opponent_jersey_image = ImageTk.PhotoImage(resized_opponent_image)

    # Keep a reference to prevent garbage collection
    canvas.opponent_jersey_image = opponent_jersey_image

    x, y = (50, 76)
    opponent_number = -1

    opponent_image_id = canvas.create_image(x, y, image=opponent_jersey_image)
    opponent_text_id = canvas.create_text(x, y, text=str(opponent_number), font=('Helvetica', 16, 'bold'), fill="white")
    opponent_tag = "opponent_player"
    canvas.addtag_withtag(opponent_tag, opponent_image_id)
    canvas.addtag_withtag(opponent_tag, opponent_text_id)
    canvas.tag_bind(opponent_tag, "<Button-1>", lambda event, pn=opponent_number: player_selected(pn, root, image_path))

    back_button = tk.Button(root, text="Back", command=lambda: result_question(root, image_path, type_type), font=('Helvetica', 16))
    back_button.pack(pady=(10, 20))
    


# def show_field(root, image_path, action_type):
#     from action_handlers import canvas_click
#     # Clear the window
#     for widget in root.winfo_children():
#         widget.destroy()

#     # Display label based on the selected action
#     question_label = Label(root, text=f"Where did the {action_type} happen?", font=('Helvetica', 16))
#     question_label.pack(pady=(10, 20))

#     # Load and display the soccer field image
#     image = Image.open(image_path)
#     photo = ImageTk.PhotoImage(image)
#     canvas = tk.Canvas(root, width=image.width, height=image.height)
#     canvas.pack()
#     canvas.create_image(0, 0, anchor=tk.NW, image=photo)
#     canvas.image = photo  # Keep a reference
#     canvas.bind("<Button-1>", lambda event, c=canvas: canvas_click(event, canvas, root, image_path))

# ROTATE CODE
def show_field(root, image_path, action_type):
    from action_handlers import canvas_click
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Display label based on the selected action
    question_label = Label(root, text=f"Where did the {action_type} happen?", font=('Helvetica', 16))
    question_label.pack(pady=(10, 20))

    # Load and rotate the soccer field image
    image = Image.open(image_path)
    rotated_image = image.rotate(-90, expand=True)
    photo = ImageTk.PhotoImage(rotated_image)
    canvas = tk.Canvas(root, width=rotated_image.width, height=rotated_image.height)
    canvas.pack()
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo  # Keep a reference
    canvas.bind("<Button-1>", lambda event, c=canvas: canvas_click(event, canvas, root, image_path))

    back_button = tk.Button(root, text="Back", command=lambda: setup_player_picker(root, image_path), font=('Helvetica', 16))
    back_button.pack(pady=(10, 20))


def show_goalmouth(root, image_path):
    from action_handlers import goalcanvas_click

    for widget in root.winfo_children():
        widget.destroy()
    
    question_label = Label(root, text = f"Where did the shot end up?", font=('Helvetica', 16))
    question_label.pack(pady=(10, 20))

    goalimage = Image.open("images/Goalmouth.png")
    goalphoto = ImageTk.PhotoImage(goalimage)
    goalcanvas = tk.Canvas(root, width=goalimage.width, height=goalimage.height)
    goalcanvas.pack()
    goalcanvas.create_image(0, 0, anchor=tk.NW, image=goalphoto)
    goalcanvas.image = goalphoto  # Keep a reference
    goalcanvas.bind("<Button-1>", lambda event, c=goalcanvas: goalcanvas_click(event, root, image_path))

def shot_related_question(root, image_path):
    from action_handlers import related_shot
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Instructions label
    action_label = tk.Label(root, text="Was this shot related to the action before?", font=('Helvetica', 16))
    action_label.pack(pady=(10, 20))

    frame = tk.Frame(root)
    frame.pack(pady=20, padx=20)  # Adjust padding as needed

    yes_button = tk.Button(frame, text="Yes", command=lambda: related_shot(root, image_path, "Yes"),
                            height=2, width=10, font=('Helvetica', 20))
    no_button = tk.Button(frame, text="No", command=lambda: related_shot(root, image_path, "No"),
                            height=2, width=10, font=('Helvetica', 20))
        
   
    yes_button.grid(row=0, column=0, padx=10, pady=10)    
    no_button.grid(row=0, column=1, padx=10, pady=10)

def result_question(root, image_path, selected_type):
    from action_handlers import set_result_and_show_field

    for widget in root.winfo_children():
        widget.destroy()

    result_label = tk.Label(root, text=f"What was the Result?", font=('Helvetica', 16))
    result_label.pack(pady=(10, 20))    

    global type_type
    type_type = selected_type

    if type_type == "Cross":
        pass
    else:
        runners = None
        frame = tk.Frame(root)
        frame.pack(pady=20, padx=20)  # Adjust padding as needed

    if action_type == "Shot":
        blocked_button = tk.Button(frame, text="Blocked", command=lambda: set_result_and_show_field(root, image_path, "Blocked"),
                            height=2, width=10, font=('Helvetica', 20))
        goal_button = tk.Button(frame, text="Goal", command=lambda: set_result_and_show_field(root, image_path, "Goal"),
                            height=2, width=10, font=('Helvetica', 20))
        offtarget_button = tk.Button(frame, text="Off Target", command=lambda: set_result_and_show_field(root, image_path, "Off Target"),
                            height=2, width=10, font=('Helvetica', 20))
        saved_button = tk.Button(frame, text="Saved", command=lambda: set_result_and_show_field(root, image_path, "Saved"),
                            height=2, width=10, font=('Helvetica', 20))
        

        blocked_button.grid(row=0, column=0, padx=10, pady=10)    
        goal_button.grid(row=1, column=0, padx=10, pady=10)    
        offtarget_button.grid(row=0, column=1, padx=10, pady=10)    
        saved_button.grid(row=1, column=1, padx=10, pady=10)

    elif type_type == "Cross":

        runners_label = tk.Label(root, text="How many runners were there?", font=('Helvetica', 16))
        #runners_label.grid(row=0, column=0, padx=10, pady=10)
        runners_label.pack(pady=(10,20))

        runners_entry = tk.Entry(root, font=('Helvetica', 16))
        #runners_entry.grid(row=1, column=0, padx=10, pady=10)
        runners_entry.pack(pady=(10,20))

        frame = tk.Frame(root)
        frame.pack(pady=20, padx=20)
    
        successful_button = tk.Button(frame, text="Successful", command=lambda: set_result_and_show_field(root, image_path, "Successful", runners_entry.get()),
                        height=2, width=10, font=('Helvetica', 20))
        unsuccessful_button = tk.Button(frame, text="Unsuccessful", command=lambda: set_result_and_show_field(root, image_path, "Unsuccessful", runners_entry.get()),
                        height=2, width=10, font=('Helvetica', 20))
        assist_button = tk.Button(frame, text="Assist", command=lambda: set_result_and_show_field(root, image_path, "Assist", runners_entry.get()),
                        height=2, width=10, font=('Helvetica', 20))
        deflected_button = tk.Button(frame, text="Deflected", command=lambda: set_result_and_show_field(root, image_path, "Deflected", runners_entry.get()),
                        height=2, width=10, font=('Helvetica', 20))

        successful_button.grid(row=0, column=0, padx=10, pady=10)    
        unsuccessful_button.grid(row=0, column=1, padx=10, pady=10)    
        assist_button.grid(row=1, column=0, padx=10, pady=10)    
        deflected_button.grid(row=1, column=1, padx=10, pady=10)

    elif action_type == "Pass":
        successful_button = tk.Button(frame, text="Successful", command=lambda: set_result_and_show_field(root, image_path, "Successful"),
                            height=2, width=10, font=('Helvetica', 20))
        unsucessful_button = tk.Button(frame, text="Unsuccessful", command=lambda: set_result_and_show_field(root, image_path, "Unsuccessful"),
                            height=2, width=10, font=('Helvetica', 20))
        assist_button = tk.Button(frame, text="Assist", command=lambda: set_result_and_show_field(root, image_path, "Assist"),
                            height=2, width=10, font=('Helvetica', 20))
        deflected_button = tk.Button(frame, text="Deflected", command=lambda: set_result_and_show_field(root, image_path, "Deflected"),
                            height=2, width=10, font=('Helvetica', 20))
        

        successful_button.grid(row=0, column=0, padx=10, pady=10)    
        unsucessful_button.grid(row=0, column=1, padx=10, pady=10)    
        assist_button.grid(row=1, column=0, padx=10, pady=10)    
        deflected_button.grid(row=1, column=1, padx=10, pady=10)

    elif type_type == "Free Kick":
        blocked_button = tk.Button(frame, text="Blocked", command=lambda: set_result_and_show_field(root, image_path, "Blocked"),
                            height=2, width=10, font=('Helvetica', 20))
        goal_button = tk.Button(frame, text="Goal", command=lambda: set_result_and_show_field(root, image_path, "Goal"),
                            height=2, width=10, font=('Helvetica', 20))
        offtarget_button = tk.Button(frame, text="Off Target", command=lambda: set_result_and_show_field(root, image_path, "Off Target"),
                            height=2, width=10, font=('Helvetica', 20))
        saved_button = tk.Button(frame, text="Saved", command=lambda: set_result_and_show_field(root, image_path, "Saved"),
                            height=2, width=10, font=('Helvetica', 20))
        successful_button = tk.Button(frame, text="Successful", command=lambda: set_result_and_show_field(root, image_path, "Successful"),
                            height=2, width=10, font=('Helvetica', 20))
        unsuccessful_button = tk.Button(frame, text="Unsuccessful", command=lambda: set_result_and_show_field(root, image_path, "Unsuccessful"),
                            height=2, width=10, font=('Helvetica', 20))
        assist_button = tk.Button(frame, text="Assist", command=lambda: set_result_and_show_field(root, image_path, "Assist"),
                            height=2, width=10, font=('Helvetica', 20))

        blocked_button.grid(row=0, column=0, padx=10, pady=10)    
        goal_button.grid(row=1, column=0, padx=10, pady=10)    
        offtarget_button.grid(row=0, column=1, padx=10, pady=10)    
        saved_button.grid(row=1, column=1, padx=10, pady=10)
        successful_button.grid(row=0, column=2, padx=10, pady=10)    
        unsuccessful_button.grid(row=1, column=2, padx=10, pady=10)
        assist_button.grid(row=2, column = 1, padx=10, pady=10)        

    elif type_type == "Corner":
        successful_button = tk.Button(frame, text="Successful", command=lambda: set_result_and_show_field(root, image_path, "Successful"),
                            height=2, width=10, font=('Helvetica', 20))
        unsuccessful_button = tk.Button(frame, text="Unsuccessful", command=lambda: set_result_and_show_field(root, image_path, "Unsuccessful"),
                            height=2, width=10, font=('Helvetica', 20))
        assist_button = tk.Button(frame, text="Assist", command=lambda: set_result_and_show_field(root, image_path, "Assist"),
                            height=2, width=10, font=('Helvetica', 20))
        

        successful_button.grid(row=0, column=0, padx=10, pady=10)    
        unsuccessful_button.grid(row=0, column=1, padx=10, pady=10)      
        assist_button.grid(row=1, column=1, padx=10, pady=10)
    
    else:
        successful_button = tk.Button(frame, text="Successful", command=lambda: set_result_and_show_field(root, image_path, "Successful"),
                            height=2, width=10, font=('Helvetica', 20))
        unsuccessful_button = tk.Button(frame, text="Unsuccessful", command=lambda: set_result_and_show_field(root, image_path, "Unsuccessful"),
                            height=2, width=10, font=('Helvetica', 20))
        
        successful_button.grid(row=0, column=0, padx=10, pady=10)    
        unsuccessful_button.grid(row=0, column=1, padx=10, pady=10)

    back_button = tk.Button(root, text="Back", command=lambda: type_question(action_type, root, image_path, entered_time), font=('Helvetica', 16))
    back_button.pack(pady=(10, 20))
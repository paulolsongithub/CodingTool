from utilities import transform_coordinates, draw_temp_line, transform_goal_coordinates
from config import AppConfig

# Global state variables
selected_player_number = None
start_location_x = None
start_location_y = None
end_location_x = None
end_location_y = None
end_location_z = None
capturing_start = True
line_x, line_y = None, None
result = None
runners = None

def set_result_and_show_field(root, image_path, selected_result, runners_count=None):
    from interface_setup import setup_player_picker
    global result, runners
    result = selected_result  # Capture the time right after an action is selected
    runners = runners_count
    setup_player_picker(root, image_path)

def player_selected(player_number, root, image_path):
    from interface_setup import show_field, action_type
    global selected_player_number
    selected_player_number = player_number
    show_field(root, image_path, action_type)

# def canvas_click(event, canvas, root, image_path):
#     from interface_setup import setup_initial_interface, show_goalmouth, shot_related_question, action_type, entered_time, type_type
#     from config import AppConfig, add_event_data

#     global start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, line_x, line_y, capturing_start
#     x, y = transform_coordinates(event.x, event.y, image_path)
#     line_x, line_y = event.x, event.y
#     if capturing_start:
#         start_location_x, start_location_y = x, y
#         end_location_z = None
#         radius = 5
#         canvas.create_oval(event.x-radius, event.y-radius, event.x+radius, event.y+radius, fill='blue')
#         if action_type == "Possession":
#             # For Possession, only capture the start location and then reset
#             capturing_start = True  # Allow capturing another start location without needing an end location
#             end_location_x, end_location_y = None, None  # Reset end locations to None
#             print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) {result} Runners for cross {runners}")
#             add_event_data(AppConfig.game_id, AppConfig.event_id, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
#             AppConfig.event_id = AppConfig.event_id + 1
#             AppConfig.id = AppConfig.id + 1
#             setup_initial_interface(root, image_path)
#         else:
#             capturing_start = False  # For other actions, next click will capture the end location
#             canvas.bind("<Motion>", lambda e, c=canvas: draw_temp_line(e, c, line_x, line_y))

#     elif (action_type == "Shot" or (type_type == 'Free Kick' and (result == "Goal" or result == "Saved"))) and x > 118.0:
#         canvas.unbind("<Motion>")
#         # Optional: Delete the temporary line from the canvas
#         canvas.delete("temp_line")
#         if x > 120:
#             x = 120
#         end_location_x = x
#         show_goalmouth(root, image_path)

#     elif action_type == "Shot":
#         end_location_x, end_location_y = x, y
#         shot_related_question(root, image_path)

#     else:
#         canvas.unbind("<Motion>")
#         # Optional: Delete the temporary line from the canvas
#         canvas.delete("temp_line")
#         if action_type != "Possession":  # Only capture end location for actions other than Possession
#             if x > 120:
#                 x = 120
#             end_location_x, end_location_y = x, y
#             print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) and ending at ({end_location_x:.2f}, {end_location_y:.2f}) {result} Runners for cross {runners}")
#             add_event_data(AppConfig.game_id, AppConfig.event_id, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
#         capturing_start = True  # Reset for the next action/event, allowing to capture a new start location
#         AppConfig.event_id = AppConfig.event_id + 1
#         AppConfig.id = AppConfig.id + 1
#         setup_initial_interface(root, image_path)
        
# ROTATE CODE
def canvas_click(event, canvas, root, image_path):
    from interface_setup import setup_initial_interface, show_goalmouth, shot_related_question, action_type, entered_time, type_type
    from config import AppConfig, add_event_data

    global start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, line_x, line_y, capturing_start, runners
    x, y = transform_coordinates(event.x, event.y, image_path)
    line_x, line_y = event.x, event.y
    if capturing_start:
        start_location_x, start_location_y = x, y
        end_location_z = None
        radius = 5
        canvas.create_oval(event.x-radius, event.y-radius, event.x+radius, event.y+radius, fill='blue')
        if action_type == "Possession":
            # For Possession, only capture the start location and then reset
            capturing_start = True  # Allow capturing another start location without needing an end location
            end_location_x, end_location_y = None, None  # Reset end locations to None
            print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) {result}")
            add_event_data(AppConfig.game_id, AppConfig.event_id, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
            AppConfig.event_id = AppConfig.event_id + 1
            AppConfig.id = AppConfig.id + 1
            setup_initial_interface(root, image_path)
        else:
            capturing_start = False  # For other actions, next click will capture the end location
            canvas.bind("<Motion>", lambda e, c=canvas: draw_temp_line(e, c, line_x, line_y))

    elif (action_type == "Shot" or (type_type == 'Free Kick' and (result == "Goal" or result == "Saved"))) and y > 118.0:
        canvas.unbind("<Motion>")
        # Optional: Delete the temporary line from the canvas
        canvas.delete("temp_line")
        if y > 120:
            y = 120
        end_location_x, end_location_y = x, y
        show_goalmouth(root, image_path)

    elif action_type == "Shot":
        end_location_x, end_location_y = x, y
        shot_related_question(root, image_path)

    else:
        canvas.unbind("<Motion>")
        # Optional: Delete the temporary line from the canvas
        canvas.delete("temp_line")
        if action_type != "Possession":  # Only capture end location for actions other than Possession
            if y > 120:
                y = 120
            end_location_x, end_location_y = x, y
            print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) and ending at ({end_location_x:.2f}, {end_location_y:.2f}) {result} Runners for cross {runners}")
            add_event_data(AppConfig.game_id, AppConfig.event_id, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
        capturing_start = True  # Reset for the next action/event, allowing to capture a new start location
        AppConfig.event_id = AppConfig.event_id + 1
        AppConfig.id = AppConfig.id + 1
        setup_initial_interface(root, image_path)

def goalcanvas_click(event, root, image_path):
    from interface_setup import shot_related_question
    global start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, capturing_start
    x, z = transform_goal_coordinates(event.x, event.y, "images/Goalmouth.png")
    if capturing_start:
        pass
    else:
        end_location_x, end_location_z = x, z
        shot_related_question(root, image_path)

def related_shot(root, image_path, related):
    from interface_setup import setup_initial_interface, action_type, entered_time, type_type
    from config import add_event_data
    global start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, capturing_start

    # Construct the ending location string, conditionally including Z if it exists
    end_location_str = f"({end_location_x:.2f}, {end_location_y:.2f}" + (f", {end_location_z:.2f})" if end_location_z is not None else ")")

    if related == "Yes":
        print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id-1}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) and ending at {end_location_str} {result}")
        add_event_data(AppConfig.game_id, AppConfig.event_id-1, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
        capturing_start = True  # Reset for the next action/event
        AppConfig.id = AppConfig.id + 1
    else:
        print(f"Game Id: {AppConfig.game_id}, Event Id: {AppConfig.event_id}, Id: {AppConfig.id}, Period: {AppConfig.period}, {entered_time} Player {selected_player_number} {action_type} - {type_type} starting at ({start_location_x:.2f}, {start_location_y:.2f}) and ending at {end_location_str} {result}")
        add_event_data(AppConfig.game_id, AppConfig.event_id, AppConfig.id, AppConfig.period, entered_time, selected_player_number, action_type, type_type, start_location_x, start_location_y, end_location_x, end_location_y, end_location_z, result, runners)
        AppConfig.event_id = AppConfig.event_id + 1
        AppConfig.id = AppConfig.id + 1
        capturing_start = True  # Reset for the next action/event
    
    setup_initial_interface(root, image_path)
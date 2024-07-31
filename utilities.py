from PIL import Image

# def transform_coordinates(x, y, image_path):
#     image = Image.open(image_path)
#     # Assuming dimensions of the soccer field image
#     canvas_width, canvas_height = image.width, image.height  # Replace with actual dimensions of your image
#     min_x, max_x, min_y, max_y = -20, 140, -20, 100
    
#     # Calculate transformed coordinates
#     transformed_x = ((x / canvas_width) * (max_x - min_x)) + min_x
#     transformed_y = ((1-(y / canvas_height)) * (max_y - min_y)) + min_y
    
#     return transformed_x, transformed_y

# ROTATE CODE
def transform_coordinates(x, y, image_path):
    image = Image.open(image_path)
    canvas_width, canvas_height = image.width, image.height
    min_x, max_x, min_y, max_y = -20, 140, -20, 100
    # min_x, max_x, min_y, max_y = -20, 100, -20, 140

    # Rotate coordinates by 90 degrees
    rotated_x = canvas_width - y
    rotated_y = x

    transformed_x = ((rotated_y / canvas_height) * (max_y - min_y)) + min_y
    transformed_y = (((rotated_x / canvas_width)) * (max_x - min_x)) + min_x
    
    return transformed_x, transformed_y

def transform_goal_coordinates(y, z, image_path):
    image = Image.open(image_path)
    # Assuming dimensions of the soccer field image
    canvas_width, canvas_height = image.width, image.height  # Replace with actual dimensions of your image
    min_y, max_y, min_z, max_z = 34.5, 45.5, -1, 4.75
    
    # Calculate transformed coordinates
    transformed_y = ((y / canvas_width) * (max_y - min_y)) + min_y
    transformed_z = ((1-(z / canvas_height)) * (max_z - min_z)) + min_z
    
    return transformed_y, transformed_z

def draw_temp_line(event, canvas, line_x, line_y):
    # Delete the existing temporary line to avoid drawing multiple lines
    canvas.delete("temp_line")
    
    # Draw a new temporary line from the start location to the current mouse position
    canvas.create_line(line_x, line_y, event.x, event.y, fill="blue", tag="temp_line")
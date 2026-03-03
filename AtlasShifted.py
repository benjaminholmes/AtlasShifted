# Atlas Shifted by Benjamin Holmes#
#Atlas Shifted is an interactive way to reinterpred the world Atlas#
#By Pressing one of any of the character keys on a computer keyboard, one or a few countries are selected.#
#Once selected they can by moved by the directional buttons on the keyboard.#
#Atlas Shifted is built using Python and the CV2 and py5Canvas Python libraries.#
#Built in January 2025 for the module Programming For Artists and Designers#

from py5canvas import *
import cv2
import numpy as np

key = ''  # Global variable to store the pressed key

# Load the input image
img = load_image('vector-map.jpg')
num_wave_vertices = 40  # Number of vertices for the wave
num_waves = 10

# Contour Sets 
first_set = list(range(1, 5))   
second_set = list(range(5, 10))  
third_set = list(range(10, 15))    
fourth_set = list(range(15, 20))   
fifth_set = list(range(20, 25))    
sixth_set = list(range(25, 30))    
seventh_set = list(range(30, 35))  
eighth_set = list(range(35, 40))   
ninth_set = list(range(40, 45))   
tenth_set = list(range(50, 55))   
eleventh_set = list(range(55, 60)) 
twelfth_set = list(range(60, 65))   
thirteenth_set = list(range(65, 70))  
fourteenth_set = list(range(70, 75))  
fifteenth_set = list(range(75, 80))   
sixteenth_set = list(range(80, 85))   
seventeenth_set = list(range(85, 90)) 
eighteenth_set = list(range(90, 95))  
nineteenth_set = list(range(95, 100))  
twentieth_set = list(range(100, 105))   
twenty_first_set = list(range(105, 110))  
twenty_second_set = list(range(110, 115))  
twenty_third_set = list(range(115, 120))  
twenty_fourth_set = list(range(120, 125)) 
twenty_fifth_set = list(range(125, 130))   
twenty_sixth_set = list(range(130, 135)) 
twenty_seventh_set = list(range(135, 140))   
twenty_eighth_set = list(range(140, 145))   
twenty_ninth_set = list(range(145, 150))   
thirtieth_set = list(range(150, 155))   
thirty_first_set = list(range(155, 160)) 
thirty_second_set = list(range(160, 165))  
thirty_third_set = list(range(165, 170))  
thirty_fourth_set = list(range(170, 175))    
thirty_fifth_set = list(range(175, 180))   
thirty_sixth_set = list(range(180, 185))  
thirty_seventh_set = list(range(185, 190))   
thirty_eighth_set = list(range(190, 195))  
thirty_ninth_set = list(range(195, 200))  
fortieth_set = list(range(200, 205))   
forty_first_set = list(range(205, 210))  
forty_second_set = list(range(210, 215)) 
forty_third_set = list(range(215, 220))  
forty_fourth_set = list(range(220, 225))  
forty_fifth_set = list(range(225, 230))   
forty_sixth_set = list(range(230, 235))  
forty_seventh_set = list(range(235, 238))  

# All contours (from original image)
contours = []

# track which contour set is selected
selected_set = first_set

# Contour manipulation variables
contour_offset = np.array([0, 0])  # To translate contours

# Utility function to get contours
def find_contours(im, invert=False, thresh=117, eps=0.0):
    _, thresh_img = cv2.threshold(im, thresh, 256, cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    all_contours = []
    for ctr in contours:
        all_contours.append(np.vstack([ctr[:, 0, 0], ctr[:, 0, 1]]).T)
    return all_contours

def setup():
    global contours
    create_canvas(img.width, img.height)
    
    # Convert py5 image to OpenCV format (numpy array)
    gray_img = np.array(img.convert('L'))  # Convert to grayscale
    gray_img = cv2.blur(gray_img, (5, 5))  # Apply a blur

    # Find contours
    contours = find_contours(gray_img, invert=True, eps=0.1)

def draw():
    global contours

    t = frame_count * 0.2

    # Background animation 
    background(0, 0, 255)
    stroke(255)
    stroke_weight(1)
    wave_amplitude = height / num_waves
    shape_depth = wave_amplitude * 2
    fill(0, 0, 255)

    for y in linspace(0, height, num_waves):
        grey_value = remap(y, 0, height, 250, 0)
        y_resolution = y * 0.001
        y_phase = y * 0.1
        push()
        translate(0, y)
        begin_shape()
        # Create a square bottom left corner
        vertex(0, shape_depth)
        for x in linspace(0, width, num_wave_vertices):
            phase = (x * y_resolution) + y_phase
            vert_y = noise(phase + t) * (wave_amplitude / 2)
            # Add a curve vertex for each point on the wave
            vertex(x, vert_y)
        # Create a square bottom on the bottom right
        vertex(width, shape_depth)
        end_shape(CLOSE)
        pop()

    # Draw all contours with their colors
    draw_colored_contours(contours)
    # Draw contours with transform
    draw_contours_with_transform(contours)

#function to add different colors to different sets of contours
#The draw_colored_contours function was built with the help of ChatGPT. 
#I had built a much less optomised version of it and asked ChatGpt to optomise the previous code.#

def draw_colored_contours(contours):
    # List of colors as RGB tuples 
    colors = [
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (100, 148, 155),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
        (0, 255, 255),  # Cyan
        (128, 0, 198),  # Purple
        (128, 128, 0),  # Olive
        (0, 128, 128),  # Teal
        (255, 165, 0),  # Orange
    ]

    all_sets = [
        first_set, second_set, third_set, fourth_set, fifth_set, sixth_set,
        seventh_set, eighth_set, ninth_set, tenth_set, eleventh_set, twelfth_set,
        thirteenth_set, fourteenth_set, fifteenth_set, sixteenth_set, seventeenth_set,
        eighteenth_set, nineteenth_set, twentieth_set, twenty_first_set, twenty_second_set,
        twenty_third_set, twenty_fourth_set, twenty_fifth_set, twenty_sixth_set, twenty_seventh_set,
        twenty_eighth_set, twenty_ninth_set, thirtieth_set, thirty_first_set, thirty_second_set,
        thirty_third_set, thirty_fourth_set, thirty_fifth_set, thirty_sixth_set, thirty_seventh_set,
        thirty_eighth_set, thirty_ninth_set, fortieth_set, forty_first_set, forty_second_set,
        forty_third_set, forty_fourth_set, forty_fifth_set, forty_sixth_set, forty_seventh_set
    ]

    for i, contour_set in enumerate(all_sets):
        color_index = i % len(colors)  # Cycle through the colors
        r, g, b = colors[color_index]
        fill(r, g, b)
        stroke(0)
        stroke_weight(1)

        for id in contour_set:
            if id < len(contours):  # Ensure id is within bounds
                ctr = contours[id]

                # Draw the contour
                begin_shape()
                for x, y in ctr:
                    vertex(x, y)
                end_shape(CLOSE)

#Function that applies movement to contours on directional key presses
def draw_contours_with_transform(contours):
    
    for id in selected_set:
        
            ctr = contours[id]

            # Apply translation
            ctr[:, 0] += contour_offset[0]
            ctr[:, 1] += contour_offset[1]

def key_pressed(k):
    global key, selected_set, contour_offset, contours
    
    key = k  # Store the pressed key
    
    # Check which key was pressed. Each key selects a different set
    if key == 'a':  
        selected_set = first_set
    elif key == 'b':  
        selected_set = second_set
    elif key == 'c':  
        selected_set = third_set
    elif key == 'd':  
        selected_set = fourth_set
    elif key == 'e':  
        selected_set = fifth_set
    elif key == 'f':  
        selected_set = sixth_set
    elif key == 'g':  
        selected_set = seventh_set
    elif key == 'h':  
        selected_set = eighth_set
    elif key == 'i':  
        selected_set = ninth_set
    elif key == 'j': 
        selected_set = tenth_set
    elif key == 'k':  
        selected_set = eleventh_set
    elif key == 'l':  
        selected_set = twelfth_set
    elif key == 'm':  
        selected_set = thirteenth_set
    elif key == 'n':  
        selected_set = fourteenth_set
    elif key == 'o':  
        selected_set = fifteenth_set
    elif key == 'p':  
        selected_set = sixteenth_set
    elif key == 'q':  
        selected_set = seventeenth_set
    elif key == 'r':  
        selected_set = eighteenth_set
    elif key == 's':  
        selected_set = nineteenth_set
    elif key == 't':  
        selected_set = twentieth_set
    elif key == 'u':  
        selected_set = twenty_first_set
    elif key == 'v':  
        selected_set = twenty_second_set
    elif key == 'w':  
        selected_set = twenty_third_set
    elif key == 'x':  
        selected_set = twenty_fourth_set
    elif key == '1':  
        selected_set = twenty_fifth_set
    elif key == '2':  
        selected_set = twenty_sixth_set
    elif key == '3':  
        selected_set = twenty_seventh_set
    elif key == '4':  
        selected_set = twenty_eighth_set
    elif key == '5':  
        selected_set = twenty_ninth_set
    elif key == '6': 
        selected_set = thirtieth_set
    elif key == '7':  
        selected_set = thirty_first_set
    elif key == '8':  
        selected_set = thirty_second_set
    elif key == '9':  
        selected_set = thirty_third_set
    elif key == '0': 
        selected_set = thirty_fourth_set
    elif key == '-':  
        selected_set = thirty_fifth_set
    elif key == '=':  
        selected_set = thirty_sixth_set
    elif key == '[':  
        selected_set = thirty_seventh_set
    elif key == ']':  
        selected_set = thirty_eighth_set
    elif key == '#':  
        selected_set = thirty_ninth_set
    elif key == ';':  
        selected_set = fortieth_set
    elif key == ',':  
        selected_set = forty_first_set
    elif key == '.':  
        selected_set = forty_second_set
    elif key == '/':  
        selected_set = forty_third_set
    elif key == '+': 
        selected_set = forty_fourth_set
    elif key == '*':  
        selected_set = forty_fifth_set
    elif key == 'z':  
        selected_set = forty_sixth_set
    elif key == 'y': 
        selected_set = forty_seventh_set
    
    # Key checks for contour set movement on selection

    elif key == 'UP':  # Move contours up
        contour_offset[1] -= 1
    elif key == 'DOWN':  # Move contours down
        contour_offset[1] += 1
    elif key == 'LEFT':  # Move contours left
        contour_offset[0] -= 1
    elif key == 'RIGHT':  # Move contours right
        contour_offset[0] += 1

run()

import pandas as pd
import turtle as t
import math

# --------- Setup -------- #
# Load data
penglings = pd.read_csv('penglings.csv')
x_col = 'flipper_length_mm'
y_col = 'body_mass_g'

# Get data ranges and map
min_x = penglings[x_col].min()
max_x = penglings[x_col].max()
min_y = penglings[y_col].min()
max_y = penglings[y_col].max()
size_col = 'bill_length_mm'
min_size = penglings[size_col].min()
max_size = penglings[size_col].max()

#setup parameters
box_height = 400
box_width = 500
scale_x = box_width / (max_x - min_x)
scale_y = box_height / (max_y - min_y)
x_grid_increment = 10
y_grid_increment = 1000 

#setup turtle and display
t.setup(width=box_width+300, height=box_height+200)
t.speed(0)
t.tracer(0)
t.hideturtle()
t.penup()

#draw background box
t.goto(-box_width/2, -box_height/2) 
t.fillcolor("#ebebeb")
t.begin_fill()
for _ in range(2):
    t.forward(box_width)
    t.left(90)
    t.forward(box_height)
    t.left(90)
t.end_fill()

#--------- draw grid lines --------#
t.pencolor("white")

# Vertical grid lines
x_half_increment = x_grid_increment / 2
first_x_grid = math.ceil(min_x / x_half_increment) * x_half_increment
label_font = ("Arial", 8, "normal")
for grid_val in range(int(first_x_grid), int(max_x) + 1, int(x_half_increment)):
    is_primary = (grid_val % x_grid_increment == 0)
    if is_primary:
        t.pensize(1.5)
    else:
        t.pensize(0.5)
    x_pos = (grid_val - min_x) * scale_x

    t.goto(-box_width/2 + x_pos, -box_height/2)
    t.pendown()
    t.goto(-box_width/2 + x_pos, box_height/2)
    t.penup()

    if is_primary:
        t.pencolor("black")
        t.goto(-box_width/2 + x_pos, -box_height/2 - 20)
        t.write(grid_val, align="center", font=label_font)
        t.pencolor("white")

# Horizontal grid lines 
y_half_increment = y_grid_increment / 2
first_y_grid = math.ceil(min_y / y_half_increment) * y_half_increment
for grid_val in range(int(first_y_grid), int(max_y) + 1, int(y_half_increment)):
    is_primary = (grid_val % y_grid_increment == 0)
    if is_primary:
        t.pensize(1.5) 
    else:
        t.pensize(0.5)
    y_pos = (grid_val - min_y) * scale_y

    t.goto(-box_width/2, -box_height/2 + y_pos)
    t.pendown()
    t.goto(box_width/2, -box_height/2 + y_pos)
    t.penup()

    if is_primary:
        t.pencolor("black")
        t.goto(-box_width/2 - 10, -box_height/2 + y_pos - 5)
        t.write(grid_val, align="right", font=label_font)
        t.pencolor("white")

# ------ Add axis labels -------- #
t.pencolor("black")
axis_label_font = ("Arial", 15, "normal")

t.goto(0, -box_height/2 - 45)
t.write("Flipper Length (mm)", align="center", font=axis_label_font)

t.goto(-box_width/2 - 70, 0)
t.write("Body Mass (g)", align="center", font=axis_label_font)

# ------ plot data points -------- #
species_colors = {
    'Adelie': '#fe9013',
    'Chinstrap': '#9932cc',
    'Gentoo': '#018b8b'
}

for _, row in penglings.iterrows():
    x_val = row[x_col]
    y_val = row[y_col]
    species = row['species']
    bill_len = row[size_col]

    if pd.isna(x_val) or pd.isna(y_val) or pd.isna(bill_len) or pd.isna(species):
        continue

    color = species_colors.get(species)

    # Scale data points to fit in the box
    x_pos = (x_val - min_x) * scale_x - box_width / 2
    y_pos = (y_val - min_y) * scale_y - box_height / 2

    # Scale dot size based on bill length
    min_dot_size = 6
    max_dot_size = 20
    dot_size = min_dot_size + (bill_len - min_size) / (max_size - min_size) * (max_dot_size - min_dot_size)

    # Draw the point
    t.fillcolor(color)
    t.goto(x_pos, y_pos)
    t.dot(dot_size + 2, 'black')
    t.dot(dot_size, color)
    
t.update()
t.done()
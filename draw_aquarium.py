import turtle
import random
import math 

turtle.speed(0)  # Set speed to fastest
screen = turtle.Screen()
screenWidth = screen.window_width()
screenHeight = screen.window_height()
sand_bottom_y = -screenHeight // 2 + screenHeight // 3

# Track positions of fishes, turtles, and stars
fish_positions = []
turtle_positions = []
star_positions = []

def draw_background():
    """Draws the background with water and a sandy ocean floor."""
    turtle.speed(0)

    # Draw water background
    turtle.penup()
    turtle.goto(-screenWidth // 2, screenHeight // 2)
    turtle.pendown()
    turtle.color("lightblue")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screenWidth)
        turtle.right(90)
        turtle.forward(screenHeight * 2 // 3)
        turtle.right(90)
    turtle.end_fill()

    # Draw sandy ocean floor
    floorHeight = screenHeight // 3
    turtle.penup()
    turtle.goto(-screenWidth // 2, -screenHeight // 2 + floorHeight)  # start at the bottom of the water
    turtle.pendown()
    turtle.color("tan")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(screenWidth)
        turtle.right(90)
        turtle.forward(floorHeight)
        turtle.right(90)
    turtle.end_fill()

    # Add sand texture using small dots
    turtle.penup()
    turtle.color("peru")
    for _ in range(300):
        x = random.randint(-screenWidth // 2, screenWidth // 2)
        y = random.randint(-screenHeight // 2, -screenHeight // 2 + floorHeight)
        turtle.goto(x, y)
        turtle.dot(random.randint(2, 5))

def draw_star(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

def draw_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(x, y, size, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_fish(x, y, size, color, facing_right=True):
    draw_circle(x, y, size, color)
    if facing_right:
        draw_triangle(x + size, y, size, color)
    else:
        draw_triangle(x - size, y, size, color)

def draw_oval(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    
    steps = 100  # increase steps for smoother oval
    for step in range(steps + 1):
        angle = 2 * math.pi * step / steps
        oval_x = x + (width / 2) * math.cos(angle)
        oval_y = y + (height / 2) * math.sin(angle)
        turtle.goto(oval_x, oval_y)
    
    turtle.end_fill()

def draw_sea_turtle(x, y, size, color):
    # Draw the turtle's body
    draw_circle(x, y, size, color)
    
    # Draw the turtle's head
    head_size = size / 2
    draw_circle(x, y + size + head_size, head_size, "green")

    # Use draw_oval for flippers and back legs
    flipper_size = size
    offset = 20
    draw_oval(x - size - flipper_size / 2, y - size / 2 + offset, flipper_size, flipper_size / 2, "green")  # Left flipper
    draw_oval(x + size + flipper_size / 2, y - size / 2 + offset, flipper_size, flipper_size / 2, "green")  # Right flipper
    draw_oval(x - size / 2, y - size, size / 2, size / 4, "green")  # Left back leg
    draw_oval(x + size / 2, y - size, size / 2, size / 4, "green")  # Right back leg

def draw_half_circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x - radius, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius, 180)  # Draw a half-circle (180 degrees)
    turtle.end_fill()

def draw_treasure_chest(x, y, width, height, color):
    # Draw the chest body
    draw_rectangle(x, y, width, height, color)

    # Draw the lid using existing rectangle function
    lid_height = height / 3
    draw_rectangle(x, y + height, width, lid_height, color)

    # Draw the rounded top of the lid
    lid_radius = width / 2
    draw_half_circle(x + width / 2 +95, y + height + lid_height -15, lid_radius, color)

    # Draw the lock
    lock_width = width / 5
    lock_height = height / 5
    draw_rectangle(x + width / 2 - lock_width / 2, y + height / 2 - lock_height / 2 - 10, lock_width, lock_height, "gold")

# Function to check if new fish or turtle overlaps with existing ones
def is_overlapping(x, y, size, positions):
    for pos in positions:
        pos_x, pos_y, pos_size = pos
        # Simple check: if the distance between centers is less than the sum of radii, they overlap
        distance = math.sqrt((x - pos_x) ** 2 + (y - pos_y) ** 2)
        if distance < size + pos_size:
            return True
    return False

# Function to check if a star overlaps with fishes
def is_star_overlapping(x, y, size):
    for fish in fish_positions:
        fish_x, fish_y, fish_size = fish
        distance = math.sqrt((x - fish_x) ** 2 + (y - fish_y) ** 2)
        if distance < size + fish_size:
            return True
    return False

# Main drawing commands
draw_background()

# Define new fish colors
fish_colors = ["blue", "red", "orange", "pink", "purple", "cyan", "violet", "turquoise", "magenta"]

# Draw fishes
fish_count = 4
for _ in range(fish_count):
    overlap = True
    while overlap:
        x = random.randint(-screenWidth // 3, screenWidth // 3)
        y = sand_bottom_y + random.randint(50, 300)
        size = random.randint(15, 35)
        color = random.choice(fish_colors)  # Choose a color from the new list
        overlap = is_overlapping(x, y, size, fish_positions)
    draw_fish(x, y, size, color, True)
    fish_positions.append((x, y, size))

# Draw turtles
turtle_count = 2
for _ in range(turtle_count):
    overlap = True
    while overlap:
        x = random.randint(-screenWidth // 3, screenWidth // 3 - 50)
        y = sand_bottom_y - random.randint(30, 100)
        size = random.randint(20, 44)
        overlap = is_overlapping(x, y, size, turtle_positions)
    draw_sea_turtle(x, y, size, "darkgreen")
    turtle_positions.append((x, y, size))

# Draw stars
star_count = 20
for _ in range(star_count):
    overlap = True
    while overlap:
        x = random.randint(-screenWidth // 2, screenWidth // 2 - 150)
        y = random.randint(-screenHeight // 2, screenHeight // 2)
        size = random.randint(25, 50)
        color = random.choice(["blue", "red", "orange", "purple", "pink"])
        overlap = is_star_overlapping(x, y, size)
    draw_star(x, y, size, color)
    star_positions.append((x, y, size))

# Draw treasure chest
draw_treasure_chest(300, -300, 100, 60, "brown")

turtle.done()

import cv2
import turtle
from PIL import ImageGrab
import time

# ==========================================
# SETTINGS
# ==========================================

IMAGE_PATH = "wife.jpg"

DRAW_WIDTH = 400
STEP = 4

# ==========================================
# LOAD IMAGE
# ==========================================

img = cv2.imread(IMAGE_PATH)

if img is None:
    print("Image not found")
    exit()

# ==========================================
# RESIZE
# ==========================================

h, w = img.shape[:2]

ratio = DRAW_WIDTH / w
new_h = int(h * ratio)

img = cv2.resize(img, (DRAW_WIDTH, new_h))

# ==========================================
# GRAYSCALE SKETCH
# ==========================================

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = 255 - gray

blur = cv2.GaussianBlur(invert, (21, 21), 0)

invertedblur = 255 - blur

sketch = cv2.divide(gray, invertedblur, scale=256.0)

# ==========================================
# TURTLE SETUP
# ==========================================

screen = turtle.Screen()

screen.setup(1200, 800)

screen.bgcolor("white")

artist = turtle.Turtle()

artist.speed(0)
artist.hideturtle()
artist.penup()

screen.tracer(0)

# ==========================================
# CENTER
# ==========================================

rows, cols = sketch.shape

x_offset = -cols // 2
y_offset = rows // 2

# ==========================================
# DRAW
# ==========================================

for y in range(0, rows, STEP):

    for x in range(0, cols, STEP):

        pixel = sketch[y, x]

        darkness = 255 - pixel

        if darkness > 60:

            screen_x = x + x_offset
            screen_y = y_offset - y

            artist.goto(screen_x, screen_y)

            if darkness > 200:
                size = 3
            elif darkness > 120:
                size = 2
            else:
                size = 1

            artist.dot(size)

    screen.update()

# ==========================================
# TEXT
# ==========================================

artist.goto(0, -y_offset - 40)

artist.color("red")

artist.write(
    "Made with Love ❤️",
    align="center",
    font=("Arial", 18, "bold")
)

# ==========================================
# SAVE SCREENSHOT
# ==========================================

time.sleep(2)

img = ImageGrab.grab()

img.save("portrait.png")

print("✅ portrait.png saved successfully!")

# ==========================================
# END
# ==========================================

turtle.done()
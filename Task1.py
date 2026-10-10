import numpy as np
import cv2 as cv 
img_name = 'garden.jpeg'
path = './images/'

def show(windows, max_h=450):
    x, y = 0, 50
    for title, image in windows.items():
        ih, iw = image.shape[:2]
        scale = min(1.0, max_h / ih)
        win_w, win_h = int(iw * scale), int(ih * scale)
        cv.namedWindow(title, cv.WINDOW_NORMAL)
        cv.resizeWindow(title, win_w, win_h)
        cv.moveWindow(title, x, y)
        cv.imshow(title, image)
        x += win_w + 10
        if x > 1100:
            x = 0
            y += max_h + 40
    cv.waitKey(0)
    cv.destroyAllWindows()

#  Read the image
img_bgr = cv.imread(path + img_name, cv.IMREAD_COLOR)       # BGR 
img_gray = cv.imread(path + img_name, cv.IMREAD_GRAYSCALE)  # Gray 

#  Error handling 
assert img_bgr is not None, "Cant read image"


print("BGR shape:", img_bgr.shape)
print("Gray shape:", img_gray.shape)

# BGR & Gray 
cv.imshow("BGR", img_bgr)
cv.moveWindow("BGR", 50, 50)

cv.imshow("Gray", img_gray)
cv.moveWindow("Gray", 850, 50)

cv.waitKey(0)
cv.destroyAllWindows()
img_bgr = cv.resize(img_bgr, None, fx=0.5, fy=0.5)
img_gray = cv.resize(img_gray, None, fx=0.5, fy=0.5)

#TASK2
h, w, _ = img_bgr.shape

#  Downscale to 60% 
scale_percent = 60
new_h = int(scale_percent * h / 100)
new_w = int(scale_percent * w / 100)
dim = (new_w, new_h)   #w, h
down_img = cv.resize(img_bgr, dim, interpolation=cv.INTER_AREA)

#  Upscale to 200% 
scale_percent = 200
new_h = int(scale_percent * h / 100)
new_w = int(scale_percent * w / 100)
dim = (new_w, new_h)
up_img = cv.resize(img_bgr, dim, interpolation=cv.INTER_CUBIC)

# Compare shapes 
print(" Task 2 ")
print("Original:", img_bgr.shape)
print("Down 60%:", down_img.shape)
print("Up 200%:", up_img.shape)

#  Display 
cv.namedWindow("Up 200%", cv.WINDOW_NORMAL)
cv.resizeWindow("Up 200%", 460, 614)

cv.imshow("Original", img_bgr)
cv.imshow("Down 60%", down_img)
cv.imshow("Up 200%", up_img)
cv.waitKey(0)
cv.destroyAllWindows()

#TASK3

# only width  100 (height unchanged)
only_width = cv.resize(img_bgr, (100, h), interpolation=cv.INTER_AREA)
# only height  200 (width unchanged)
only_height = cv.resize(img_bgr, (w, 200), interpolation=cv.INTER_AREA)
# both (200, 200)
both = cv.resize(img_bgr, (200, 200), interpolation=cv.INTER_AREA)

print("Task 3")
print("Only width=100 :", only_width.shape)
print("Only height=200:", only_height.shape)
print("Both 200x200   :", both.shape)

show({"Original": img_bgr, "Only width": only_width,  "Only height": only_height, "200x200": both})

#resizing using scake factors x,y
up_linear = cv.resize(img_bgr, None, fx=1.2, fy=1.2, interpolation=cv.INTER_LINEAR)
up_nearest = cv.resize(img_bgr, None, fx=1.2, fy=1.2, interpolation=cv.INTER_NEAREST)
down_linear = cv.resize(img_bgr, None, fx=0.6, fy=0.6, interpolation=cv.INTER_LINEAR)
down_nearest = cv.resize(img_bgr, None, fx=0.6, fy=0.6, interpolation=cv.INTER_NEAREST)

print(" Task 4")
print("Up   x1.2 :", up_linear.shape)
print("Down x0.6 :", down_linear.shape)

show({"Up LINEAR": up_linear, "Up NEAREST": up_nearest,
    "Down LINEAR": down_linear, "Down NEAREST": down_nearest})

# Zoom on a small patch (8x) to make the difference between the methods visible
patch = img_bgr[400:450, 300:350]   # small 50x50 region
patch_linear = cv.resize(patch, None, fx=8, fy=8, interpolation=cv.INTER_LINEAR)
patch_nearest = cv.resize(patch, None, fx=8, fy=8, interpolation=cv.INTER_NEAREST)
show({"Patch LINEAR": patch_linear, "Patch NEAREST": patch_nearest})

#TASK5
cropped = img_bgr[20:200, 50:200]   # rows 20..199, columns 50..199

print("Task5")
print("Original:", img_bgr.shape)
print("Cropped :", cropped.shape)

show({"Original": img_bgr, "Cropped": cropped})
mid_h = h // 2   # midpoint of height
mid_w = w // 2   # midpoint of width

top_left = img_bgr[:mid_h, :mid_w]
top_right = img_bgr[:mid_h, mid_w:]
bottom_left = img_bgr[mid_h:, :mid_w]
bottom_right = img_bgr[mid_h:, mid_w:]

# Stitch: glue each row horizontally, then glue the two rows vertically
top_row = np.hstack((top_left, top_right))
bottom_row = np.hstack((bottom_left, bottom_right))
stitched = np.vstack((top_row, bottom_row))

print("Task6")
print("Block shape:", top_left.shape)
print("Stitched equals original:", np.array_equal(img_bgr, stitched))
show({"Top-Left": top_left, "Top-Right": top_right,
    "Bottom-Left": bottom_left, "Bottom-Right": bottom_right,
    "Stitched": stitched})


#TASK7

center = (w / 2, h / 2)   # center of rotation (x, y)

# positive angle = counter-clockwise
M45 = cv.getRotationMatrix2D(center, 45, 1)
M90 = cv.getRotationMatrix2D(center, 90, 1)
M180 = cv.getRotationMatrix2D(center, 180, 1)

# dsize is (width, height); keeping the same size cuts off the corners
rot45 = cv.warpAffine(img_bgr, M45, (w, h))
rot90 = cv.warpAffine(img_bgr, M90, (w, h))
rot180 = cv.warpAffine(img_bgr, M180, (w, h))

print("Task7")
print("Rotated shapes:", rot45.shape, rot90.shape, rot180.shape)

show({"Original": img_bgr, "Rotate 45": rot45,
    "Rotate 90": rot90, "Rotate 180": rot180})


# Task 8: Rotate + scale in ONE operation vs separate steps

#  rotation (45) and scale (0.5) inside the same matrix
M_both = cv.getRotationMatrix2D(center, 45, 0.5)
one_step = cv.warpAffine(img_bgr, M_both, (w, h))

# Two steps: resize first, then rotate the smaller image around its own center
small = cv.resize(img_bgr, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
sh, sw = small.shape[:2]
M_small = cv.getRotationMatrix2D((sw / 2, sh / 2), 45, 1)
two_steps = cv.warpAffine(small, M_small, (sw, sh))

print("Task8")
print("One step  :", one_step.shape)
print("Two steps :", two_steps.shape)

show({"Original": img_bgr, "Rotate+Scale one step": one_step,
    "Resize then Rotate": two_steps})


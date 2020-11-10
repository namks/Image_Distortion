# Import Library

from PIL import Image
import numpy as np
import csv

# Get path from csv file

image_names = []

with open("FILE_CONTAINING_THE_NAMES_OF_IMAGES", "r") as f:
    csvReader = csv.reader(f)
    next(csvReader, None)   # Skip header

    for line in csvReader:
        image_name = line[0]
        image_names.append("FULL_PATH_TO_IMAGE" + image_name) # Append full path to the list

path_to_save = "PATH_TO_SAVE"

def origin_img(path_to_image, file_number):
    img = Image.open(path_to_image)
    img.save(path_to_save + str(file_number) + ".jpg")

for i in range(len(image_names)):
    origin_img(image_names[i], i)


# Rotation

path_to_save = "PATH_TO_SAVE"

def rotate_img(path_to_image, angle, file_number):
    img = Image.open(path_to_image)
    rotated_img = img.rotate(angle)
    rotated_img.save(path_to_save + str(file_number) + ".jpg")

for i in range(len(image_names)):
    angle = np.random.uniform(-15, 15)
    rotate_img(image_names[i], angle, i)  # Input Angle (Counter-clockwise = positive)


# Translation

path_to_save = "PATH_TO_SAVE"

def translate_img(path_to_image, x, y, file_number):
    img = Image.open(path_to_image)
    # x = x-axis translation, y = y-axis translation
    w, h = img.size
    x = int(np.random.uniform(-w * x / 100, w * x / 100))
    y = int(np.random.uniform(-h * y / 100, h * y / 100))

    translated_img = img.transform(img.size, Image.AFFINE, (1, 0, x, 0, 1, y))
    translated_img.save(path_to_save + str(file_number) + ".jpg")

for i in range(len(image_names)):
    translate_img(image_names[i], 10, 10, i)  # Input x, y (Left/Up = positive)


# Zoom-in and out

def zoom_img(path_to_image, scale, file_number):
    img = Image.open(path_to_image)
    w, h = img.size
    x = w / 2  # midpoint
    y = h / 2  # midpoint
    img = img.crop((x - w / (2 * scale), y - h / (2 * scale), x + w / (2 * scale), y + h / (2 * scale)))
    zoomed_img = img.resize((w, h), Image.LANCZOS)
    zoomed_img.save(path_to_save + str(file_number) + ".jpg")

path_to_save = "PATH_TO_SAVE"

for i in range(len(image_names)):
    zoom_in = np.random.uniform(1.1, 1.3)
    zoom_img(image_names[i], zoom_in, i)  # Zoom-in if scale > 1

path_to_save = "PATH_TO_SAVE"

for i in range(len(image_names)):
    zoom_out = np.random.uniform(0.7, 0.9)
    zoom_img(image_names[i], zoom_out, i)  # Zoom-out if scale < 1


# Low resolution

path_to_save = "PATH_TO_SAVE"

def lower_res_img(path_to_image, scale, file_number):
    img = Image.open(path_to_image)
    w, h = img.size
    low_res_img = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    low_res_img.save(path_to_save + str(file_number) + ".jpg")

for i in range(len(image_names)):
    lower_res_img(image_names[i], 0.5, i)  # Scale should be smaller than 1


# Add noise

path_to_save = "PATH_TO_SAVE"

def noise_img(path_to_image, intensity, file_number):
    img = Image.open(path_to_image)
    w, h = img.size
    img_arr = np.array(img)
    noisy_arr = img_arr + intensity * np.random.randn(h, w)
    noisy_img = Image.fromarray(noisy_arr)
    noisy_img = noisy_img.convert("L")
    noisy_img.save(path_to_save + str(file_number) + ".jpg")
    
for i in range(len(image_names)):
    intensity = np.random.normal(0, 10)
    noise_img(image_names[i], intensity, i)  # Intensity should be greater than 0


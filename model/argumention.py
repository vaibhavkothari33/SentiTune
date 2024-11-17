import os
from PIL import Image, ImageEnhance
import random
import cv2
import numpy as np

def rotate_image(image):
    """Randomly rotate the image within a small range, ensuring it stays portrait."""
    # Get the aspect ratio of the image
    width, height = image.size
    aspect_ratio = width / height
    
    # Only rotate between -30 and 30 degrees to avoid drastic changes in orientation
    angle = random.uniform(-30, 30)
    
    # Rotate the image
    rotated_image = image.rotate(angle, resample=Image.BICUBIC, expand=True)
    
    # Ensure the rotated image retains the same portrait aspect ratio
    rotated_width, rotated_height = rotated_image.size
    if rotated_width > rotated_height:
        rotated_image = rotated_image.transpose(Image.ROTATE_90)
    
    return rotated_image

def flip_image(image):
    """Randomly flip the image horizontally or vertically."""
    flip_type = random.choice(['horizontal', 'vertical'])
    if flip_type == 'horizontal':
        return image.transpose(Image.FLIP_LEFT_RIGHT)
    else:
        return image.transpose(Image.FLIP_TOP_BOTTOM)

def zoom_image(image):
    """Randomly zoom in or out."""
    zoom_factor = random.uniform(0.8, 1.5)  # Random zoom factor between 0.8x to 1.5x
    width, height = image.size
    new_width = int(width * zoom_factor)
    new_height = int(height * zoom_factor)
    
    image = image.resize((new_width, new_height))
    # Crop the center of the image after zooming
    left = (new_width - width) // 2
    top = (new_height - height) // 2
    right = (new_width + width) // 2
    bottom = (new_height + height) // 2
    image = image.crop((left, top, right, bottom))
    
    return image

def crop_image(image):
    """Randomly crop a section of the image."""
    width, height = image.size
    crop_width = random.randint(int(width * 0.6), width)  # Crop between 60% and 100% width
    crop_height = random.randint(int(height * 0.6), height)  # Crop between 60% and 100% height
    left = random.randint(0, width - crop_width)
    top = random.randint(0, height - crop_height)
    right = left + crop_width
    bottom = top + crop_height
    return image.crop((left, top, right, bottom))

def color_jitter(image):
    """Adjust brightness, contrast, and saturation."""
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))  # Randomly adjust brightness
    
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))  # Randomly adjust contrast
    
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))  # Randomly adjust color saturation
    
    return image

def translate_image(image):
    """Randomly translate (shift) the image horizontally or vertically."""
    width, height = image.size
    max_translation = int(width * 0.2)  # Limit translation to 20% of image width/height
    tx = random.randint(-max_translation, max_translation)
    ty = random.randint(-max_translation, max_translation)
    
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    image = cv2.warpAffine(np.array(image), matrix, (width, height))
    return Image.fromarray(image)

def augment_image(image_path, output_dir):
    """Apply a series of augmentations to an image and save the results."""
    image = Image.open(image_path)
    
    # Apply transformations
    augmented_images = [
        # rotate_image(image),
        flip_image(image),
        zoom_image(image),
        crop_image(image),
        color_jitter(image),
        # translate_image(image)
    ]
    
    # Save augmented images
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    base_name = os.path.basename(image_path).split('.')[0]
    for i, augmented_image in enumerate(augmented_images):
        output_path = os.path.join(output_dir, f"{base_name}_augmented_{i+1}.jpg")
        augmented_image.save(output_path)
        print(f"Saved augmented image to {output_path}")

def process_directory(input_dir, output_dir):
    """Process all images in a directory."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for subfolder in os.listdir(input_dir):
        subfolder_path = os.path.join(input_dir, subfolder)
        
        if os.path.isdir(subfolder_path):
            # Process the 'photo' folder inside each emotion folder (angry, sad, happy, calm)
            photo_folder = os.path.join(subfolder_path)
            output_subfolder = os.path.join(output_dir, subfolder)
            
            for image_name in os.listdir(photo_folder):
                image_path = os.path.join(photo_folder, image_name)
                if os.path.isfile(image_path):
                    augment_image(image_path, output_subfolder)

# Example usage
input_directory = "AugmentedData"  # Directory with angry, sad, happy, calm subfolders
output_directory = "AugmentedData"  # Directory to save augmented images
process_directory(input_directory, output_directory)

# Install TensorFlow, TensorFlow Hub, and Matplotlib
!pip install tensorflow tensorflow_hub matplotlib

# Import essential Python libraries
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# Function to load and prepare the image
def load_image(image_path, max_dim=512):
    img = Image.open(image_path).convert('RGB')
    img = img.resize((max_dim, max_dim))
    img = tf.keras.utils.img_to_array(img)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]
    return img

# Upload your images (content and style)
from google.colab import files
uploaded = files.upload()

# Upload your images (content and style)
from google.colab import files
uploaded = files.upload()

# Load the uploaded images (update filenames accordingly)
content_image = load_image("pretty-lady-model-short-blue-dress-hat-with-retrocamera-her-hands-white.jpg")   # Replace with actual filename
style_image = load_image("watercolor-moon-illustration.jpg")       # Replace with actual filename

# Load the pre-trained neural style transfer model from TensorFlow Hub
model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')

# Apply the style to the content image
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]

# Function to display all images side by side
def show_images(content, style, stylized):
    plt.figure(figsize=(15, 5))
    titles = ['Content Image', 'Style Image', 'Stylized Image']
    for i, img in enumerate([content, style, stylized]):
        plt.subplot(1, 3, i+1)
        plt.imshow(tf.squeeze(img))
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

# Call the function to show images
show_images(content_image, style_image, stylized_image)

# Save and download the stylized image
# Remove the batch dimension using tf.squeeze
result = tf.keras.utils.array_to_img(tf.squeeze(stylized_image))
result.save("stylized_output.jpg")
files.download("stylized_output.jpg")
      

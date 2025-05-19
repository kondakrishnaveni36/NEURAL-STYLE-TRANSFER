# NEURAL-STYLE-TRANSFER

COMPANY CODTECH IT SOLUTIONS

NAME: KONDA KRISHNAVENI

INTERN ID: ID:CODF46

ARTIFICIAL INTELLIGENCE MARKUP LANGUAGE

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

As part of my CodTech AIML Internship, Task 3 involved building a Neural Style Transfer (NST) model using Python. The goal of this project was to apply the artistic style of one image to the content of another image, generating a new, visually stylized image. This task combines computer vision and deep learning concepts and demonstrates how neural networks can learn the artistic patterns and textures from one image and apply them to another. NST is widely used in creative fields, mobile apps, and image editing tools to transform normal photos into artistic renditions.

To complete this project, I first explored the concept of neural style transfer, which was originally proposed in a research paper by Gatys et al. The idea is to extract the content features of one image and the style features of another using a pre-trained convolutional neural network (CNN), and then combine them to produce a stylized image. For simplicity and efficiency, I used TensorFlow Hub’s pre-trained model called “Arbitrary Image Stylization” which allows applying style to any content image without training from scratch.

The main tasks performed in this project included:

1. Setting up the environment and installing required libraries like tensorflow, tensorflow_hub, PIL (Python Imaging Library), matplotlib, and using google.colab.files for image uploads.


2. Implementing functions to load and preprocess both the content and style images. I resized the images and normalized their pixel values to ensure compatibility with the model.


3. Loading the pre-trained style transfer model from TensorFlow Hub. This model takes two inputs — a content image and a style image — and returns a stylized image.


4. Applying the model to generate the output image, and using matplotlib to visually display the original content image, style image, and the final stylized result.


5. Making the script more interactive and user-friendly by allowing users to upload their own images directly from Google Colab.



For this project, I used Google Colab as my main editor platform. It allowed me to run the code without any local installation and take advantage of free GPU support. Colab also made it easier to upload images and preview outputs directly in the browser, which was especially helpful since I was working on a mobile device during the internship. Once I finalized the code and tested it with different image combinations, I converted the notebook into a .py script as per the submission requirement and uploaded it to my GitHub repository.

This project has several real-world applications, including photo editing apps, artistic filters, AI-powered creative tools, and more. By completing this task, I learned how to use powerful pre-trained models to perform complex visual transformations with very little code. I also gained hands-on experience in handling images, working with TensorFlow Hub, and deploying deep learning applications in a lightweight and user-friendly way. Uploading the .py script to GitHub ensures the project is accessible and easy to reuse for others, fulfilling the requirement stated in the task instructions.

OUTPUT :


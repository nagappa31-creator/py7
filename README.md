Here is a clean, professional, and beginner-friendly README.md for your Image Resizer Tool project.


---

📄 README.md — Image Resizer Tool (Python + Pillow)

🖼️ Project Title

Batch Image Resizer and Converter using Python & Pillow


---

📘 Description

This project is a simple Python tool that automatically resizes and converts all images in a folder.
It is useful for:

Reducing image sizes

Converting formats (PNG → JPG, JPG → WEBP, etc.)

Preparing images for web uploads

Batch processing instead of resizing manually


The script uses the Pillow library (PIL) for image manipulation and os module for file handling.


---

🔧 Features

✔ Resize all images in a folder
✔ Convert image format (JPEG, PNG, WEBP)
✔ Automatic output folder creation
✔ Supports .png, .jpg, .jpeg, .webp
✔ Easy to customize width, height, and format
✔ Error handling included


---

📂 Project Structure

📁 image-resizer-tool
│
├── image_resizer.py          # Main script (your code)
│
├── 📁 input_images           # Put original images here
│
└── 📁 output_images          # Resized images appear here


---

⚙️ Installation

✓ Install Python

Check Python version:

python --version

✓ Install Pillow

pip install pillow

If pip doesn’t work:

py -m pip install pillow


---

▶️ How to Run the Tool

1. Put all your original images inside the folder:



input_images/

2. Edit the settings inside the script if needed:



new_width = 800
new_height = 600
convert_to = "JPEG"

3. Run the script:



python image_resizer.py

4. Resized images will be automatically saved in:



output_images/


---

🧠 What You Learn from This Project

Using Pillow library

Opening, resizing, and saving images

Looping through folders with os.listdir()

Handling file paths

Automating repetitive image tasks



---

🚀 Future Enhancements (Optional)

If you want to extend the tool, you can add:

Maintain aspect ratio automatically

Resize by percentage

Set max-width or max-height only

Add watermark

Convert all images to grayscale

GUI version using Tkinter


I can help you add any of these—just ask!


---

👨‍💻 Author

Created by Pranathi N 


---


import os
from PIL import Image

# ---------- SETTINGS ----------
input_folder = "input_images"        # Folder containing original images
output_folder = "output_images"      # Folder where resized images will be saved

new_width = 800                      # Width you want
new_height = 600                     # Height you want
convert_to = "JPEG"                  # Options: "JPEG", "PNG", "WEBP" (optional)
# -------------------------------

def resize_images():
    # Create output folder if not exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            img_path = os.path.join(input_folder, filename)
            
            try:
                img = Image.open(img_path)
                
                # Resize image
                img_resized = img.resize((new_width, new_height))

                # Construct save path
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_resized.{convert_to.lower()}"
                save_path = os.path.join(output_folder, new_filename)

                # Save resized/converted image
                img_resized.save(save_path, convert_to)

                print(f"✔ Saved: {new_filename}")

            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

    print("\nCompleted resizing all images!")

# Run the tool
resize_images()
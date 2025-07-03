import os
from PIL import Image

# Configuration
input_folder = "images_in"
output_folder = "images_out"
output_size = (800, 600)  # width, height
output_format = "JPEG"    # or "PNG", etc.

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        input_path = os.path.join(input_folder, filename)
        with Image.open(input_path) as img:
            img_resized = img.resize(output_size, Image.LANCZOS)
            base, _ = os.path.splitext(filename)
            # Always use .jpg for JPEG output, .png for PNG, etc.
            ext = "jpg" if output_format.upper() == "JPEG" else output_format.lower()
            output_path = os.path.join(output_folder, f"{base}.{ext}")
            img_resized.save(output_path, output_format)
            print(f"Saved: {output_path}")
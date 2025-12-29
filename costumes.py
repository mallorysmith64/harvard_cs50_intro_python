import sys
from PIL import Image

# Skip the script name (argv[0])
image_files = sys.argv[1:]

if len(image_files) < 2:
    print("Please provide at least two image files.")
    sys.exit(1)

images = []

for arg in image_files:
    try:
        image = Image.open(arg)
        images.append(image)
    except Exception as e:
        print(f"Could not open {arg}: {e}")

# Save all images, skipping the first one in append_images 
# because it's already the 'base' image (images[0])
images[0].save(
    "costumes.gif", 
    save_all=True, 
    append_images=images[1:], 
    duration=200,  # Fixed typo
    loop=0
)

print("GIF created successfully!")
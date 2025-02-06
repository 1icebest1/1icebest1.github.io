import os
import json

image_dir = "images"
image_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp")

images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(image_extensions)]

with open("images.json", "w") as f:
    json.dump(images, f, indent=4)

print("Файл images.json оновлено.")

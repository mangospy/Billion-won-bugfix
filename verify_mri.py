from PIL import Image
import imagehash
import os

# Precomputed phash of your secret MRI
SECRET_IMAGE_HASH = imagehash.hex_to_hash("952e1a796a786963")

def verify_image(img_path, threshold=10):
    img = Image.open(img_path)
    img_hash = imagehash.phash(img)
    diff = SECRET_IMAGE_HASH - img_hash

    if diff <= threshold:
        print("✅ Correct MRI found!")
        secret = os.getenv("SECRET_CODE")  # fetched from GitHub Secret
        print("🔐 Secret Code:", secret)
    else:
        print("❌ Wrong MRI. Try again!")

if __name__ == "__main__":
    img_path = input("Enter path of your MRI image: ")
    verify_image(img_path)

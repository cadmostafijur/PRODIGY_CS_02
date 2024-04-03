from PIL import Image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # encrypt each color channel using XOR operation with the key
            r ^= key
            g ^= key
            b ^= key
            # update the pixel value with the  color channels
            pixels[x, y] = (r, g, b)

    encrypted_image_path = "encrypted_image.png"
    img.save(encrypted_image_path)
    print("Image encrypted and saved as:", encrypted_image_path)
def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # decrypt each color channel
            r ^= key
            g ^= key
            b ^= key
            # update the pixel value 
            pixels[x, y] = (r, g, b)

    decrypted_image_path = "decrypted_image.png"
    img.save(decrypted_image_path)
    print("Image decrypted and saved as:", decrypted_image_path)

#test:
image_path = "teddy.jpg"
encryption_key = 128
encrypt_image(image_path, encryption_key)

encrypted_image_path = "encrypted_image.png"
decrypt_image(encrypted_image_path, encryption_key)

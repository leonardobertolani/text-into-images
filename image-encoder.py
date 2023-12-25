from PIL import Image
from bitarray import bitarray
from math import ceil, sqrt


def text_in_bitarray(file_path):
    with open(file_path, 'r') as file:
        text_content = file.read()

    # Convert it into a bitarray object
    bits = bitarray()
    bits.frombytes(text_content.encode('utf-8'))

    return bits



def bitarray_in_image(image, height, width, bits):

    for y in range(height):
        for x in range(width):

            actual_image_index = y * width + x
            image.putpixel((x, y), int(bits[actual_image_index]))




file_path = 'text.txt'
bits = text_in_bitarray(file_path)           # Getting the bits

width = height = ceil(sqrt(len(bits)))          # Setting width and height based on the number of bits
bits.extend([0] * (width*height - len(bits)))   # Extending the bits array so that bits and image have same dimension

img = Image.new('1', (width, height))
bitarray_in_image(img, height, width, bits)   # Getting the image


img.save("image.png", compress_level=0)   # No compression so that we don't lose data
img.show()

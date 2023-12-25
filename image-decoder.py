from PIL import Image
from bitarray import bitarray



def image_to_bitarray(image_path):
    img = Image.open(image_path, mode='r')

    pix_val = list(img.getdata())
    pix_val = [1 if x == 255 else 0 for x in pix_val]

    return bitarray(pix_val)




def bitarray_to_text(bits):

    # Preparing the bits array to be converted
    padding_length = 8 - len(bits) % 8
    bits.extend([0] * padding_length)

    byte_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]

    ascii_characters = [chr(int(chunk.to01(), 2)) for chunk in byte_chunks]

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(''.join(ascii_characters))

    return ''.join(ascii_characters)





image_path = 'image.png'
bits = image_to_bitarray(image_path)
text = bitarray_to_text(bits)

print(text)


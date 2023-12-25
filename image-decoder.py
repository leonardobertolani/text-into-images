from PIL import Image
import io
from bitarray import bitarray

def image_to_bits(image_path):
    img = Image.open(image_path, mode='r')

    pix_val = list(img.getdata())
    pix_val = [1 if x == 255 else 0 for x in pix_val]

    return bitarray(pix_val)








def bits_to_ascii(bits):
    # Assicurati che la lunghezza della sequenza di bit sia un multiplo di 8
    padding_length = (8 - len(bits) % 8) % 8
    bits.extend([False] * padding_length)

    # Dividi la sequenza di bit in gruppi di 8
    byte_chunks = [bits[i:i+8] for i in range(0, len(bits), 8)]

    # Converti ciascun gruppo di 8 bit in un numero intero e poi in un carattere ASCII
    ascii_characters = [chr(int(chunk.to01(), 2)) for chunk in byte_chunks]

    # Restituisci la stringa risultante
    return ''.join(ascii_characters)





# Esempio di utilizzo
image_path = 'image.png'  # Sostituisci con il percorso della tua immagine
bits = image_to_bits(image_path)

# Stampa i primi 64 bit a titolo di esempio
print(bits[67:])

utf8_string = bits_to_ascii(bits)

print("UTF-8 String:", utf8_string)








#00001011100100110111100100000011011010110100100100000011001100111010100
#





from PIL import Image
from bitarray import bitarray


def text_to_bits(text):
    bits = bitarray()
    bits.frombytes(text.encode('utf-8'))
    return bits


def read_text_file_bits(file_path):
    with open(file_path, 'r') as file:
        # Leggi il contenuto del file di testo
        text_content = file.read()

    # Converti il testo in bit
    bits = text_to_bits(text_content)

    return bits


# Esempio di utilizzo
file_path = 'testo.txt'  # Sostituisci con il percorso del tuo file di testo
bits = read_text_file_bits(file_path)

# Stampa i primi 64 bit a titolo di esempio
print(bits[67:])
print(len(bits))






# Stringa di bit di esempio (8x8)
bit_string = "00110000" \
             "01111000" \
             "10001100" \
             "10001100" \
             "10011100" \
             "01111100" \
             "00100100" \
             "00011000"

# Dimensioni dell'immagine
'''
width = int(len(bits)/10)
height = int(len(bits)/width) + len(bits) % width
'''
width = 217
height = 217

# Creazione di un oggetto immagine
img = Image.new('1', (width, height))

# Iterazione attraverso la stringa di bit e impostazione dei pixel dell'immagine
for y in range(height):
    for x in range(width):
        if len(bits) > (y * width + x):
            # Estrai il bit corrispondente dalla stringa di bit
            bit = int(bits[y * width + x])
            # Imposta il pixel nell'immagine
            img.putpixel((x, y), bit)
        else:
            img.putpixel((x, y), 0)

# Salva l'immagine
img.save("image.png", compress_level=0)

# Mostra l'immagine
img.show()




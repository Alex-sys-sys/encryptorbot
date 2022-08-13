import qrcode
from PIL import Image, ImageDraw
import math

en_english = {
    "a": (3, 25), "b": (16, 23), "c": (18, 11), "d": (20, 20), "e": (6, 8), "f": (8, 7),
    "g": (17, 19), "h": (11, 12), "i": (9, 3), "j": (22, 24), "k": (21, 10),
    "l": (1, 18), "m": (15, 2), "n": (23, 1), "o": (7, 6), "p": (25, 13),
    "q": (2, 22), "r": (4, 16), "s": (14, 15), "t": (10, 4), "u": (13, 9),
    "v": (26, 14), "w": (19, 26), "x": (24, 17), "y": (5, 21), "z": (12, 5)}

de_english = {
    (3, 25): "a", (16, 23): "b", (18, 11): "c", (20, 20): "d", (6, 8): "e",
    (8, 7): "f", (17, 19): "g", (11, 12): "h", (9, 3): "i", (22, 24): "j",
    (21, 10): "k", (1, 18): "l", (15, 2): "m", (23, 1): "n", (7, 6): "o",
    (25, 13): "p", (2, 22): "q", (4, 16): "r", (14, 15): "s", (10, 4): "t",
    (13, 9): "u", (26, 14): "v", (19, 26): "w", (24, 17): "x", (5, 21): "y", (12, 5): "z"}

en_russian = {
    "а": (14, 9), "б": (8, 17), "в": (7, 25), "г": (5, 16), "д": (8, 20), "е": (23, 1),
    "ж": (23, 7), "з": (14, 2), "и": (2, 15), "й": (11, 24), "к": (12, 7), "л": (8, 16),
    "м": (4, 6), "н": (2, 21), "о": (13, 16), "п": (16, 13), "р": (21, 2), "с": (5, 22),
    "т": (19, 11), "у": (20, 20), "ф": (18, 26), "х": (24, 20), "ц": (26, 20), "ч": (22, 13),
    "ш": (12, 10), "щ": (23, 8), "ъ": (26, 10), "ы": (5, 16), "ь": (12, 12), "э": (12, 3),
    "ю": (17, 22), "я": (8, 14), "ѐ": (7, 22), "ё": (9, 6)}

de_russian = {(14, 9): "а", (8, 17): "б", (7, 25): "в", (5, 16): "г", (8, 20): "д", (23, 1): "е",
              (23, 7): "ж", (14, 2): "з", (2, 15): "и", (11, 24): "й", (12, 7): "к", (8, 16): "л",
              (4, 6): "м", (2, 21): "н", (13, 16): "о", (16, 13): "п", (21, 2): "р", (5, 22): "с",
              (19, 11): "т", (20, 20): "у", (18, 26): "ф", (24, 20): "х", (26, 20): "ц", (22, 13): "ч",
              (12, 10): "ш", (23, 8): "щ", (26, 10): "ъ", (5, 16): "ы", (12, 12): "ь", (12, 3): "э",
              (17, 22): "ю", (8, 14): "я", (7, 22): "ѐ", (9, 6): "ё", }

Morse_code = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ', ': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', ' ': '.-.-.', '\n': '.-.-.'}

eng_alph = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

rus_alph = [
    "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

Morse_code_back = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
    '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1',
    '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9', '-----': '0',
    '--..--': ', ', '.-.-.-': '.', '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')',
    '.-.-.': ' '}

Ru_Morse_code = {'а': '.-', 'б': '-...', 'в': '.--', 'г': '--.', 'д': '-..', 'е': '.', "ё": ".-.-.-.",
                 'ж': '...-', 'з': '--..', 'и': '..', 'й': '.---', 'к': '-.-', 'л': '.-..',
                 'м': '--', 'н': '-.', 'о': '---', 'п': '.--.', 'р': '.-.', 'с': '...',
                 'т': '-', 'у': '..-', 'ф': '..-.', 'х': '....', 'ц': '-.-.', 'ч': '---.', 'ш': '----',
                 'щ': '--.-', 'ъ': '.--.-.', 'ы': '-.--', 'ь': '-..-', 'э': '..-..', 'ю': '..--', 'я': '.-.-',
                 '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----', ', ': '--..--', '.': '.-.-.-',
                 '?': '..--..', '/': '-..-.', '-': '-....-',
                 '(': '-.--.', ')': '-.--.-', ' ': '.-.-.', '\n': '.-.-.'
                 }

Ru_Morse_code_back = {".-": "а", "-...": "б", ".--": "в", "--.": "г", "-..": "д", ".": "е", ".-.-.-.": "ё",
                      "...-": "ж", "--..": "з", "..": "и", ".---": "й", "-.-": "к", ".-..": "л",
                      "--": "м", "-.": "н", "---": "о", ".--.": "п", ".-.": "р", "...": "с", "-": "т",
                      "..-": "у", "..-.": "ф", "....": "х", "-.-.": "ц", "---.": "ч", "----": "ш",
                      "--.-": "щ", ".--.-.": "ъ", "-.--": "ы", "-..-": "ь", "..-..": "э",
                      "..--": "ю", ".-.-": "я", '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
                      '-....': '6', '--...': '7',
                      '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.', '..--..': '?',
                      '-..-.': '/',
                      '-....-': '-', '-.--.': '(', '-.--.-': ')', '.-.-.': ' '}


def morse_encode(text):
    encoded_text = ''
    for i in text:
        try:
            encoded_text += Morse_code[i.upper()]
            encoded_text += ' '
        except KeyError:
            try:
                encoded_text += Ru_Morse_code[i.lower()]
                encoded_text += ' '
            except KeyError:
                encoded_text += i
                encoded_text += ' '
    return encoded_text


def morse_decode(text, lang):
    decoded_text = ''
    for i in text.split():
        if lang == 'English':
            try:
                decoded_text += Morse_code_back[i.upper()]
            except KeyError:
                decoded_text += i
        elif lang == 'Russian':
            try:
                decoded_text += Ru_Morse_code_back[i.lower()]
            except KeyError:
                decoded_text += i
        else:
            decoded_text += i
    return decoded_text


def encode_to_qr(text):
    pass


def encode_caesar(text, shift):
    encoded = []
    if text != '':
        if text[0].lower() in eng_alph:
            for i in text:
                if i.lower() in eng_alph:
                    encoded.append(eng_alph[(eng_alph.index(i) + shift)
                                            % len(eng_alph)])
                else:
                    encoded.append(i)
            return ''.join(encoded)
        elif text[0].lower() in rus_alph:
            for i in text:
                if i.lower() in rus_alph:
                    encoded.append(rus_alph[(rus_alph.index(i.lower()) + shift)
                                            % len(rus_alph)])
                else:
                    encoded.append(i)
            return ''.join(encoded)
        else:
            return text


def encode_caesar_word(text, shift):
    text = [i for i in text if i.isalpha()]
    if text == []:
        return ''
    shift = shift % len(text)
    ins = text[-shift:len(text)]
    del text[-shift:len(text)]
    text = ''.join(text)
    text = ''.join(ins) + text
    return text


def decode_caesar_word(text, shift):
    text = [i for i in text]
    shift = shift % len(text)
    ins = text[0:shift]
    del text[0:shift]
    text = ''.join(text)
    text = text + ''.join(ins)
    return text


def decode_caesar(text, shift):
    decoded = []
    if text != '':
        if text[0].lower() in eng_alph:
            for i in text:
                if i in eng_alph:
                    index = (eng_alph.index(i) - shift) \
                            % len(eng_alph)
                    decoded.append(eng_alph[index])
                else:
                    decoded.append(i)
            return ''.join(decoded)
        elif text[0].lower() in rus_alph:
            for i in text:
                if i in rus_alph:
                    index = (rus_alph.index(i) - shift) \
                            % len(rus_alph)
                    decoded.append(rus_alph[index])
                else:
                    decoded.append(i)
            return ''.join(decoded)


def encode_picture(text):
    text_it = ''
    text_bi = []
    for i in text.lower():
        if i.lower() in en_english:
            text_it += i
            text_bi = [en_english[i] for i in text_it.lower()]
        elif i.lower() in en_russian:
            text_it += i
            text_bi = [en_russian[i] for i in text_it.lower()]
    text_bi.sort()
    im = Image.new('RGB', (26, 26), (255, 255, 255))
    drawer = ImageDraw.Draw(im)
    drawer.polygon(text_bi, (0, 0, 0))
    for i in text_bi:
        if i in de_english:
            drawer.point(i, (0, text_it.find(de_english[i]) + 1, 0))
            drawer.point((0, 0), (255, 0, 0))
        else:
            drawer.point(i, (0, text_it.find(de_russian[i]) + 1, 0))
    im.show()


def decode_picture(file_name):
    im = Image.open(file_name)
    pixels = im.load()
    text = []
    for i in range(1, 26):
        for j in range(1, 26):
            if pixels[i, j] != (0, 0, 0, 255) and \
                    pixels[i, j] != (255, 255, 255, 255):
                if len(text) == 0:
                    if pixels[0, 0] == (255, 0, 0, 255):
                        text.append(de_english[(i, j)])
                    else:
                        text.append(de_russian[(i, j)])
                else:
                    if pixels[0, 0] == (255, 0, 0, 255):
                        text.insert(pixels[i, j][1] - 1,
                                    de_english[(i, j)])
                    else:
                        text.insert(pixels[i, j][1] - 1,
                                    de_russian[(i, j)])
    return ''.join(text)


def encode_friend(text, cipher):
    encoded = []
    for word in text.split():
        word = encode_caesar(word, int(cipher[0]))
        word = encode_caesar_word(word, int(cipher[1]))
        word += ' '
        try:
            # for i in word:
            #     a = ord(i)
            #     a **= int(cipher[2])
            #     a *= int(cipher[3])
            #     a += int(cipher[4])
            #     word += str(a)
            #     word += '|'
            word = [str(ord(i) ** int(cipher[2]) * int(cipher[3]) +
                        int(cipher[4])) for i in word]
        except KeyError:
            pass
        encoded.append('|'.join(word))
    return '-'.join(encoded)


def decode_friend(text, cipher):
    decoded = []
    for word in text.split('-'):
        word += ' '
        try:
            for a in word.split('|'):
                a = int(a)
                a -= int(cipher[4])
                a //= int(cipher[3])
                a = int(math.pow(a, 1 / int(cipher[2])))
                word += chr(a + 1)
            # word = [chr(int(math.pow((int(i) - int(cipher[4])) // int(cipher[3]), 1 / int(cipher[2])))) for i in
            #         word.split('|')]
            word = word.split()[-1]
            word = decode_caesar_word(word, int(cipher[1]))
            word = decode_caesar(word, int(cipher[0]))
            decoded.append(word)
        except Exception:
            pass
    if decoded is None or decoded == []:
        return ''
    return ' '.join(decoded)


def encode_xor(text, num):
    encoded = ''
    for i in text:
        encoded += str(ord(i) ^ num)
        encoded += '-'
    return encoded[:-1]


def decode_xor(text, num):
    decoded = ''
    for i in text.split('-'):
        decoded += chr(num ^ int(i))
    return decoded

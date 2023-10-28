from sound import audio
import time


def readtext(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    while '\n' in lines:
        lines.remove('\n')
    while '\t' in lines:
        lines.remove('\t')

    for i in range(0, len(lines)):
        lines[i] = lines[i].lower().replace('\n', ' ').replace('\t', '')
    return lines


def translate_file(lines: list):
    letters = []
    translation = ""
    letters_translation = {
        'a': ".-",
        'b': "-...",
        'c': "-.-.",
        'd': "-..",
        'e': ".",
        'f': "..-.",
        'g': "--.",
        'h': "....",
        'i': "..",
        'j': ".---",
        'k': "-.-",
        'l': ".-..",
        'm': "--",
        'n': "-.",
        'o': "---",
        'p': ".--.",
        'q': "--.-",
        'r': ".-.",
        's': "...",
        't': "-",
        'u': "..-",
        'v': "...-",
        'w': ".--",
        'x': "-..-",
        'y': "-.--",
        'z': "--..",
        '/': "/"

    }

    for line in lines:

        for i in list(line):
            letters.append(i)

    for i in range(0, len(letters)):
        if letters[i] == ' ':
            letters[i] = '/'

    for letter in letters:

        translation = translation + letters_translation[letter]
        translation = translation + ' '

    return translation


def translate_user_input(lines):

    lines = list(lines)
    translation = translate_file(lines)
    return translation


def sound_translation(translation: str):
    sound_duration = {
        '.': 0.3,
        '-': 0.9,
        ' ': 0.0,
        '/': 0.0
    }
    word_space = False

    for i in range(0, len(translation)-1):
        if translation[i] == '/':
            time.sleep(0.5)
            continue
        print(translation[i])
        audio(sound_duration[translation[i]])


def main():
    translation = ''

    if int(input("[1]Translate file\n[2]Enter text\nSelect an option:")) == 1:
        path = input("Write the file path: ")
        translation = translate_file(readtext(path))
        print(translation)

        sound_translation(translation)

    else:
        lines = input("Enter the text: ").lower()
        translation = translate_user_input(lines)
        sound_translation(translation)
        print(translation)


if __name__ == '__main__':
    main()

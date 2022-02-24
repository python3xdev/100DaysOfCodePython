print('enter some text to convert in into morse code!'.title())

morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
valid_chars = [k for k in morse_code_dict]

running = True

while running:
    user_text = input('Convert: ')
    # result = [morse_code_dict[char.upper()] for char in user_text if char in valid_chars else char]
    result = [char if char not in valid_chars else morse_code_dict[char] for char in user_text.upper()]
    print(' '.join(result))
    again = input('Do you want to go again? (Y/N): ')
    if again[0].lower() != 'y':
        running = False
        print('Thank you for using my program!')
    else:
        print('-' * 20)

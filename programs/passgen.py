import random
import string



def passgen(char_count):
    lowascii_char = string.ascii_lowercase
    upascii_char = string.ascii_uppercase
    punct_char = string.punctuation
    digit_chat = string.digits
    all_chars = [lowascii_char, upascii_char, punct_char, digit_chat]

    # char_count = 14
    # while char_count not in range(12, 21):
    #     msg_len = 'Wybierz liczbę znaków hasła (12-20)'
        

    passw = ""
    randomized_list = []
    while len(randomized_list) < char_count:
        for char_type in all_chars:
            randomized_list += random.sample(char_type, 1)
        random.shuffle(randomized_list)
        ready_pass = ''.join(randomized_list)[:char_count]

    ready_pass = f"Your {char_count} char password is {ready_pass}"

    return ready_pass

# print(passgen(15))
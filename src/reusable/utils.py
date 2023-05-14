from string import ascii_letters
from random import sample 


def fake_generate():
    chars = f'{ascii_letters}0123456789'
    return ''.join(sample(chars,12))
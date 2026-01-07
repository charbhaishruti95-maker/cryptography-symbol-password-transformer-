from blocks import symbols
from utils import generate_salt

def transform_password(password, user_id, rounds=2):
    salt = generate_salt(user_id)
    salted_input = password + salt
    ascii_codes = [ord(c) for c in salted_input]
    final_password = []

    for i, char in enumerate(password):
        block = symbols.get(char, ['*', '%', '#', '&', '@'])
        block_len = len(block)
        index = (i * ascii_codes[i % len(ascii_codes)]) % block_len

        # optional rounds for extra mixing
        for r in range(rounds):
            index = (index * (r + 1) + ascii_codes[(i + r) % len(ascii_codes)]) % block_len
        
        final_password.append(block[index])
    
    return ''.join(final_password)

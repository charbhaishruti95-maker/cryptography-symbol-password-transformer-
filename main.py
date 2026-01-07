from transform import transform_password

if __name__ == "__main__":
    print("=== Cryptography-Inspired Symbol Password Transformer ===")
    user_password = input("Enter your password: ")
    user_id = input("Enter your user ID (for salt): ")

has_upper=any(ch.isupper() for ch in user_password)
has_lower=any(ch.islower() for ch in user_password)
has_digit=any(ch.isdigit() for ch in user_password)
has_special= any (ch in "@_&$%*&^_>.:;"for ch in user_password)

if len(user_password)>=8 and has_upper and has_lower and has_special and has_digit:
    print("hurrah you have an stron password")
    transformed = transform_password(user_password, user_id)
    print("Generated secure password:", transformed)

else:
    print("ah! pick another one ")
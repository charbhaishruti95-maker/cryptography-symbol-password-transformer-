import hashlib

def generate_salt(user_id):
    """Generate a user-specific salt"""
    return hashlib.sha256(user_id.encode()).hexdigest()

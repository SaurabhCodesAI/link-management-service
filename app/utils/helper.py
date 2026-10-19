import string
import secrets

def generate_identifier() -> str:
    alphabet = string.ascii_letters + string.digits
    candidate = "".join(secrets.choice(alphabet) for _ in range(6))
    return candidate

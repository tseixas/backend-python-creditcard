from cryptography.fernet import Fernet
from app.config import settings


def encrypt(value):
    key = settings.key_cryptography
    f = Fernet(key)

    return f.encrypt(value.encode())

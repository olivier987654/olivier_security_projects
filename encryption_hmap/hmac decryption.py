# hmac decryption

import hmac
import hashlib

def hmac_decrypt(key, message, hmac_digest):
    return hmac.new(key, message, hashlib.sha256).hexdigest() == hmac_digest

if __name__ == '__main__':
    key = b'key'
    message = b'message'
    hmac_digest = b'f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0c8'
    print(hmac_decrypt(key, message, hmac_digest))
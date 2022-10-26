# hmac encryption this is a SHA256 hash

import hmac
import hashlib

def hmac_encrypt(key, message):
    return hmac.new(key, message, hashlib.sha256).hexdigest()

if __name__ == '__main__':
    key = b'key'
    message = b'message'
    print(hmac_encrypt(key, message))

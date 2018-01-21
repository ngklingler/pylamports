import secrets
import hashlib


def hashEncode(number):
    return hashlib.sha256(str(number).encode()).hexdigest()


class key:

    def __init__(self):
        self.secretKey = []
        self.publicKey = []
        for i in range(256):
            self.secretKey.append((hex(secrets.randbits(256))[2:],
                                   hex(secrets.randbits(256))[2:]))
            self.publicKey.append((hashEncode(self.secretKey[i][0]),
                                   hashEncode(self.secretKey[i][1])))
        self.secretKey = tuple(self.secretKey)
        self.publicKey = tuple(self.publicKey)

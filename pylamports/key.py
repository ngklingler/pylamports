import secrets
import hashlib


def hashEncode(number):
    return hashlib.sha256(str(number).encode()).hexdigest()


def hexToBin(hexString):
    """takes a hex string, converts it to a binary string, trims the '0b'
    prefix, and pads it with leading zeroes to ensure a 256 bit length"""
    binaryString = bin(int(hexString, 16))[2:]
    if len(binaryString) < 256:
        prefix = "0" * (256 - len(binaryString))
        binaryString = prefix + binaryString
    return binaryString


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

    def signMessageHash(self, messageHash):
        binString = hexToBin(messageHash)
        signatureArray = []
        for i in range(len(binString)):
            bit = int(binString[i])
            signatureArray.append(self.secretKey[i][bit])
        return tuple(signatureArray)

import secrets
import hashlib


def hashEncode(string):
    """Helper function to encode and hash string and return a hex string"""
    return hashlib.sha3_256(string.encode()).hexdigest()


def hexToBin(hexString):
    """takes a hex string, converts it to a binary string, trims the '0b'
    prefix, and pads it with leading zeroes to ensure a 256 bit length"""
    binaryString = bin(int(hexString, 16))[2:]
    if len(binaryString) < 256:
        prefix = "0" * (256 - len(binaryString))
        binaryString = prefix + binaryString
    return binaryString


class key:

    def __init__(self, seed=hex(secrets.randbits(256))[2:]):
        self.secretKey = []
        self.publicKey = []
        self.seed = seed
        for i in range(256):
            self.secretKey.append((hashEncode(self.seed + "0" + str(i)),
                                   hashEncode(self.seed + "1" + str(i))))
            self.publicKey.append((hashEncode(self.secretKey[i][0]),
                                   hashEncode(self.secretKey[i][1])))
        self.secretKey = tuple(self.secretKey)
        self.publicKey = tuple(self.publicKey)

    def saveSeed(self, filename="lamportSeed"):
        filename += ".sec"
        secretKeyFile = open(filename, "w")
        secretKeyFile.write(self.seed)
        secretKeyFile.close()

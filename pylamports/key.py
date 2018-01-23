import secrets
import hashlib
import fnmatch


def hashEncode(string):
    """Helper function to encode and hash string and return a hex string"""
    return hashlib.sha3_256(string.encode()).hexdigest()


class key:

    def __init__(self, seed=hex(secrets.randbits(256))[2:]):
        if fnmatch.fnmatch(seed, "*.*"):
            self.getSeed(seed)
        else:
            self.seed = seed
            self.__generateKeys()
        self.secretKey = tuple(self.secretKey)
        self.publicKey = tuple(self.publicKey)

    def saveSeed(self, filename="lamportSeed.sec"):
        seedFile = open(filename, "w")
        seedFile.write(self.seed)
        seedFile.close()

    def getSeed(self, filename="lamportSeed.sec"):
        seedFile = open(filename, "r")
        self.seed = seedFile.readline()
        self.seed = self.seed[:64]
        self.__generateKeys()

    def __generateKeys(self):
        self.secretKey = []
        self.publicKey = []
        for i in range(256):
            self.secretKey.append((hashEncode(self.seed + "0" + str(i)),
                                   hashEncode(self.seed + "1" + str(i))))
            self.publicKey.append((hashEncode(self.secretKey[i][0]),
                                   hashEncode(self.secretKey[i][1])))

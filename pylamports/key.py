import secrets
import hashlib
import fnmatch


def hashEncode(string):
    # gunna dump this function probably after conversion to b64
    """Helper function to encode and hash string and return a hex string"""
    return hashlib.sha3_256(string.encode()).hexdigest()


class key:

    def __init__(self, seed=hex(secrets.randbits(256))[2:]):  # see line 18
        # secrets.randbits.to_bytes(32, "big") to replace hex
        if fnmatch.fnmatch(seed, "*.*"):
            self.getSeed(seed)
        else:
            self.seed = seed  # put random seed generator here
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
        # gunna have to be fixed from [:64] once base 64
        self.seed = self.seed[:64]
        self.__generateKeys()

    def __generateKeys(self):
        # switch from array/tuple model to string of appended b64 strings
        self.secretKey = []
        self.publicKey = []
        for i in range(256):
            self.secretKey.append((hashEncode(self.seed + "0" + str(i)),
                                   hashEncode(self.seed + "1" + str(i))))
            # hashllib.sha3(seed + bytes("0") + bytes(str(i))).digest() or
            # something like that
            # do base64.b64encode(theAbove)
            self.publicKey.append((hashEncode(self.secretKey[i][0]),
                                   hashEncode(self.secretKey[i][1])))

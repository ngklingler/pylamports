import secrets


class key:

    def __init__(self):
        self.secretKey = []
        for i in range(256):
            self.secretKey.append((secrets.randbits(256),
                                   secrets.randbits(256)))

    def getSecretHex(self):
        secretKeyHex = []
        for i in range(256):
            secretKeyHex.append((hex(self.secretKey[i][0])[2:],
                                 hex(self.secretKey[i][1])[2:]))
        return tuple(secretKeyHex)

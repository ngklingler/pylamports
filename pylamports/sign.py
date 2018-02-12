class sign:
    # make it so it takes seed and generates b64 pieces as needed
    def __init__(self, message, key):
        # turn the message which is a hex string into a binary string
        self.message = bin(int(message, 16))[2:]
        # pad with necessary zeroes
        prefix = "0" * (256 - len(self.message))
        self.message = prefix + self.message
        self.key = key
        self.signature = []  # make it a string which substrng are appended to
        # hashlib_sha3(bin(seed) + {0,1} + bytes(str(i)))
        # base64.b64encode(theAbove)
        for i in range(len(self.message)):
            bit = int(self.message[i])
            self.signature.append(self.key[i][bit])
        # make it not a tuple but a b64 string
        self.signature = tuple(self.signature)

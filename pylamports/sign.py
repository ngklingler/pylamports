class sign:

    def __init__(self, message, key):
        # turn the message which is a hex string into a binary string
        self.message = bin(int(message, 16))[2:]
        # pad with necessary zeroes
        prefix = "0" * (256 - len(self.message))
        self.message = prefix + self.message
        self.key = key
        self.signature = []
        for i in range(len(self.message)):
            bit = int(self.message[i])
            self.signature.append(self.key[i][bit])
        self.signature = tuple(self.signature)

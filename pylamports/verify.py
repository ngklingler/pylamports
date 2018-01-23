import hashlib


def hashEncode(string):
    """Helper function to encode and hash string and return a hex string"""
    return hashlib.sha3_256(string.encode()).hexdigest()


def verify(messageHash, signatureArray, pubKey):
    """Takes three args: message, signature as generated by signMessage, and a
    public key, returns True/False as to whether signature is valid for public
    key"""
    binaryString = bin(int(messageHash, 16))[2:]
    prefix = "0" * (256 - len(binaryString))
    binaryString = prefix + binaryString
    hashOfSig = []
    verificationArray = []
    for i in range(len(signatureArray)):
        hashOfSig.append(hashEncode(signatureArray[i]))
    for i in range(len(binaryString)):
        bit = int(binaryString[i])
        verificationArray.append(pubKey[i][bit])
    if verificationArray == hashOfSig:
        return True
    else:
        return False

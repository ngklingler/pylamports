# pylamports
Implements Lamport signatures with keypair creation, signing of messages, and verification of signatures in python.

Read more about Lamport signatures [here.](https://en.wikipedia.org/wiki/Lamport_signature)

There are currently three files, one for the key class, one for the sign class, and one to verify signatures.

### To-do list:
* switch to b64 from hex so things can be stored in smaller ASCII
* for key class
    * print public key to file
    * remove sign class and put an attribute in key class self.sign
    * print self.sign, update it, save to file
* verify should differentiate between file and tuple form of publicKey
    * maybe get rid of tuple form all together for both keys
* eventually build a class to implement the [Merkle signature scheme](https://en.wikipedia.org/wiki/Merkle_signature_scheme)

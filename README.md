# pylamports
Implements Lamport signatures with keypair creation, signing of messages, and verification of signatures in python.

Read more about Lamport signatures [here.](https://en.wikipedia.org/wiki/Lamport_signature)

There are currently three files, one for the key class, one for the sign class, and one to verify signatures.

### To-do list:
* method in key class to print publicKey to file
* verify should differentiate between file and tuple form of publicKey
* method in key class to print signature to file with messages
* separate signature method to sign file and generate separate signature file vs sign string and store string and signature together as text
* eventually build a class to implement the [Merkle signature scheme](https://en.wikipedia.org/wiki/Merkle_signature_scheme)

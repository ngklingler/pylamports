# pylamports
Implements Lamport signatures with keypair creation, signing of messages, and verification of signatures in python.

Read more about Lamport signatures [here.](https://en.wikipedia.org/wiki/Lamport_signature)

Right now I just have the key class, which generates a key pair and allows you to sign a message with it.

### To-do list:
* method in key class to print publicKey to file
* method in key class to print signature to file with messages
* separate signature method to sign file and generate separate signature file vs sign string and store string and signature together as text
* eventually build a class to implement the [Merkle signature scheme](https://en.wikipedia.org/wiki/Merkle_signature_scheme)

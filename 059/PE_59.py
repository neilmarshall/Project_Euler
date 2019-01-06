#! /usr/bin/env python3.7

"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified
method is to use a password as a key. If the password is shorter than the
message, which is likely, the key is repeated cyclically throughout the
message. The balance for this method is using a sufficiently long password key
for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower
case characters. Using cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the knowledge that the plain
text must contain common English words, decrypt the message and find the sum of
the ASCII values in the original text.

Solution: 107359
"""

from itertools import cycle

class Cypher(object):
    """
    Class to decrypt a string of ASCII character codes using the XOR
    encryption / decryption algorithm, for a given key
    """
    def __init__(self, key):
        """
        Initialise with key to decrypt messages; if key is shorter than
        message to be decrypted then the key will repeat
        """
        self.key = key

    def encrypt(self, message):
        """
        Return encrypted message

        Args:
            message (string): Message to be encrypted

        Returns:
            int list: List of ASCII character codes for encrypted message
        """
        return [ord(k) ^ ord(c) for k, c in zip(cycle(self.key), message)]

    def decrypt(self, characters):
        """
        Return decrypted message
        
        Args:
            characters (int list): List of ASCII character codes to decrypt

        Returns:
            string: Decrypted message
        """
        return ''.join(chr(ord(k) ^ c) for k, c in zip(cycle(self.key), characters))


if __name__ == '__main__':
    with open("p059_cipher.txt", 'rt') as f:
        characters = map(int, f.read().split(','))
    message = Cypher("god").decrypt(characters)
    print(message, f"\nSolution: {sum(ord(c) for c in message)}", sep='\n')

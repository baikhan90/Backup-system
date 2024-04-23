from cryptography.fernet import Fernet
import logging
import argparse

class Encryptor:
    def __init__(self):
        # private.key was generate using Fernet symmetric encryption
        with open('./private.key', 'r') as file:
            self.key = file.read()

        self.cipher_suite = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher_suite.encrypt(data)

    def decrypt(self, encrypted_data):
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8') 


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    parser = argparse.ArgumentParser(description='CLI tool to decrypt and print file content.')
    parser.add_argument('--files', '-f', nargs='+', required=True, help='Files to decrypt and print')
    args = parser.parse_args()
    encryptor = Encryptor()

    for file in args.files:
        with open(file, 'rb') as file:
            print("File: {}".format(file.name))
            decrypted_data = encryptor.decrypt(file.read())
            print(decrypted_data)

if __name__ == "__main__":
    main()

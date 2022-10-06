from aes import AES

class AES_TEST():
    def __init__(self):
        master_key = 0x2b7e151628aed2a6abf7158809cf4f3c
        self.AES = AES(master_key)

        plaintext = 0x3243f6a8885a308d313198a2e0370734
        encrypted = self.AES.encrypt(plaintext)
        print(hex(encrypted[-1]))

if __name__ == '__main__':
    AES_TEST()
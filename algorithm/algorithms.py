import random
import gmpy2


class CommutativeEncrypter(object):
    def __init__(self, n):
        self.n = n

    @staticmethod
    def generate_modulus(key_size=1024):
        return CommutativeEncrypter.generate_prime(key_size)

    def encrypt(self, plaintext):
        pass

    def decrypt(self, ciphertext):
        pass

    @staticmethod
    def generate_prime(bit_length):
        left = 2 ** (bit_length - 1)
        right = 2 ** bit_length - 1
        while True:
            random_integer = random.randint(left, right)
            random_prime = gmpy2.next_prime(random_integer)
            if random_prime <= right:
                return random_prime


class PohligHellmanEncrypter(CommutativeEncrypter):
    def __init__(self, n):
        super(PohligHellmanEncrypter, self).__init__(n)

        while True:
            self.a = random.randint(1, self.n - 1)
            if gmpy2.gcd(self.a, self.n - 1) == 1:
                self.a_inverse = int(gmpy2.invert(self.a, self.n - 1))
                break

    def encrypt(self, plaintext):
        ciphertext = int(gmpy2.powmod(plaintext, self.a, self.n))
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = int(gmpy2.powmod(ciphertext, self.a_inverse, self.n))
        return plaintext


class AffineCipher(CommutativeEncrypter):
    def __init__(self, n, ratio):
        super(AffineCipher, self).__init__(n)

        self.ratio = ratio
        self.a = random.randint(1, self.n - 1)
        self.a_inverse = int(gmpy2.invert(self.a, self.n))
        self.b = (self.a - 1) * self.ratio % self.n

    def encrypt(self, plaintext):
        ciphertext = (plaintext * self.a + self.b) % self.n
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = (ciphertext - self.b) * self.a_inverse % self.n
        return plaintext

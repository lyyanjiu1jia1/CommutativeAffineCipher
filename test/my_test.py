from algorithm.algorithms import PohligHellmanEncrypter, AffineCipher, CommutativeEncrypter

ratio = int(1e4)
key_size = 1024
n = CommutativeEncrypter.generate_modulus(key_size)

ph1 = PohligHellmanEncrypter(n)
ph2 = PohligHellmanEncrypter(n)
ac1 = AffineCipher(n, ratio)
ac2 = AffineCipher(n, ratio)

plaintext = 323

print(ph2.encrypt(ph1.encrypt(plaintext)))
print(ph1.encrypt(ph2.encrypt(plaintext)))
print(ph1.decrypt(ph2.decrypt(ph2.encrypt(ph1.encrypt(plaintext)))))

print(ac2.encrypt(ac1.encrypt(plaintext)))
print(ac1.encrypt(ac2.encrypt(plaintext)))
print(ac1.decrypt(ac2.decrypt(ac2.encrypt(ac1.encrypt(plaintext)))))
print(ac2.decrypt(ac1.decrypt(ac2.encrypt(ac1.encrypt(plaintext)))))

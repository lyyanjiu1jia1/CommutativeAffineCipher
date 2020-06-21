import copy
import time

import numpy as np

from algorithm.algorithms import CommutativeEncrypter, PohligHellmanEncrypter, AffineCipher


def save_time(time_array, file_name):
    time_array = np.array(time_array)
    np.save(r'../plot/' + file_name + r'.npy', time_array)


id_length = int(1e5)
id_ph = [i for i in range(id_length)]
id_ac = copy.deepcopy(id_ph)

ratio = 5
key_size = 1024
n = CommutativeEncrypter.generate_modulus(key_size)

ph1 = PohligHellmanEncrypter(n)
ph2 = PohligHellmanEncrypter(n)
ac1 = AffineCipher(n, ratio)
ac2 = AffineCipher(n, ratio)

time_points_ph = []
time_points_ac = []

# ph
time_points_ph.append(time.time())
print(time.time() - time_points_ph[0])
for i in range(len(id_ph)):
    id_ph[i] = ph1.encrypt(id_ph[i])
    print("stage 0.{}".format(i))
time_points_ph.append(time.time() - time_points_ph[0])
print(time.time() - time_points_ph[0])
for i in range(len(id_ph)):
    id_ph[i] = ph2.encrypt(id_ph[i])
    print("stage 1.{}".format(i))
time_points_ph.append(time.time() - time_points_ph[0])
print(time.time() - time_points_ph[0])
for i in range(len(id_ph)):
    id_ph[i] = ph1.decrypt(id_ph[i])
    print("stage 2.{}".format(i))
time_points_ph.append(time.time() - time_points_ph[0])
print(time.time() - time_points_ph[0])
for i in range(len(id_ph)):
    id_ph[i] = ph2.decrypt(id_ph[i])
    print("stage 3.{}".format(i))
time_points_ph.append(time.time() - time_points_ph[0])
print(time.time() - time_points_ph[0])
save_time(time_points_ph, 'ph')

# ce
time_points_ac.append(time.time())
print(time.time() - time_points_ac[0])
for i in range(len(id_ac)):
    id_ac[i] = ac1.encrypt(id_ac[i])
    print("stage 0.{}".format(i))
time_points_ac.append(time.time() - time_points_ac[0])
print(time.time() - time_points_ac[0])
for i in range(len(id_ac)):
    id_ac[i] = ac2.encrypt(id_ac[i])
    print("stage 1.{}".format(i))
time_points_ac.append(time.time() - time_points_ac[0])
print(time.time() - time_points_ac[0])
for i in range(len(id_ac)):
    id_ac[i] = ac1.decrypt(id_ac[i])
    print("stage 2.{}".format(i))
time_points_ac.append(time.time() - time_points_ac[0])
print(time.time() - time_points_ac[0])
for i in range(len(id_ac)):
    id_ac[i] = ac2.decrypt(id_ac[i])
    print("stage 3.{}".format(i))
time_points_ac.append(time.time() - time_points_ac[0])
print(time.time() - time_points_ac[0])
save_time(time_points_ac, 'ac')


pass

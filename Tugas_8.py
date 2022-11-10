from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
    if (i+1)%2==0:
       print(i+1, "Genap - ID proses", getpid())
       sleep(1)
    else:
       print(i+1, "Ganjil - ID proses", getpid())
       sleep(1)

n = int(input("Masukkan Range Angka : "))

print("Sekuensial")

# sebagai waktu sebelum eksekusi
sekuensial_awal = time()

# mengproses
for i in range(n):
    cetak(i)

# sebagai waktu setelah eksekusi
sekuensial_akhir = time()

print("multiprocessing.Process")
# sebagai wadah seluruh proses
kumpulan_proses = []

# sebagai waktu sebelum eksekusi
process_awal = time()

# mengproses
for i in range(n):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()

# menyatukan keseluruhan proses
for i in kumpulan_proses:
    p.join()

# sebagai waktu setelah eksekusi
process_akhir = time()

print("multiprocessing.Pool")
# sebagai waktu sebelum eksekusi
pool_awal = time()

# mengproses
pool = Pool()
pool.map(cetak, range(0,n))
pool.close

# sebagai waktu sebelum eksekusi
pool_akhir = time()

print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")

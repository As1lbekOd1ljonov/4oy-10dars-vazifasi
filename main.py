# vazifa 1
import time
from multiprocessing import Process

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def raqamlar_yigindisi(royxat: list):
    i = 0
    count = 0
    while i < len(royxat):
        count += royxat[i]
        i += 1
        time.sleep(0.5)
    print(count)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=raqamlar_yigindisi, args=(l,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))



# vazifa 2
from multiprocessing import Process
import random
import time

l = [1,2,3,4,5,6,7,8,9,0]

def royxatni_aylatirish(royxat: list):
    for i in range(10):
        random.shuffle(royxat)
        time.sleep(1)
        print(royxat)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=royxatni_aylatirish, args=(l,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 3
from multiprocessing import Process
import time

numbers = [23, 45, 12, 9, 12, 76, 23, 94, 49, 10]
def min_max_qiymatlar(royxat: list):
    time.sleep(2)
    max_number = max(royxat)
    min_number = min(royxat)
    print(f"Eng katta son: {max_number}. Eng kichik son: {min_number}")

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=min_max_qiymatlar, args=(numbers,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 4
from multiprocessing import Process
import time

mevalar = ["Olma", "Anor", "Nok", "Uzum", "Banan", "Shaftoli"]


def tekshir(royxat, qiymat):
    print(f"{qiymat} uchun qidirilmoqda...")
    time.sleep(1)
    if qiymat in royxat:
        print(f"{qiymat} ro'yxatda mavjud.")
    else:
        print(f"{qiymat} ro'yxatda mavjud emas.")


if __name__ == "__main__":
    search = input("Qaysi mevani qidirmoqchisiz: ").capitalize()

    process = Process(target=tekshir, args=(mevalar, search))
    process.start()
    process.join()

    print("Tekshiruv tugadi.")

# ========================================================================

# vazifa 5
import time
from multiprocessing import Process

mevalar = ["Olma", "Anor", "Nok", "Nok", "Uzum", "Olma", "Banan","Olma", "Anor"]

def unikal_elementlar(royxat):
    unikal = []
    for element in royxat:
        time.sleep(1)
        if element not in unikal:
            unikal.append(element)
    print(unikal)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=unikal_elementlar, args=(mevalar,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 6
import time
from multiprocessing import Process

mevalar = ["Olma", "Anor", "Nok", "Uzum", "Banan", "Shaftoli"]
def teskari_soz(royxat: list):
    new_mevalar = []
    for i in royxat:
        time.sleep(1)
        new_mevalar.append(i[::-1])
    print(new_mevalar)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=teskari_soz, args=(mevalar,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 7
import time
from multiprocessing import Process

mevalar = ["Olma", "Anor", "Shaftoli", "Nok", "Uzum", "Banan"]

def eng_uzun_soz(royxat: list):
    max_word = max(royxat, key=len)
    time.sleep(2)
    print(max_word)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=eng_uzun_soz, args=(mevalar,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 8
import time
from multiprocessing import Process


lugat = {
    "bir": 10,
    "ikki": 20,
    "uch": 10,
    "to‘rt": 30,
    "besh": 20,
    "olti": 40
}

def takrorlangan_qiymatlar(lugat: dict):
    barcha_qiymatlar = list(lugat.values())

    takrorlar = set()
    for qiymat in barcha_qiymatlar:
        time.sleep(0.5)
        if barcha_qiymatlar.count(qiymat) > 1:
            takrorlar.add(qiymat)

    print(takrorlar)


start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=takrorlangan_qiymatlar, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 9
from multiprocessing import Process
import time

def qiymatlarni_saralash(lugat: dict):
    raqamlar = []
    for qiymat in lugat.values():
        time.sleep(0.5)
        if isinstance(qiymat, (int, float)):
            raqamlar.append(qiymat)
    print(sorted(raqamlar))

lugat = {
    "bir": 10,
    "ikki": 20.5,
    "uch": "matn",
    "to‘rt": 15,
    "besh": 30,
    "olti": "salom",
    "yetti": 5
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=qiymatlarni_saralash, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 10
from multiprocessing import Process
import time

def kopaytirish(lugat: dict):
    numbers = []
    for i in lugat.values():
        time.sleep(0.5)
        if isinstance(i, (int, float)):
            a = i * 2
            numbers.append(a)
    print(numbers)


lugat = {
    "bir": 10,
    "ikki": 20.5,
    "uch": "matn",
    "to‘rt": 15,
    "besh": 30,
    "olti": "salom",
    "yetti": 5
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=kopaytirish, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 11
from multiprocessing import Process
import time


def max_num(lugat: dict):
    numbers = []
    for i in lugat.values():
        time.sleep(0.5)
        if isinstance(i, (int, float)):
            numbers.append(i)

    max_number = max(numbers)
    print(max_number)

lugat = {
    "bir": 10,
    "ikki": 20.5,
    "uch": "matn",
    "to‘rt": 15,
    "besh": 30,
    "olti": "salom",
    "yetti": 5
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=max_num, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print(round(time.time() - start, 2))

# ========================================================================

# vazifa 12
from multiprocessing import Process
import time

def orta_qiymat(lugat: dict):
    numbers = []
    count = 0
    for i in lugat.values():
        time.sleep(0.5)
        if isinstance(i, (float, int)):
            numbers.append(i)
    for i in numbers:
        count += 1

    ortacha_qiymat = sum(numbers) / count

    print(ortacha_qiymat)

lugat = {
    "bir": 10,
    "ikki": 20.5,
    "uch": "matn",
    "to‘rt": 15,
    "besh": 30,
    "olti": "salom",
    "yetti": 5
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=orta_qiymat, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))

# ========================================================================

# vazifa 13
from multiprocessing import Process
import time

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
def dict_qoshish(dict1: dict, dict2: dict):
    merged_dict = {}
    for key in set(dict1) | set(dict2):
        time.sleep(0.5)
        merged_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)

    print(merged_dict)

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=dict_qoshish, args=(dict1, dict2))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))

# ========================================================================

# vazifa 14
import time
from multiprocessing import Process

def min_max_words(lugat: dict):
    words = []
    for i in lugat.keys():
        time.sleep(0.5)
        if isinstance(i, str):
            words.append(i)

    max_word = max(words, key=len)
    min_word = min(words, key=len)

    print(f"Eng uzun so‘z: {max_word}. Eng kalta so‘z: {min_word}")


lugat = {
    "on": 10,
    "ikki": 20.5,
    "uch": "matn",
    "tort": 15,
    "besh": 30,
    "olti": "salom",
    "yetti": 5
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=min_max_words, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))

# ========================================================================

# vazifa 15
import time
from multiprocessing import Process

def stringni_int_qilish(lugat: dict):
    for key, value in lugat.items():
        time.sleep(0.5)
        if isinstance(value, str) and value.isdigit():
            lugat[key] = int(value)
    print(lugat)
lugat = {
    "bir": "123",
    "ikki": "45a",
    "uch": "456",
    "to‘rt": 78,
    "besh": "9",
    "olti": "salom"
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=stringni_int_qilish, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))

# ========================================================================

# vazifa 16
import time
from multiprocessing import Process

def kopaytirish(lugat: dict):
    new_dict = {}
    for key, value in lugat.items():
        time.sleep(0.5)
        if isinstance(value, (int, float)):
            new_dict[key] = value * 2
        else:
            new_dict[key] = value
    print(new_dict)

lugat = {
    "bir": 10,
    "ikki": 20.5,
    "uch": "matn",
    "to‘rt": 15,
    "besh": 30,
    "olti": "salom"
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=kopaytirish, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))

# ========================================================================

# vazifa 17
import time
from multiprocessing import Process

def sozlarni_teskari_yozish(lugat: dict):
    new_dict = {}
    for key, value in lugat.items():
        time.sleep(0.5)
        if isinstance(value, str):
            new_dict[key] = value[::-1]
        else:
            new_dict[key] = value
    print(new_dict)

lugat = {
    "bir": "salom",
    "ikki": 123,
    "uch": "dunyo",
    "to‘rt": "matn",
    "besh": 45.6,
    "olti": "python"
}

start = time.time()

if __name__ == "__main__":
    process = []
    for i in range(10):
        pr = Process(target=sozlarni_teskari_yozish, args=(lugat,))
        pr.start()
        process.append(pr)

    for pr in process:
        pr.join()

    print("Ketgan vaqti: ",round(time.time() - start, 2))
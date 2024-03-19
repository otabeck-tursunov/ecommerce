# 4, 5, 6, ...

# 4
def kalta(ismlar: list):
    return min(ismlar, key=len)


# names = ['Nizomiddin', 'Foziljon', 'Umida']
# print(kalta(names))

# 5
def teskari(ism: str):
    return ism[::-1]


# print(teskari("Shaxzod"))

# 6
def musbat_manfiy(a: int, b: int, c: int):
    musbat = 0
    if a >= 0:
        musbat += 1
    if b >= 0:
        musbat += 1
    if c >= 0:
        musbat += 1
    manfiy = 3 - musbat
    print(f"Musbat: {musbat} ta \nManfiy: {manfiy} ta")


# musbat_manfiy(5, 231, -367)
# musbat_manfiy(1, -2, -10)


# 7
def qosh(key, value, dict):
    # dict[key] = value
    dict.update({key: value})


davlat = {
    "nom": "O'zbekiston",
    "poytaxt": "Toshkent"
}
qosh("valyuta", "so'm", davlat)
qosh("aholi", 38000000, davlat)
qosh("maydon", 448.97, davlat)


# print(davlat)

# 8
def tekshir(start, end, son):
    if son in list(range(start, end + 1)):
        return True
    else:
        return False


# print(tekshir(10, 100, 100))


teskari = lambda ism: print(ism[::-1])
# teskari("Otabek")
yigindi = lambda toplam: sum(toplam)


# print(yigindi([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 4! = 1 * 2 * 3 * 4 = 24
# 5! = 24 * 5 = 120
# 6! = 720 = 1 * 2 * 3 * 4 * 5 * 6
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(5))
# print(factorial(6))

def xona(son):
    if son // 10 == 0:
        return 1
    else:
        return 1 + xona(son // 10)


# print(xona(1234567890))

def hisobla(galaba, maglubiyat):  # hisobla(12, 18)
    bir_foiz = (galaba + maglubiyat) / 100
    galaba_foiz = galaba / bir_foiz
    return galaba_foiz


# print(hisobla(1, 4))

# ctrl + alt + l
# shift + enter
# alt + cursor
# a = int(input("a = "))
# b = int(input("b = "))

def iscouple(text):
    d = {}
    for i in range(len(text)):
        if text[i] in d.keys():
            d[text[i]] += 1
        else:
            d[text[i]] = 1
    values_list = list(d.values())
    values_unique = list(set(values_list))
    if len(values_unique) == 1:
        return True
    elif len(values_unique) == 2:
        if abs(values_unique[0] - values_unique[1]) == 1:
            katta = max(values_unique)
            if values_list.count(katta) == 1:
                return True
            return True
        return False
    return False


# print(iscouple("aaaaabbbbbbccccc"))
# 3


kub_daraja = lambda son: son ** 3


def kubdaraja(son):
    return son ** 3


# print(kub_daraja(2))
# print(kubdaraja(2))


def yigindi(son):  # 345   -> 5, 34
    if son < 10:
        return son
    else:
        q = son % 10
        return q + yigindi(son // 10)


def kun_soni(yil):
    if yil % 4 == 0:
        if yil % 100 == 0 and yil % 400 != 0:
            return 365
        else:
            return 366
    else:
        return 365


def rang(a: int, b: int):
    if (a + b) % 2 == 0:
        print("qora")
    else:
        print("oq")


def tekshir(x1, y1, x2, y2):
    if (x1 + x2) % 2 == (y1 + y2) % 2:
        return True
    else:
        return False


def ruh(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return True
    return False


def shoh(x1, y1, x2, y2):
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        return True
    else:
        return False

print(shoh(4, 2, 3, 1))
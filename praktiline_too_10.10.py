"""Matemaatilised tehted"""
import math

# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
a = float(input("Sisestage kaatet a: "))
# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks
b = float(input("Sisestage kaatet b: "))

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)
c = (a**2 + b**2)**0.5

ümbermõõt = a + b + c

pindala = (a * b) / 2

c = round(c, 2)
ümbermõõt = round(ümbermõõt, 2)
pindala = round(pindala, 2)

print(f"Hüpoteenus c: {c}")
print(f"Kolmnurga ümbermõõt: {ümbermõõt}")
print(f"Kolmnurga pindala: {pindala}")

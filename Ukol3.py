"""
Napište funkci, která určí, kolik prvočísel je v seznamu celých čísel. Seznam je předán jako parametr.
Výsledek je vrácen z funkce.
"""
def pocet_prvocisel(seznam_celych_cisel):
  pocet_prvocisel = 0
  for cislo in seznam_celych_cisel:
    if je_prvocislo(cislo):
      pocet_prvocisel += 1
  return pocet_prvocisel

def je_prvocislo(cislo):
  if cislo <= 1:
    return False
  elif cislo <= 3:
    return True
  elif cislo % 2 == 0 or cislo % 3 == 0:
    return False
  i = 5
  while i * i <= cislo:
    if cislo % i == 0 or cislo % (i + 2) == 0:
      return False
    i += 6
  return True

seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 , 17, 18, 19, 20]
pocet_prvocisel = pocet_prvocisel(seznam)
print(f"Počet prvočísel v seznamu {seznam} je: {pocet_prvocisel}")

"""
Napište funkci, která vypočítá mocninu každého prvku ze seznamu celých čísel.
Jako parametr se předává hodnota výkonu, jako parametr se předává také seznam.
Funkce vrátí nový seznam obsahující výsledky.
"""
def mocniny(seznam_celych_cisel, exponent):
  mocniny_seznamu = []
  for cislo in seznam_celych_cisel:
    mocnina = cislo ** exponent
    mocniny_seznamu.append(mocnina)
  return mocniny_seznamu


seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exponent = 3
vysledny_seznam = mocniny(seznam, exponent)
print(f"Mocniny čísel v seznamu {seznam} na exponent {exponent} jsou: {vysledny_seznam}")

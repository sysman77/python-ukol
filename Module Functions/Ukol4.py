"""
Napište funkci, která odstraní dané číslo ze seznamu celých čísel. Vrátí počet odstraněných prvků z funkce.
"""


def odstran_cislo(seznam_celych_cisel, cislo):
    pocet_smazanych = 0
    while cislo in seznam_celych_cisel:
        seznam_celych_cisel.remove(cislo)
        pocet_smazanych += 1
    return pocet_smazanych

seznam = [1, 2, 3, 4, 5, 1, 2, 3]
smazano = odstran_cislo(seznam, 3)
print(f"Bylo smazáno {smazano} trojek ze seznamu. Nový seznam: {seznam}")

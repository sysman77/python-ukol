"""
Napište funkci, která vypočítá součin prvků ze seznamu celých čísel. Seznam je předán jako parametr.
Výsledek je vrácen z funkce.
"""


def soucin_seznamu(seznam_celych_cisel):
    if not seznam_celych_cisel:
        return 0

    soucin = 1
    for cislo in seznam_celych_cisel:
        soucin *= cislo
    return soucin


seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
vysledek = soucin_seznamu(seznam)
print(f"Součin prvků v seznamu {seznam} je: {vysledek}")

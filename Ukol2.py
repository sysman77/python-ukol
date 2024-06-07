"""
Napište funkci, která najde minimum v seznamu celých čísel. Seznam je předán jako parametr.
Výsledek je vrácen z funkce.
"""


def najdi_minimum(seznam_celych_cisel):

    if not seznam_celych_cisel:
        return None

    return min(seznam_celych_cisel)


seznam = [1, 4, 2, -10, 5]
minimum = najdi_minimum(seznam)
print(f"Minimum v seznamu {seznam} je: {minimum}")

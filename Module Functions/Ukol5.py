"""
Napište funkci, která vezme dva seznamy jako parametr a vrátí seznam obsahující prvky obou seznamů.
"""

def sloucit_seznamy(seznam1, seznam2):
    return seznam1 + seznam2

seznam1 = [1, 2, 3, 4, 5]
seznam2 = [6, 7, 8, 9, 10]
sjednoceny_seznam = sloucit_seznamy(seznam1, seznam2)
print(f"Sloučený seznam: {sjednoceny_seznam}")

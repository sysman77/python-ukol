def pocet_vyskytu_slova(soubor, slovo):

  pocet_vyskytu = 0
  with open(soubor, 'r') as f:
    for radek in f:
      slova = radek.lower().split()  # Převedeme text na malá písmena a rozdělíme na slova
      for w in slova:
        if w == slovo:
          pocet_vyskytu += 1

  return pocet_vyskytu

if __name__ == "__main__":
  soubor = "soubor.txt"
  slovo = input("Zadejte slovo: ")

  pocet_vyskytu = pocet_vyskytu_slova(soubor, slovo)
  print(f"Slovo '{slovo}' se v souboru vyskytuje {pocet_vyskytu}krát.")

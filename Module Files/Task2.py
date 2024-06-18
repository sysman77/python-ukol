def analyzuj_text(soubor_vstup, soubor_vystup):

  with open(soubor_vstup, 'r') as f_vstup, open(soubor_vystup, 'w') as f_vystup:
    text = f_vstup.read()

    pocet_znaku = len(text)
    pocet_radku = text.count('\n') + 1  # Počítáme i prázdný řádek na konci
    pocet_samohlasenek = 0
    pocet_souhlasek = 0
    pocet_cisel = 0

    for znak in text:
      znak = znak.lower()
      if znak in "aeiouyáéíóúý":
        pocet_samohlasenek += 1
      elif znak.isdigit():
        pocet_cisel += 1
      elif znak.isalpha():
        pocet_souhlasek += 1

    f_vystup.write(f"Počet znaků: {pocet_znaku}\n")
    f_vystup.write(f"Počet řádků: {pocet_radku}\n")
    f_vystup.write(f"Počet samohlásek: {pocet_samohlasenek}\n")
    f_vystup.write(f"Počet souhlásek: {pocet_souhlasek}\n")
    f_vystup.write(f"Počet číslic: {pocet_cisel}\n")

if __name__ == "__main__":
  soubor_vstup = "soubor.txt"
  soubor_vystup = "statistiky.txt"

  analyzuj_text(soubor_vstup, soubor_vystup)
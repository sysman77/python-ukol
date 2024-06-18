def najdi_delku_nejdelsiho_radku(soubor):

  delka_nejdelsiho_radku = 0
  with open(soubor, 'r') as f:
    for radek in f:
      delka_radku = len(radek.rstrip())  # Odstranění mezer na konci řádku
      if delka_radku > delka_nejdelsiho_radku:
        delka_nejdelsiho_radku = delka_radku

  return delka_nejdelsiho_radku

if __name__ == "__main__":
  soubor = "soubor.txt"
  delka_nejdelsiho_radku = najdi_delku_nejdelsiho_radku(soubor)
  print(f"Délka nejdelšího řádku: {delka_nejdelsiho_radku}")

def porovnej_radky(soubor1, soubor2):

  with open(soubor1, 'r') as f1, open(soubor2, 'r') as f2:
    radky1 = f1.readlines()
    radky2 = f2.readlines()

    for i, (radek1, radek2) in enumerate(zip(radky1, radky2)):
      if radek1 != radek2:
        print(f"Neshoda v řádku {i + 1}:")
        print(f"Soubor 1: {radek1}")
        print(f"Soubor 2: {radek2}")

if __name__ == "__main__":
  soubor1 = "soubor1.txt"
  soubor2 = "soubor2.txt"

  porovnej_radky(soubor1, soubor2)

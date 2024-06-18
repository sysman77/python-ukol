def remove_last_line(vstupni_soubor, vystupni_soubor):

    # Načtení obsahu vstupního souboru
    with open(vstupni_soubor, 'r') as file:
        lines = file.readlines()

    # Zkontrolování, zda soubor není prázdný
    if lines:
        # Odstranění posledního řádku
        lines = lines[:-1]

    # Zápis upraveného obsahu do výstupního souboru
    with open(vystupni_soubor, 'w') as file:
        file.writelines(lines)

vstupni_soubor = "soubor.txt"
vystupni_soubor = "del_last_line.txt"
remove_last_line(vstupni_soubor, vystupni_soubor)

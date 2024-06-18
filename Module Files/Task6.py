def nahrad_slovo(soubor, slovo_k_hledani, slovo_k_nahrazeni):

    # Načtení obsahu vstupního souboru
    with open(soubor, 'r') as f_vstup:
        obsah = f_vstup.read()

    # Nahrazení hledaného slova
    novy_obsah = obsah.replace(slovo_k_hledani, slovo_k_nahrazeni)

    # Zápis upraveného obsahu zpět do souboru
    with open(soubor, 'w') as f_vystup:
        f_vystup.write(novy_obsah)

if __name__ == "__main__":
    soubor = "soubor.txt"
    slovo_k_hledani = input("Zadejte slovo, které chcete hledat: ")
    slovo_k_nahrazeni = input(f"Zadejte slovo, kterým chcete slovo '{slovo_k_hledani}' nahradit: ")

    nahrad_slovo(soubor, slovo_k_hledani, slovo_k_nahrazeni)
    print(f"Slovo '{slovo_k_hledani}' bylo v souboru '{soubor}' nahrazeno slovem '{slovo_k_nahrazeni}'.")
def viiva(pituus, sana):
    if sana == "":
        sana = "*"
    print(pituus * sana[0])

def risulaatikko(korkeus):
    # täällä tulee kutsua funktiota viiva sopivilla parametreilla
    kertaa = 1
    while kertaa <= korkeus:
        viiva(10, "#")
        kertaa += 1


# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risulaatikko(5)

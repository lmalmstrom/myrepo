def viiva(pituus, sana):
    if sana == "":
        sana = "*"
    print(pituus * sana[0])

def risulaatikko(korkeus):

    kertaa = 1
    while kertaa <= korkeus:
        viiva(10, "#")
        kertaa += 1



if __name__ == "__main__":
    risulaatikko(5)

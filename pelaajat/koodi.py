# tee ratkaisusi tänne
import json
class Pelaaja:
    def __init__(self, name: str, nationality: str, assists: int, goals: int, penalties: int, team: str, games: int):
        self.__nimi = name
        self.__kansallisuus = nationality
        self.__syotot = assists
        self.__maalit = goals
        self.__rangaistusminuutit = penalties
        self.__joukkue = team
        self.__pelit = games

    def __str__(self):
        return f"{self.__nimi:21}{self.__joukkue:3}{self.__maalit:>4} + {self.__syotot:>2} ={(self.__maalit+self.__syotot):>4}"

    @property
    def nimi(self):
        return self.__nimi

    @property
    def joukkue(self):
        return self.__joukkue

    @property
    def maa(self):
        return self.__kansallisuus

    @property
    def maalit(self):
        return self.__maalit

    @property
    def syotot(self):
        return self.__syotot

    @property
    def pelit(self):
        return self.__pelit

class PelaajaLuettelo:
    def __init__(self):
        self.__luettelo = []

    def lisaa_pelaaja(self, pelaaja: 'Pelaaja'):
        self.__luettelo.append(pelaaja)

    def tulosta_kaikki(self):
        for pelaaja in self.__luettelo:
            print(pelaaja)

    def hae_pelaaja(self, nimi: str):
        for pelaaja in self.__luettelo:
            if pelaaja.nimi == nimi:
                return pelaaja
        return None

    def hae_joukkueet(self):
        joukkueet = []
        for pelaaja in self.__luettelo:
            if pelaaja.joukkue not in joukkueet:
                joukkueet.append(pelaaja.joukkue)
        return joukkueet

    def hae_maat(self):
        maat = []
        for pelaaja in self.__luettelo:
            if pelaaja.maa not in maat:
                maat.append(pelaaja.maa)
        return maat    
        
    def hae_joukkueen_pelaajat(self, joukkue: str):
        pelaajat = []
        for pelaaja in self.__luettelo:
            if pelaaja.joukkue == joukkue:
                pelaajat.append((pelaaja,pelaaja.maalit+pelaaja.syotot))


        def pisteet(alkio):
            return alkio[1]
        return sorted(pelaajat, key=pisteet, reverse=True)

    def hae_maan_pelaajat(self, maa: str):
        pelaajat = []
        for pelaaja in self.__luettelo:
            if pelaaja.maa == maa:
                pelaajat.append((pelaaja,pelaaja.maalit+pelaaja.syotot))


        def pisteet(alkio):
            return alkio[1]
        return sorted(pelaajat, key=pisteet, reverse=True)

    def hae_pisteiden_mukaan(self, maara: int):

        pelaajat = []
        for pelaaja in self.__luettelo:
            pelaajat.append((pelaaja,pelaaja.maalit+pelaaja.syotot))
        def pisteet(alkio):
            return alkio[1]
        pelaajat = sorted(pelaajat, key=pisteet, reverse=True)
        return pelaajat[:maara]

    def hae_maalien_mukaan(self, maara: int):
        pelaajat = []
        for pelaaja in self.__luettelo:
            pelaajat.append(pelaaja)
        def maalit(alkio):
            return alkio.maalit
        pelaajat = sorted(pelaajat, key=lambda pelaaja: (pelaaja.maalit,-pelaaja.pelit),reverse=True)
        return pelaajat[:maara] 

class Sovellus:
    def __init__(self):
        self.__luettelo = PelaajaLuettelo()
        tiedostonimi = input("tiedosto: ")
#        tiedostonimi = "osa.json"
        self.lue_tiedosto(tiedostonimi)
        self.suorita()

    def lue_tiedosto(self,tiedostonimi):
        with open(tiedostonimi,) as data:
            data = data.read()
        data = json.loads(data)
        lkm = 0
        for peluri in data:
            lkm += 1
            pelaaja = Pelaaja(peluri["name"],peluri["nationality"],peluri["assists"],peluri["goals"],peluri["penalties"],peluri["team"],peluri["games"])

            self.__luettelo.lisaa_pelaaja(pelaaja)
        print(f"luettiin {lkm} pelaajan tiedot")
        print()

    def suorita(self):
        self.ohje()
        while True:
            komento = input("komento: ")
            
            if komento == "0":
                break
            if komento == "1":
                self.hae_pelaaja()
            if komento == "2":
                self.hae_joukkueet()
            if komento == "3":
                self.hae_maat()
            if komento == "4":
                self.joukkueen_pelaajat()
            if komento == "5":
                self.maan_pelaajat()
            if komento == "6":
                self.eniten_pisteita()
            if komento == "7":
                self.eniten_maaleja()
        
    def ohje(self):
        print("komennot:")
        print("0 lopeta")
        print("1 hae pelaaja")
        print("2 joukkueet")
        print("3 maat")
        print("4 joukkueen pelaajat")
        print("5 maan pelaajat")
        print("6 eniten pisteitä")
        print("7 eniten maaleja")

    def hae_pelaaja(self):
        haettava_pelaaja = input("nimi: ")
        pelaaja = self.__luettelo.hae_pelaaja(haettava_pelaaja)
        print(pelaaja)

    def hae_joukkueet(self):
        joukkueet = self.__luettelo.hae_joukkueet()
        for joukkue in sorted(joukkueet):
            print(joukkue)

    def hae_maat(self):
        maat = self.__luettelo.hae_maat()
        for maa in sorted(maat):
            print(maa)
    
    def joukkueen_pelaajat(self):
        joukkue = input("joukkue: ")
        pelaajat = self.__luettelo.hae_joukkueen_pelaajat(joukkue)
        for pelaaja in pelaajat:
            print(pelaaja[0])

    def maan_pelaajat(self):
        maa = input("maa: ")
        pelaajat = self.__luettelo.hae_maan_pelaajat(maa)
        for pelaaja in pelaajat:
            print(pelaaja[0])

    def eniten_pisteita(self):
        maara = int(input("kuinka monta: "))
        pelaajat = self.__luettelo.hae_pisteiden_mukaan(maara)
        for pelaaja in pelaajat:
            print(pelaaja[0])

    def eniten_maaleja(self):
        maara = int(input("kuinka monta: "))
        pelaajat = self.__luettelo.hae_maalien_mukaan(maara)
        for pelaaja in pelaajat:
            print(pelaaja)

#luettelo = PelaajaLuettelo()
#lue_tiedosto("kaikki.json")
#luettelo.tulosta_kaikki()

#a = Sovellus()

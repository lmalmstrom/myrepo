using System;
using System.Text;
using System.Collections.Generic;

class Program
{

    ///pitää loopin käynnissä
    private static bool jatko = true;

    //käynnistää valintafunktion joka pitää ohjelman käynnissä
    static void Main()
    {
        
        Console.WriteLine("Lukumuunnin");
        Console.WriteLine("-----------");
        Valinta();
    }

    //pääfunktio, jonka kautta muuta ohjelmaa pyöritetään
    private static void Valinta()
    {
        while(jatko)
        {
        Console.WriteLine("Binääri- vai heksalukumuunto?");
        Console.WriteLine("\tb - Binääri");
        Console.WriteLine("\th - Heksa");
        Console.WriteLine("\tl - Lopeta");
        Console.Write("Valintasi?");
        Switsi(Console.ReadLine());
        }
    }

    //Käsittelee valinnan binäärin ja heksan välillä, muuttaa myös jatkofunktion ja lopettaa ohjelman
    private static void Switsi(string valinta)
    {
        switch(valinta)
        {
        case "b":
        Console.WriteLine("Binääri");
        BinaariValitsin();
        break;

        case "h":
        Console.WriteLine("Heksa");
        HeksaValitsin();
        break;
        

        case "l":
        jatko = false;
        break;
        }
    }

    //Kysyy 10- ja binäärijärjestelmän välillä, välittää muuttujan itse muuntimeen
    private static void BinaariValitsin()
    {
        Console.WriteLine("Muutetaanko 10- vai binäärijärjestelmän luku?");
        Console.WriteLine("\t1 - 10-järjestelmä");
        Console.WriteLine("\tb - binäärijärjestelmä");
        BinaariMuunnin(Console.ReadLine());
    }

    //Hoitaa varsinaisen muunnoksen käyttäjän antamasta luvusta. EI osaa käsitellä virheellisiä muuttujia
    private static void BinaariMuunnin(string valinta)
    {
        if(valinta == "1")
        {
            Console.WriteLine("-------------------------");
            Console.WriteLine("Anna 10-järjestelmän luku");
            int luku = Int32.Parse(Console.ReadLine());
            Console.WriteLine("-------------------------");

            int potenssi = 0;
            potenssi = PotenssiHaku(potenssi, luku);

            StringBuilder palautusLuku = new StringBuilder();
            if(potenssi==0) palautusLuku.Append("0");

            while( potenssi != 0)
            {
                if(potenssi <= luku)
                {
                    luku -= potenssi;
                    palautusLuku.Append("1");
                }
                else palautusLuku.Append("0");

                potenssi = potenssi / 2;
            }

            Console.WriteLine("Binäärilukusi on: " + palautusLuku);
            Console.WriteLine("-----------------");
        }

        else if(valinta == "b")
        {
            Console.WriteLine("----------------");
            Console.WriteLine("Anna binääriluku");
            StringBuilder luku = new StringBuilder(Console.ReadLine());
            Console.WriteLine("----------------");
            
            double palautusLuku = 0;
            double luvunPituus = luku.Length-1;

            for(int indeksi = 0; indeksi < luku.Length; indeksi++)
            {
                if(luku[indeksi] != '0')
                {
                    palautusLuku += Math.Pow(2,luvunPituus);
                }
                luvunPituus --;
            }

            Console.WriteLine("Desimaaliluku on: " + palautusLuku);
            Console.WriteLine("-----------------");
            return;
        }

        else
        {
            Console.WriteLine("Epäkelpo valinta, valitse uudestaan");
            return;
        }

    }
    
    //Hakee binäärimuuntoa varten oikean potenssin
    private static int PotenssiHaku(int potenssi, int luku)
        {

        while((Math.Pow(2,potenssi))<=luku)
            {
                potenssi++;
            }
        return Convert.ToInt32((Math.Pow(2,potenssi-1)));
        }

    // Kysyy 10- ja heksajärjestelmän välillä, välittää muuttujan itse muuntimeen
    private static void HeksaValitsin()
    {
        Console.WriteLine("Muutetaanko 10- vai heksajärjestelmän luku?");
        Console.WriteLine("\t1 - 10-järjestelmä");
        Console.WriteLine("\th - heksajärjestelmä");
        HeksaMuunnin(Console.ReadLine());
    }

    //Hoitaa varsinaisen muunnoksen käyttäjän antamasta luvusta. EI osaa käsitellä virheellisiä muuttujia
    private static void HeksaMuunnin(string valinta)
    {
        Dictionary<string, string> lukuTaulukko = new Dictionary<string, string>(){
            {"A","10"},
            {"B","11"},
            {"C","12"},
            {"D","13"},
            {"E","14"},
            {"F","15"},
            {"10","A"},
            {"11","B"},
            {"12","C"},
            {"13","D"},
            {"14","E"},
            {"15","F"}
        };

        if(valinta == "1")
        {
            Console.WriteLine("-------------------------");
            Console.WriteLine("Anna 10-järjestelmän luku");
            int luku = Int32.Parse(Console.ReadLine());
            Console.WriteLine("-------------------------");

            StringBuilder palautusLuku = new StringBuilder();

            int jakoTulos = luku/16;
            int jakoJaannos = luku%16;

            while(jakoTulos != 0)
            {
                if(jakoJaannos > 9) palautusLuku.Append(lukuTaulukko[jakoJaannos.ToString()]);
                else palautusLuku.Append(jakoJaannos);
                
                jakoJaannos = jakoTulos%16;
                jakoTulos = jakoTulos/16;
            }

            if(jakoJaannos > 9) palautusLuku.Append(lukuTaulukko[jakoJaannos.ToString()]);
            else palautusLuku.Append(jakoJaannos);
            
            palautusLuku = SbKaanto(palautusLuku);
            Console.WriteLine("Heksaluku on: " + palautusLuku);
            Console.WriteLine("-----------------");


        }
        if(valinta == "h")
        {
            Console.WriteLine("-------------------------");
            Console.WriteLine("Anna heksaluku");
            String luku = Console.ReadLine();
            Console.WriteLine("-------------------------");

            int palautusLuku = 0;
            string merkki;
            int potenssi =luku.Length - 1;

            for(int indeksi = 0; indeksi < luku.Length; indeksi++)
            {

                merkki = luku[indeksi].ToString();

                if(char.IsDigit(merkki[0]) == false)
                {
                    merkki = Char.ToUpper(merkki[0]).ToString();
                    merkki = lukuTaulukko[merkki];
                }

                palautusLuku += Convert.ToInt32(Convert.ToInt32(merkki) * Math.Pow(16,potenssi));
                potenssi --;
            }

            Console.WriteLine("Desimaaliluku on: " + palautusLuku);
            Console.WriteLine("-----------------");
        }
    }


    //Kääntää stringbuilder-muuttujan ympäri
    private static StringBuilder SbKaanto(StringBuilder teksti)
    {
        StringBuilder palautus = new StringBuilder();

        for(int indeksi = teksti.Length -1; indeksi >=0; indeksi--)
        {
            palautus.Append(teksti[indeksi]);
        }
        return palautus;
    }
}
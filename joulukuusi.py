def joulukuusi(x):
    print("joulukuusi!")
    kertaa = 1
    tyhjaa = x
    tahtia = 1
   
    while kertaa <= x:
        print(" " *(tyhjaa-1), end ="")
        print("*" *tahtia) 

        tyhjaa -=1
        kertaa +=1
        tahtia = tahtia + 2
    print(" " * (x-1) + "*")
    
# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    koko = int(input("Kuinka iso joulukuusi?: "))
    joulukuusi(koko)



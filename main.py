betoltott = []

with open("adatok.txt", "r", encoding="utf-8") as file:
    for line in file:
        betoltott.append(line)

print("Üdv!\n1. Adatok listázása\n2. Adatok listázása fájlba...\n3. Keresés...")
valasz = int(input("A menüpontok közül válasszon egyet: "))
if valasz == 1:
    for i in betoltott:
        for j in i:
            print(j, end="")
        print()
elif valasz == 2:
    fajlnev = input("Adj meg egy fájlnevet: ")
    fajlnev = fajlnev + ".txt"
    print(fajlnev)
elif valasz == 3:
    print("ok")
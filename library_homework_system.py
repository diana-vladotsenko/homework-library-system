fail = "raamatukogud.txt"
faili_avamine = open(fail,"r",encoding = "UTF-8")
raamatukogud = list()
linnad = list()
raamatukogude_arv_linnas = list()
raamatute_arvud = list()
lugejate_arvud = list()

for andmed in faili_avamine:
    raamatukogu,linn,arv_linnas,raamatute_arv,lugejate_arv = andmed.split(";")
    raamatukogud.append(raamatukogu)
    linnad.append(linn)
    raamatukogude_arv_linnas.append(int(arv_linnas))
    raamatute_arvud.append(int(raamatute_arv))
    lugejate_arvud.append(int(lugejate_arv))

faili_avamine.close()
print()

# Leia raamatukogu, kus on kõige rohkem raamatuid.
# Kuvage selle raamatukogu nimi, asukoht ja raamatute arv.
suurem_tulemus = 0
for i in range(len(raamatute_arvud)):
    if raamatute_arvud[i]>suurem_tulemus:
        #Savime tulemuse, et võrrelda seda tsüklis
        suurem_tulemus = raamatute_arvud[i]
        #Panin siia indeksi, et ma saaks aru mis linnas ja raamatukogus selline kogus raamatuid asub. Kui ma paneks i, siis ta kuvaks tsükli viimase numbri, millal ta jäi ehk 3 ja see oleks teine raamatukogu
        indeks = i
print(f"Kõige rohkem raamatuid arvuga {suurem_tulemus} on raamatukogus {raamatukogud[indeks]} linnas {linnad[indeks]}")

# Keskmise lugejate arvu arvutamine:
# Arvuta ja trüki välja keskmine lugejate arv kõigi raamatukogude kohta.
print()

summa = 0
for i in range(len(raamatukogud)):
    summa = summa + lugejate_arvud[i]
keskmine = round(summa/ len(lugejate_arvud),2)
print(f"Keskmine lugejate arv kõigi raamatute kohta on {keskmine}.  *Ümmardatud kuni sajani.")

# Raamatute ja kogude suhte leidmine:
# Arvuta igas raamatukogus raamatute arv ühe kogu kohta ja salvesta tulemused uude listi.
# Kuvage iga raamatukogu nimi ja raamatute/kogude suhe.
tulemused = list()
for i in range(len(raamatukogud)):
    suhe = round(raamatute_arvud[i]/raamatukogude_arv_linnas[i])
    print("Raamatukogu",raamatukogud[i],"kogude suhega",suhe)
    tulemused.append(suhe)
print(tulemused)
print()

# Küsige kasutajalt minimaalne raamatute arv ja kuvage kõik raamatukogud, kus on rohkem raamatuid kui kasutaja sisestatud arv.
kasutaja_min_arv = int(input("Sisesta raamatute minimaalne arv: "))
arv = 0
print("Loeme raamatukogud, kus on rohkem raamatuid, kui teie poolt sisestatud arv...")
for i in range(len(raamatute_arvud)):
    if raamatute_arvud[i] > kasutaja_min_arv:
        arv = arv + 1
        print(raamatukogud[i])
if arv == 0:
    print("Kahjuks, selliseid pole.")
print()

# Loenda, mitu raamatukogu on igas linnas (nt Tallinn, Tartu jne). Kuvage tulemused.
for i in range(len(raamatukogude_arv_linnas)):
    print(linnad[i] ,"on kokku",raamatukogude_arv_linnas[i],"raamatukogu")
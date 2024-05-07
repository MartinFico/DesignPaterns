    def __str__(self):
        return f"{self.vyrobce} {self.model} - Kapacita: {self.kapacita}, Aktuální počet cestujících: {self.aktualni_passazieri}"

    def nastoupit_passaziera(self, pocet_passazieru):
        if self.aktualni_passazieri + pocet_passazieru <= self.kapacita:
            self.aktualni_passazieri += pocet_passazieru
            print(f"{pocet_passazieru} cestujících nastoupilo.")
        else:
            print("Nedostatek kapacity pro nastoupení.")

    def vystoupit_passaziera(self, pocet_passazieru):
        if self.aktualni_passazieri - pocet_passazieru >= 0:
            self.aktualni_passazieri -= pocet_passazieru
            print(f"{pocet_passazieru} cestujících vystoupilo.")
        else:
            print("Neplatný počet cestujících.")

# Vytvoření instance třídy Letadlo
letadlo = Letadlo("Boeing", "747", 400, 100)

# Zabalit objekt letadla pomocí pickle
with open("letadlo.pickle", "wb") as soubor:
    pickle.dump(letadlo, soubor)

# Rozbalit objekt letadla pomocí pickle
with open("letadlo.pickle", "rb") as soubor:
    rozbalene_letadlo = pickle.load(soubor)

print("Rozbalené informace o letadle:")
print(rozbalene_letadlo)

# Příklad použití metod objektu rozbaleného letadla
rozbalene_letadlo.nastoupit_passaziera(50)
print(rozbalene_letadlo)
rozbalene_letadlo.vystoupit_passaziera(20)
print(rozbalene_letadlo)


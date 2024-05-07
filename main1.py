import pickle

class Letadlo:
    def __init__(self, vyrobce, model, kapacita, aktualni_passazieri):
        self.vyrobce = vyrobce
        self.model = model
        self.kapacita = kapacita
        self.aktualni_passazieri = aktualni_passazieri

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

    def zabalit(self, nazev_souboru):
        with open(nazev_souboru, "wb") as soubor:
            pickle.dump(self, soubor)

    @staticmethod
    def rozbalit(nazev_souboru):
        with open(nazev_souboru, "rb") as soubor:
            return pickle.load(soubor)


letadlo = Letadlo("Boeing", "747", 400, 100)


with open("letadlo.pickle", "wb") as soubor:
    pickle.dump(letadlo, soubor)


with open("letadlo.pickle", "rb") as soubor:
    rozbalene_letadlo = pickle.load(soubor)

print("Rozbalené informace o letadle:")
print(rozbalene_letadlo)


rozbalene_letadlo.nastoupit_passaziera(50)
print(rozbalene_letadlo)
rozbalene_letadlo.vystoupit_passaziera(20)
print(rozbalene_letadlo)
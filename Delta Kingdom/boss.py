import random as r

class DeltaHero:
    def __init__(self, isim, bitirme_durumu, can, defans, guc, adelta):
        self.isim = "⚔️ Delta Hero"
        self.bitirme_durumu = False
        self.can = r.randint(300, 350)
        self.defans = 25
        self.guc = 50
        self.adelta = 2500

delta_hero = DeltaHero("", False, 0, 0, 0, 0)

import random as r

class oyuncu:
    def __init__(self, isim, delta, seviye, xp, envanter, maxhp, guc, hp, defans):
        self.isim = input("Karakter ismini giriniz: ")
        self.delta = 500
        self.seviye = 1
        self.xp = 20
        self.envanter = {
            "delta": 100,
            "food": 5,
            "potion": 2
        }
        self.guc = r.randint(25, 40)
        self.maxhp = r.randint(100, 125)
        self.hp = self.maxhp
        self.defans = r.randint(10, 20)
    def karakter_bilgisi(self):
        print(f"Karakter İsmi: {self.isim}")
        print(f"Delta: {self.delta}")
        print(f"Seviye: {self.seviye}")
        print(f"XP: {self.xp}")
        print(f"Envanter: {self.envanter}")
        print(f"Güç: {self.guc}")
        print(f"HP: {self.hp}")
        print(f"Defans: {self.defans}")
    def seviye_atla(self):
        if self.xp >= 100:
            self.seviye += 1
            self.xp -= 100 
            self.maxhp += 100
            self.guc += r.randint(5, 10)
            self.hp += r.randint(20, 30)
            self.defans += r.randint(5, 10)
            print(f"Tebrikler! {self.isim} seviyesi {self.seviye} oldu.")
class dusman:
    def __init__(self, isim, guc, hp, defans):
        self.isim = r.choice([
            "💰 Hırsız",
            "💰 Haydut",
            "⚔️ Şovalye",
            "⚔️ Prens",
            "🔥 Ejderha",
            "🎭 Soytarı",
            "🧙‍♂️ Büyücü"
        ])
        self.guc = r.randint(15, 30)
        self.hp = r.randint(80, 120)
        self.defans = r.randint(5, 15)
    def dusman_bilgisi(self):
        print(f"Düşman İsmi: {self.isim}")
        print(f"Güç: {self.guc}")
        print(f"HP: {self.hp}")
        print(f"Defans: {self.defans}")
if __name__ == "__main__":
    oyuncu1 = oyuncu("", 0, 0, 0, {}, 0, 0, 0, 0)
    print("=== OYUNCU STATSSI ===")
    oyuncu1.karakter_bilgisi()
def dusmanstat():
    print("\n=== DÜŞMAN STATI ===")
    dusman1 = dusman("", 0, 0, 0)
    dusman1.dusman_bilgisi()

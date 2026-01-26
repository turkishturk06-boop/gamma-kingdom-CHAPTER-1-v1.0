import random as r

class oyuncu:
    def __init__(self):
        self.isim = input("İsmini gir: ")
        self.seviye = 1
        self.can = 100
        self.guc = r.randint(25, 30)
        self.altin = 0
        self.iksir = 2

    def bilgileri_goster(self):
        print(
            f"\n🧙 OYUNCU\n"
            f"İsim   : {self.isim}\n"
            f"Seviye : {self.seviye}\n"
            f"Can    : {self.can}\n"
            f"Güç    : {self.guc}\n"
            f"Altın  : {self.altin}\n"
            f"İksir  : {self.iksir}\n"
        )


class dusman:
    def __init__(self):
        self.isim = r.choice([
            "🎭  Soytarı", "⚔️  Prens", "⚔️  Şövalye",
            "🥷  Ninja", "👑  Kraliçe", "🪖  Asker",
            "🪄  Büyücü", "💰  Hırsız", "🔥  Ejderha"
        ])
        self.seviye = 1
        self.can = r.randint(80, 120)
        self.guc = r.randint(20, 35)

    def bilgileri_goster(self):
        print(
            f"\n🚨 DÜŞMAN\n"
            f"{self.isim}\n"
            f"Seviye : {self.seviye}\n"
            f"Can    : {self.can}\n"
            f"Güç    : {self.guc}\n"
        )

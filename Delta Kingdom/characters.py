import random as r
import builtins

def get_text(key, *args):
    """Dil dosyasından metni al"""
    try:
        text_dict = getattr(builtins, 'text', {})
        text = text_dict.get(key, key)
        if args:
            return text.format(*args)
        return text
    except Exception:
        return key

class oyuncu:
    def __init__(self, isim=""):
        self.isim = isim if isim else "Player"
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
        self.zirh_seviyesi = 0
        self.kilic_seviyesi = 0
        self.maden_seviyesi = 2
        # Görev sistemi için alanlar
        self.aktif_gorev = None
        self.tamamlanan_gorevler = []
        # Eklenen özellikler (önceki zırh/kılıç bonusları)
        self.onceki_zirh_defansi = 0
        self.onceki_kilic_gucu = 0
    
    def karakter_bilgisi(self):
        print(get_text("character_name", self.isim))
        print(get_text("delta", self.delta))
        print(get_text("level", self.seviye))
        print(get_text("xp", self.xp))
        print(get_text("inventory", self.envanter))
        print(get_text("power", self.guc))
        print(get_text("hp", self.hp, self.maxhp))
        print(get_text("defense", self.defans))
    
    def seviye_atla(self):
        if self.xp >= 100:
            self.seviye += 1
            self.xp -= 100 
            self.maxhp += 100
            self.guc += r.randint(5, 10)
            self.hp += r.randint(20, 30)
            self.defans += r.randint(5, 10)
            print(get_text("level_up", self.isim, self.seviye))

class dusman:
    def __init__(self, isim=""):
        # Düşman isimleri dil dosyasından alınıyor
        enemy_names = [
            get_text("enemy_thief"),
            get_text("enemy_bandit"),
            get_text("enemy_knight"),
            get_text("enemy_prince"),
            get_text("enemy_dragon"),
            get_text("enemy_jester"),
            get_text("enemy_wizard")
        ]
        self.isim = r.choice(enemy_names)
        self.guc = r.randint(15, 30)
        self.hp = r.randint(80, 120)
        self.defans = r.randint(5, 15)
    
    def dusman_bilgisi(self):
        print(f"👹 {get_text('character_name', self.isim)}")
        print(get_text("power", self.guc))
        print(get_text("hp", self.hp, self.hp))
        print(get_text("defense", self.defans))

# Global instance oluştur (core.py tarafından kullanılır)
oyuncu_instance = oyuncu()
dusman_instance = dusman()

if __name__ == "__main__":
    print("=== ⚔️ OYUNCU STATSI ===")
    oyuncu_instance.karakter_bilgisi()
    print("\n=== 👹 DÜŞMAN STATI ===")
    dusman_instance.dusman_bilgisi()

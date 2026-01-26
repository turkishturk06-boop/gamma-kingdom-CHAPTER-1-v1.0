from classes import oyuncu, dusman
import random as r
import time as t
import os



def savas(oyuncu1, dusman1):
    print("\n⚔ SAVAŞ BAŞLADI!\n")

    while oyuncu1.can > 0 and dusman1.can > 0:
        dusman1.can -= oyuncu1.guc
        print(f"{oyuncu1.isim} vurdu → {dusman1.isim} can: {dusman1.can}")

        if dusman1.can <= 0:
            print(f"\n🎉 {dusman1.isim} yenildi!")
            break

        oyuncu1.can -= dusman1.guc
        print(f"{dusman1.isim} vurdu → {oyuncu1.isim} can: {oyuncu1.can}")

        if oyuncu1.can <= 0:
            print(f"\n💀 {oyuncu1.isim} yenildi!")
            break


# 🔽 OLUŞTURMA
oyuncu1 = oyuncu()
dusman1 = dusman()

# ✅ DOĞRU STAT GÖSTERME
oyuncu1.bilgileri_goster()

def savas_basla():
    sdec = r.choice([True, False])
    if sdec:
        t.sleep(0)
        savas(oyuncu1, dusman1)
        t.sleep(5)
    else:
        t.sleep(5)
def oyun_baslat():
    print("Oyun başlatılıyor...")
    oyuncu1.bilgileri_goster()
oyun_baslat()


def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')
    
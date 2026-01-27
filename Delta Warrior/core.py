import os
import random as r
import time
from characters import oyuncu, dusman
from boss import kral1
def ekran_temizle():
    os.system("cls" if os.name == "nt" else "clear")
def savas():
    while True:
        try:
            while oyuncu.hp or dusman.hp > 0:
                sinput = input(f"{dusman.isim} geldi ( 1) savaş / 2) yemek / 3) iksir / 4) bağışla)").lower()
                if sinput == "1":
                    oyuncu.hp -= (dusman.guc - oyuncu.defans)
                    print(f"{dusman.isim} sana {dusman.guc - oyuncu.defans} hasar verdi. Kalan HP: {oyuncu.hp}")
                    dusman.hp -= (oyuncu.guc - dusman.defans)
                    print(f"Sen {dusman.isim}'e {oyuncu.guc - dusman.defans} hasar verdin. Kalan HP: {dusman.hp}")
                    time.sleep(2)
                    if dusman.hp <= 0:
                        print(f"Tebrikler! {dusman.isim} yenildi.")
                        oyuncu.xp += 50
                        oyuncu.delta += alan_deltası
                        oyuncu.seviye_atla()
                        break
                    elif oyuncu.hp <= 0:
                        print("Düşman tarafından yenildin.")
                        oyuncu.hp += 50
                        oyuncu.xp += 20
                        break
                    elif sinput == "2":
                        if oyuncu.envanter["food"] > 0:
                            oyuncu.hp += 30
                            oyuncu.envanter["food"] -= 1
                            print(f"Yemek yedin. Kalan HP: {oyuncu.hp}, Kalan yemek: {oyuncu.envanter['food']}")
                            continue
                        else:
                            print("Yeterli yemeğin yok!")
                        continue
                    elif sinput == "3":
                        if oyuncu.envanter["potion"] > 0:
                            oyuncu.hp += 70
                            oyuncu.envanter["potion"] -= 1
                            print(f"İksir içtin. Kalan HP: {oyuncu.hp}, Kalan iksir: {oyuncu.envanter['potion']}")
                            continue
                        else:
                            print("Yeterli iksirın yok!")
                        continue
                    elif sinput == "4":
                        print(f"{dusman.isim} seni affetti ve gitti.")
                        oyuncu.delta += 20
                        oyuncu.xp += 10
                        break
        except ValueError:
            print("Geçersiz giriş, lütfen tekrar deneyin.")
            continue
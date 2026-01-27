import json
import os
import sys
from characters import oyuncu

FILE_NAME = "save_dosyasi.json"
def save_game(oyuncu_obj):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(oyuncu_obj.__dict__, f, indent=4, ensure_ascii=False)
    print("\n[OK] Oyun kaydedildi.")
def load_game():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            veri = json.load(f)
            yuklenen_oyuncu = oyuncu(**veri)
            print(f"\n[OK] {yuklenen_oyuncu.isim} geri yüklendi.")
            return yuklenen_oyuncu
    else:
        print("\n[!] Kayıt bulunamadı. Yeni karakter oluşturuluyor.")
        isim = input("Karakter ismi: ")
        return oyuncu(isim)
def quit_game(oyuncu_obj):
    cevap = input("\nÇıkmadan önce kaydetmek ister misin? (e/h): ").lower()
    if cevap == 'e':
        save_game(oyuncu_obj)
    print("Oyun kapatılıyor... Görüşmek üzere!")
    sys.exit()
from classes import oyuncu
from core import savas, savas_basla, temizle
import time as t
def harita():
     while True:
        try:
            secim = input("""\n🗺️  Haritaya Hoşgeldiniz! ne yapacaksınız ?
                1) 🏰 Krallığa Git
                2) 🏠 Han
                3) 🛒 Mağaza
                4) 🌾 Çiftlik
                5) 📊 İstatistikler
                6) 📁 Kayıt/Yükle
                7) 📚 Kütüphane
                8) ✖️ Çıkış
            """)
            if secim == "1":
                print("🏰 Krallığa gidiyorsunuz...")
                t.sleep(2)
                temizle()
                kcevap = input("""Krallıktasınız Ne yapmak istersiniz ?
                               1) Savaş Alanına Git
                               2) Han
                               3) Kaydet/Yükle
                               4) İstatistikler
                               5) Karanlık Mağaza
                               6) Çıkış
                               """)
            elif secim == "2":
                print("🏠 Han'a gidiyorsunuz...")
                t.sleep(20)
                temizle()
                print("50 can ve iksir aldınız! ama 50 altın ödüyorsunuz.")
                oyuncu.can += 50
                oyuncu.iksir += 1
                oyuncu.altin -= 50
                t.sleep(5)
            elif secim == "3":
                print("🛒 Mağazaya gidiyorsunuz...")
                t.sleep(2)
                temizle()
                print("""Mağazaya Hoşgeldiniz ! Ne almak istersiniz ?
                      a) Zırh
                        1) Hafif Zırh - 50 Altın (+5 Defans)
                        2) Orta Zırh - 125 Altın (+15 Defans)
                        3) Ejderha Zırhı 350 Altın (+40 Defans)
                        4) Karanlık Zırh - 500 Altın (+70 Defans)
                      b) Silah
                        1) Hafif Kılıç - 100 Altın (+5 Hasar)
                        2) Orta Kılıç - 200 Altın (+15 Hasar)
                        3) Ejderha Kılıcı - 400 Altın (+40 Hasar)
                        4) Karanlık Kılıç - 600 Altın (+70 Hasar)
                      c) İksir (50 altın)
                      d) yemek (30 altın)
                      e) Çıkış
                      """)  
            elif secim == "4":
                print("🌾 Çiftliğe gidiyorsunuz...")
                t.sleep(60)
                temizle()
                print("yemek buldunuz !")
                oyuncu.yemek += 1
            elif secim == "5":
                print("📊 İstatistiklerinizi görüntülüyorsunuz...")
                t.sleep(2)
                temizle()
                oyuncu.istatistikler()
            elif secim == "6":
                print("📁 Kayıt/Yükle menüsüne gidiyorsunuz...")
            elif secim == "7":
                print("📚 Kütüphaneye gidiyorsunuz...")
                t.sleep(2)
                temizle()
                print("""Kitaplardan hangisini okumak istersiniz ?
                      1) Savaşçı
                      2) Yıkılmaz Savunma
                      3) Savunma Yıkıcı
                      4) Krallığa Saldırı
                      5) Saldırı sonrası
                      6) Çıkış
                      """)
            elif secim == "8":
                print("Çıkış yapılıyor...")
                break
        except ValueError:
            print("Geçersiz giriş, lütfen tekrar deneyin.")
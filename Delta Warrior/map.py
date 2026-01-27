from core import ekran_temizle, chapter_kontrolü
from library import library

def map():
    ekran_temizle()
    while True:
        try:
            hinput = input(""":     ===== Delta Krallığındasın nereye gideceksin ? =====     :
                    1) 🗺️ Harita
                    2) 🏬 Mağaza
                    3) 📁 Kaydet/Yükle
                    4) 📝 Görev
                    5) 🎣 Aktivite
                    6) ⚔️ Arena
                    7) 🔺 Delta Marketi
                    8) 📙 Büyük Kütüphane
                    9) 🧪 Uzay Laboratuvarı
                    10) 🚁 Helipad (Kaçış)
                    11) ☹️ Oyundan Çık
Seçimin:
""")
            if hinput == "1":

            elif hinput == "2":

            elif hinput == "3":
                  
            elif hinput == "4":

            elif hinput == "5":

            elif hinput == "6":

            elif hinput == "7":    
            
            elif hinput == "8":
                library()
            elif hinput == "9":
                
            elif hinput == "10":
                if chapter_kontrolü():
                    ekran_temizle()
                    print("Helipad çalışıyor. Güvenli bir şekilde kaçtın!")
                    break
                else:
                    ekran_temizle()
                    print("Helipad kapalı. Kralı yenmeden kullanamazsın.")
                    continue
            elif hinput == "11":
                break
        except ValueError:
            print("Geçersiz Giriş")
            continue
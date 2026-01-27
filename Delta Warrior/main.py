from map import map
from saving import load_game, quit_game
from core import ekran_temizle
def main_menu():
    ekran_temizle(9)
    while True:
        try:
            menu_input = input("""
            ╔════════════════════════════════════╗
            ║   DELTA WARRIOR - ANA MENÜ         ║
            ║                                    ║
            ║  1) Yeni Oyun Başlat               ║
            ║  2) Oyunu Yükle                    ║
            ║  3) Çıkış                          ║
            ║                                    ║
            ╚════════════════════════════════════╝
            Seçimin: """).lower()
            
            if menu_input == "1":
                ekran_temizle
                from characters import oyuncu
                oyuncu_obj = oyuncu("", 0, 0, 0, {}, 0, 0, 0, 0)
                map()
            elif menu_input == "2":
                ekran_temizle
                oyuncu_obj = load_game()
                map()
            elif menu_input == "3":
                ekran_temizle
                from characters import oyuncu
                oyuncu_obj = oyuncu("", 0, 0, 0, {}, 0, 0, 0, 0)
                quit_game(oyuncu_obj)
            else:
                ekran_temizle
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
        except KeyboardInterrupt:
            print("\nOyun kapatılıyor...")
            break

if __name__ == "__main__":
    main_menu()

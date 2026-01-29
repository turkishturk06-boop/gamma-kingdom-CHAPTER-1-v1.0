import os
import builtins

def ekran_temizle():
    os.system("cls" if os.name == "nt" else "clear")

# Dil seçimi ÖNCE
ekran_temizle()
print("""
╔═══════════════════════════════════════╗
║    🎮 DELTA KINGDOM / KRALLIGI       ║
╚═══════════════════════════════════════╝
""")

lang_input = input("🌍 Dil seç / Choose language (tr/en): ").lower().strip()

if lang_input == "en":
    from lang_en import TEXT as text
else:
    from lang_tr import TEXT as text

# Seçilen dili global bir değişken olarak tanımlıyoruz ki diğer dosyalar erişebilsin
builtins.text = text

from map import map
from saving import load_game, quit_game
from characters import oyuncu

def main_menu():
    ekran_temizle()
    print(text.get("welcome", ""))

    while True:
        try:
            title = text.get("main_menu", "MAIN MENU")
            opt1 = text.get("new_game", "1) New Game")
            opt2 = text.get("load_game", "2) Load Game")
            opt3 = text.get("quit", "3) Quit")

            menu_text = f"""
╔══════════════════════════════════════╗
║ {title.center(36)} ║
║                                      ║
║ {opt1.ljust(36)} ║
║ {opt2.ljust(36)} ║
║ {opt3.ljust(36)} ║
║                                      ║
╚══════════════════════════════════════╝
"""
            menu_input = input(menu_text + text.get("enter_choice", "> ")).strip()

            if menu_input == "1":
                ekran_temizle()
                # İsim sor - Dil seçimi YAPILDIKTAN sonra
                player_name = input(text.get("enter_name")).strip()
                if not player_name:
                    player_name = "Player" if lang_input == "en" else "Oyuncu"
                oyuncu_obj = oyuncu(player_name)
                map()

            elif menu_input == "2":
                ekran_temizle()
                oyuncu_obj = load_game()
                map()

            elif menu_input == "3":
                ekran_temizle()
                quit_game(oyuncu("Player" if lang_input == "en" else "Oyuncu"))
                break
            else:
                ekran_temizle()
                print(text.get("invalid_choice", "❌ Invalid choice!"))

        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main_menu()

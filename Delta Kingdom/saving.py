import json
import os
import sys
import builtins
from characters import oyuncu

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

def ekran_temizle():
    os.system("cls" if os.name == "nt" else "clear")

def save_game(oyuncu_obj):
    ekran_temizle()
    while True:
        slot = input(get_text("choose_slot")).strip()
        if slot in ["1", "2", "3", "4", "5"]:
            file_name = f"save_slot_{slot}.json"
            try:
                with open(file_name, "w", encoding="utf-8") as f:
                    json.dump(oyuncu_obj.__dict__, f, indent=4, ensure_ascii=False)
                print(get_text("game_saved", slot))
                break
            except Exception as e:
                print(f"❌ {e}")
                break
        else:
            print(get_text("invalid_slot"))

def load_game():
    ekran_temizle()
    slots = []
    for i in range(1, 6):
        file_name = f"save_slot_{i}.json"
        if os.path.exists(file_name):
            slots.append(str(i))
    
    if not slots:
        print(get_text("no_saves"))
        isim = input(get_text("enter_name")).strip()
        yeni_oyuncu = oyuncu(isim if isim else "Oyuncu")
        return yeni_oyuncu
    
    print(get_text("available_saves"))
    for slot in slots:
        print(get_text("slot", slot, slot))
    
    while True:
        slot = input("\n" + get_text("choose_load_slot")).strip()
        if slot in slots:
            file_name = f"save_slot_{slot}.json"
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    veri = json.load(f)
                    yuklenen_oyuncu = oyuncu()
                    for key, value in veri.items():
                        setattr(yuklenen_oyuncu, key, value)
                    print(get_text("game_loaded", yuklenen_oyuncu.isim, slot))
                    return yuklenen_oyuncu
            except Exception as e:
                print(f"❌ {e}")
                return oyuncu()
        else:
            print(get_text("invalid_slot"))

def quit_game(oyuncu_obj):
    cevap = input(get_text("save_before_exit")).lower().strip()
    if cevap == 'e' or cevap == 'y':
        save_game(oyuncu_obj)
    print(get_text("goodbye"))
    sys.exit()

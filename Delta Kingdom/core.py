import os
import random as r
import time
import builtins
from characters import oyuncu, dusman, oyuncu_instance, dusman_instance
from boss import DeltaHero, delta_hero

oyuncu = oyuncu_instance
dusman = dusman_instance
alan_deltası = 100

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

def savas():
    global dusman
    dusman.guc = r.randint(15, 30)
    dusman.hp = r.randint(80, 120)
    dusman.defans = r.randint(5, 15)
    
    while True:
        try:
            while oyuncu.hp > 0 and dusman.hp > 0:
                sinput = input(get_text("enemy_appeared", dusman.isim)).lower()
                if sinput == "1":
                    hasar_oyuncu = max(0, dusman.guc - oyuncu.defans)
                    hasar_dusman = max(0, oyuncu.guc - dusman.defans)
                    
                    oyuncu.hp -= hasar_oyuncu
                    dusman.hp -= hasar_dusman
                    
                    print(get_text("took_damage", dusman.isim, hasar_oyuncu, oyuncu.hp))
                    print(get_text("dealt_damage", dusman.isim, hasar_dusman, dusman.hp))
                    time.sleep(2)
                    
                    if dusman.hp <= 0:
                        print(get_text("enemy_defeated", dusman.isim))
                        oyuncu.xp += 50
                        oyuncu.delta += alan_deltası
                        # Görev ilerlemesini güncelle
                        try:
                            if getattr(oyuncu, 'aktif_gorev', None) and oyuncu.aktif_gorev.get('type') == 'kill':
                                oyuncu.aktif_gorev['progress'] = oyuncu.aktif_gorev.get('progress', 0) + 1
                                print(get_text("quest_progress", oyuncu.aktif_gorev['progress'], oyuncu.aktif_gorev['target']))
                        except Exception:
                            pass
                        oyuncu.seviye_atla()
                        break
                    elif oyuncu.hp <= 0:
                        print(get_text("player_defeated"))
                        oyuncu.hp += 50
                        oyuncu.xp += 20
                        break
                        
                elif sinput == "2":
                    if oyuncu.envanter["food"] > 0:
                        oyuncu.hp += 30
                        oyuncu.envanter["food"] -= 1
                        print(get_text("ate_food", oyuncu.hp, oyuncu.envanter['food']))
                        continue
                    else:
                        print(get_text("not_enough_food"))
                    continue
                    
                elif sinput == "3":
                    if oyuncu.envanter["potion"] > 0:
                        oyuncu.hp += 70
                        oyuncu.envanter["potion"] -= 1
                        print(get_text("drank_potion", oyuncu.hp, oyuncu.envanter['potion']))
                        continue
                    else:
                        print(get_text("not_enough_potion"))
                    continue
                    
                elif sinput == "4":
                    print(get_text("enemy_forgave", dusman.isim))
                    oyuncu.delta += 20
                    oyuncu.xp += 10
                    break
            break
        except ValueError:
            print(get_text("invalid_input"))
            continue

def boss_savas():
    global delta_hero
    delta_hero.can = r.randint(300, 350)
    delta_hero.defans = 25
    delta_hero.guc = 50
    print(get_text("boss_appearing"))
    
    while True:
        try:
            while oyuncu.hp > 0 and delta_hero.can > 0:
                sinput = input(get_text("boss_appeared", delta_hero.isim)).lower()
                
                if sinput == "1":
                    hasar_oyuncu = max(0, delta_hero.guc - oyuncu.defans)
                    hasar_boss = max(0, oyuncu.guc - delta_hero.defans)
                    
                    oyuncu.hp -= hasar_oyuncu
                    delta_hero.can -= hasar_boss
                    
                    print(get_text("took_damage", delta_hero.isim, hasar_oyuncu, oyuncu.hp))
                    print(get_text("dealt_damage", delta_hero.isim, hasar_boss, delta_hero.can))
                    time.sleep(2)
                    
                    if delta_hero.can <= 0:
                        print(get_text("boss_defeated", delta_hero.isim))
                        delta_hero.bitirme_durumu = True
                        oyuncu.xp += 500
                        oyuncu.delta += 2500
                        # Boss görevi varsa da ilerlet
                        try:
                            if getattr(oyuncu, 'aktif_gorev', None) and oyuncu.aktif_gorev.get('type') == 'boss':
                                oyuncu.aktif_gorev['progress'] = oyuncu.aktif_gorev.get('progress', 0) + 1
                                print(get_text("quest_progress", oyuncu.aktif_gorev['progress'], oyuncu.aktif_gorev['target']))
                        except Exception:
                            pass
                        oyuncu.seviye_atla()
                        break
                    elif oyuncu.hp <= 0:
                        print(get_text("boss_player_defeated"))
                        oyuncu.hp += 50
                        oyuncu.xp += 100
                        break
                        
                elif sinput == "2":
                    if oyuncu.envanter["food"] > 0:
                        oyuncu.hp += 30
                        oyuncu.envanter["food"] -= 1
                        print(get_text("ate_food", oyuncu.hp, oyuncu.envanter['food']))
                        continue
                    else:
                        print(get_text("not_enough_food"))
                    continue
                    
                elif sinput == "3":
                    if oyuncu.envanter["potion"] > 0:
                        oyuncu.hp += 70
                        oyuncu.envanter["potion"] -= 1
                        print(get_text("drank_potion", oyuncu.hp, oyuncu.envanter['potion']))
                        continue
                    else:
                        print(get_text("not_enough_potion"))
                    continue
                    
                elif sinput == "4":
                    print(get_text("boss_no_escape"))
                    continue
            break
        except ValueError:
            print(get_text("invalid_input"))
            continue

def chapter_kontrolü():
    try:
        return bool(delta_hero.bitirme_durumu)
    except Exception:
        return False
